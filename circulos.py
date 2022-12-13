import array 
import math
import os
def writePPM(red, green, blue, width, height, filename):
  # todo archivo necesita una cabecera, en PPM la cabecera inicia con P6 e indica el anchoe, alto y valor maximo
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

def readPPM(path):
    red = []
    green = []
    blue = []
    width = 0
    height = 0
    with open(path, "rb") as f:
        # read header
        header = f.read(2)
        f.read(1) # blank
        width = f.read(3)
        f.read(1) # blank
        height = f.read(3)
        f.read(1) # blank
        max_val = f.read(3) # blank
        while (byte := f.read(1)):
            r = int.from_bytes(byte, byteorder='big')
            red.append(r) # R
            g = int.from_bytes(f.read(1), byteorder='big')
            green.append(g) # G
            b = int.from_bytes(f.read(1), byteorder='big')
            blue.append(b) # B 
            
    #return red,green,blue
    return blue,red,green

def comprobar_pixel(oldPixel,newPixel):
    return oldPixel ^ newPixel
def in_circle(Cx,Cy,x,y,r):
    if((math.pow((abs(Cx-x)),2)+math.pow(abs(Cy-y),2))<=(math.pow(r,2))):
        return True
    else:
         return False

def cuadro_inicial():
    red = []
    green=[]
    blue=[]
    width = 1024
    height = 960
    for i in range(height*width):
        red.append(0)
        green.append(0)
        blue.append(0)
    writePPM(red,green,blue, width, height, "circles")

def draw_circle(circulo):
    red = []
    green=[]
    blue=[]
    red,green,blue=readPPM("circles.ppm") 
    width = 1024
    height = 960
    #circulo=[ejex,ejey,radio,red,green,blue]
    ejeX=int(circulo[0])
    ejeY=int(circulo[1])
    radio=int(circulo[2])
    colorred=int(circulo[3])
    colorgreen=int(circulo[4])
    colorblue=int(circulo[5])
    for i in range(height):
        for j in range(width):
            if(in_circle(ejeX,ejeY,i,j,radio)):
                index = i+j*width
                red[index]=comprobar_pixel(red[index],colorred)
                green[index]=comprobar_pixel(green[index],colorgreen)
                blue[index]=comprobar_pixel(blue[index],colorblue)
    writePPM(red,green,blue, width, height, "circles")

    
if __name__ == "__main__":
    input=open("input")
    cuadro_inicial()
    n_circulos=int(input.readline())
    width = 1024
    height = 960
    for i in range(n_circulos):
        circulo=[]
        #circulo=[ejex,ejey,radio,red,green,blue]
        linea=input.readline()
        elemento=""
        circulo=linea[:len(linea)-1].split(" ")
        #print(circulo)
        draw_circle(circulo)  
    input.close()


