import array 
import math
import os
from in_circle_parallel import draw_canvas,draw_circle


def writePPM(red, green, blue, width, height, filename):
    ppm_header = f'P6 {width} {height} {255}\n'
    rgb = []
    for i in range(len(red)):
        rgb.append(red[i]) # Red 
        rgb.append(green[i]) # Green 
        rgb.append(blue[i]) # Blue
    image = array.array('B', rgb)

    with open(filename + '.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)

def cuadro_inicial(width, height):
    red = []
    green=[]
    blue=[]
    for i in range(height*width):
        red.append(0)
        green.append(0)
        blue.append(0)
    return [red, green, blue]



""" def draw_circle(circulo, cuadro, width, height):
    red = cuadro[0]
    green = cuadro[1]
    blue = cuadro[2]

    #circulo=[ejex,ejey,radio,red,green,blue]
    eje_Y=int(circulo[0])
    eje_X=int(circulo[1])
    radio=int(circulo[2])
    color_red=int(circulo[3])
    color_green=int(circulo[4])
    color_blue=int(circulo[5])

    for i in range(height):
        for j in range(width):
            if(in_circle(eje_X-1,eje_Y-1,i,j,radio)):
                index = j+i*width
                red[index]=comprobar_pixel(red[index],color_red)
                green[index]=comprobar_pixel(green[index],color_green)
                blue[index]=comprobar_pixel(blue[index],color_blue)

    cuadro = [red, green, blue] """
    
if __name__ == "__main__":
    input=open("input")
    n_circulos=int(input.readline())

    width = 1024
    height = 960
    #cuadro = cuadro_inicial(width, height)
    cuadro =  draw_canvas(width, height)

    for i in range(n_circulos):
        #circulo=[ejex,ejey,radio,red,green,blue]
        
        linea=input.readline()
        circulo=linea[:len(linea)-1].split(" ")
        circulo_int=[int(i) for i in circulo]
        #draw_circle(array.array("i",circulo_int), array.array("i",cuadro[0]),array.array("i",cuadro[1]),array.array("i",cuadro[2]), width, height)
        draw_circle(array.array("i",circulo_int),cuadro,width,height)

    writePPM(cuadro[0], cuadro[1], cuadro[2], width, height, "salida")
    
    input.close()