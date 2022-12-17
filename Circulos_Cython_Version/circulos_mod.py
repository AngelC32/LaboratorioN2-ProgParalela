import array 
import math
from draw_processing import draw_canvas,draw_circle


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
    
if __name__ == "__main__":
    input=open("input")
    n_circulos=int(input.readline())

    width = 1024
    height = 960
    cuadro =  draw_canvas(width, height)

    for i in range(n_circulos):
        
        linea=input.readline()
        circulo=linea[:len(linea)-1].split(" ")
        circulo_int=[int(i) for i in circulo]
        draw_circle(array.array("i",circulo_int),cuadro,width,height)

    writePPM(cuadro[0], cuadro[1], cuadro[2], width, height, "salida")
    
    input.close()