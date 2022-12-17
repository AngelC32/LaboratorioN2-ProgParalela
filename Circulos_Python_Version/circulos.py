import array 
import math
import os
#import time

def writePPM(red, green, blue, width, height, filename):
    '''
        Pinta y guarda una imagen segun un nombre de archivo dado en 
        formato ppm según un largo, ancho y 3 canales de color.
        
        Nota: La función presente fue distribuida por el docente del
              curso y modificada por los integrantes del grupo.
    '''

    ppm_header = f'P6 {width} {height} {255}\n'
    rgb = []
    for i in range(len(red)):
        rgb.append(red[i])      # Red 
        rgb.append(green[i])    # Green 
        rgb.append(blue[i])     # Blue
    image = array.array('B', rgb)

    with open(filename + '.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)

def comprobar_pixel(oldPixel,newPixel):
    '''
        Aplica una operación XOR (OR exclusiva) a 2 datos y devuelve
        el resultado.
    '''

    return oldPixel ^ newPixel

def in_circle(Cx,Cy,x,y,r):
    '''
        Verifica y devuelve True o False si los puntos "x" e "y" se 
        encuentran dentro de la circunferencia de ecuación:

                    (Cx - x)^2 + (Cy - y)^2 = r^2
    '''

    return (math.pow((Cx-x),2) + math.pow(Cy-y,2)) <= (math.pow(r,2))

def draw_canvas(width, height):
    '''
        Pinta un lienzo totalmente en negro según un alto y ancho
        especificado y lo devuelve.
    '''

    red = []
    green=[]
    blue=[]
    for i in range(height*width):
        red.append(0)
        green.append(0)
        blue.append(0)

    return [red, green, blue]

def draw_circle(circulo, cuadro, width, height):
    '''
        Dibuja un "circulo" dentro de un "cuadro" de alto y ancho
        especificado y lo devuelve:

        Recibe:
            circulo: Lista con los datos del circulo [x,y,r,R,G,B]
            cuadro: lienzo en el que se pintaran los circulos
    '''

    red = cuadro[0]
    green = cuadro[1]
    blue = cuadro[2]

    eje_Y=int(circulo[0])
    eje_X=int(circulo[1])
    radio=int(circulo[2])
    color_red=int(circulo[3])
    color_green=int(circulo[4])
    color_blue=int(circulo[5])

    # Recorriendo el cuadro
    for i in range(height):
        for j in range(width):
            if(in_circle(eje_X,eje_Y,i,j,radio)):
                index = j+i*width

                red[index]=comprobar_pixel(red[index],color_red)
                green[index]=comprobar_pixel(green[index],color_green)
                blue[index]=comprobar_pixel(blue[index],color_blue)

    cuadro = [red, green, blue]
    
if __name__ == "__main__":
    input=open("input")
    n_circulos=int(input.readline())

    width = 1024
    height = 960
    cuadro = draw_canvas(width, height)

    #start = time.time()

    # Bucle para pintar cada circulo uno tras otro
    for i in range(n_circulos):
        #Lectura de datos
        linea=input.readline()
        circulo=linea[:len(linea)-1].split(" ")
        
        draw_circle(circulo, cuadro, width, height)

    #end = time.time()
    #elapsed = end - start
    #print(elapsed)

    writePPM(cuadro[0], cuadro[1], cuadro[2], width, height, "salida")

    input.close()