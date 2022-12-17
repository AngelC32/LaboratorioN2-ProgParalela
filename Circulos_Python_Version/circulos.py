import array 
import math
import os
import time

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

def comprobar_pixel(oldPixel,newPixel):
    return oldPixel ^ newPixel

def in_circle(Cx,Cy,x,y,r):
    return (math.pow((Cx-x),2) + math.pow(Cy-y,2)) <= (math.pow(r,2))

def draw_canvas(width, height):
    red = []
    green=[]
    blue=[]
    for i in range(height*width):
        red.append(0)
        green.append(0)
        blue.append(0)

    return [red, green, blue]

def draw_circle(circulo, cuadro, width, height):
    red = cuadro[0]
    green = cuadro[1]
    blue = cuadro[2]

    eje_Y=int(circulo[0])
    eje_X=int(circulo[1])
    radio=int(circulo[2])
    color_red=int(circulo[3])
    color_green=int(circulo[4])
    color_blue=int(circulo[5])

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

    start = time.time()

    for i in range(n_circulos):
        
        linea=input.readline()
        circulo=linea[:len(linea)-1].split(" ")
        
        draw_circle(circulo, cuadro, width, height)

    end = time.time()
    elapsed = end - start

    print(elapsed)

    writePPM(cuadro[0], cuadro[1], cuadro[2], width, height, "salida")

    input.close()