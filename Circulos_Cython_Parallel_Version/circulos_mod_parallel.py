import array 
import math
from draw_processing_parallel import draw_canvas,draw_circle
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
    
if __name__ == "__main__":
    input=open("input")
    n_circulos=int(input.readline())

    width = 1024
    height = 960
    cuadro =  draw_canvas(width, height)    #Funcion Modulo Cython

    #start = time.time()

    # Bucle para pintar cada circulo uno tras otro
    for i in range(n_circulos):
        
        #Lectura de datos
        linea=input.readline()
        circulo=linea[:len(linea)-1].split(" ")

        circulo_int=[int(i) for i in circulo]
        draw_circle(array.array("i",circulo_int),cuadro,width,height)  #Funcion Modulo Cython

    #end = time.time()
    #elapsed = end - start
    #print(elapsed)

    writePPM(cuadro[0], cuadro[1], cuadro[2], width, height, "salida")
    
    input.close()