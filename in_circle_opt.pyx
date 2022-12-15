from cpython cimport array
from cython cimport boundscheck

@boundscheck(False)
def draw_circle(array.array circulo,array.array red_canal,array.array green_canal,array.array blue_canal, int width, int height):
#def draw_circle(array.array circulo, cuadro, int width, int height):
    #cdef int[:] circulo_convert=circulo
    #circulo=[ejex,ejey,radio,red,green,blue]
    cdef int eje_Y=circulo.data.as_ints[0]
    cdef int eje_X=circulo.data.as_ints[1]
    cdef int radio=circulo.data.as_ints[2]
    cdef int color_red=circulo.data.as_ints[3]
    cdef int color_green=circulo.data.as_ints[4]
    cdef int color_blue=circulo.data.as_ints[5]
    cdef int i,j
    cdef int h=height
    cdef int w=width
    cdef int index
    for i in range(h):
        for j in range(h):
            if(in_circle(eje_X,eje_Y,i,j,radio)):
                index = j+i*width
                red_canal.data.as_ints[index]=comprobar_pixel(red_canal.data.as_ints[index],color_red)
                green_canal.data.as_ints[index]=comprobar_pixel(green_canal.data.as_ints[index],color_green)
                blue_canal.data.as_ints[index]=comprobar_pixel(blue_canal.data.as_ints[index],color_blue)
    
    return red_canal,green_canal,blue_canal
cdef int comprobar_pixel(int oldPixel,int newPixel):
    return oldPixel ^ newPixel


cdef int in_circle( int Cent_x,  int Cent_y , int coord_x,  int coord_y,  int radio):
    cdef  int x = Cent_x
    cdef  int y = Cent_y
    cdef  int Cx = coord_x
    cdef  int Cy = coord_y
    cdef  int r = radio
   # cdef  bool result =  ((Cx-x)**2 + (Cy-y)**2) <= (r**2)
    #return result
    if ((Cx-x)**2 + (Cy-y)**2) <= (r**2):
        return 1
    return 0


#def test():
 #   print("Module")


def draw_canvas( unsigned int width, unsigned int height ):
    cdef unsigned int i
    cdef unsigned int w = width
    cdef unsigned int h = height
    cdef unsigned int size = w*h
    
    cdef  array.array template_array = array.array('i', [])
    cdef array.array red
    cdef  array.array green
    cdef  array.array blue
    red= array.clone(template_array, size, zero=False)
    green= array.clone(template_array, size, zero=False)
    blue= array.clone(template_array, size, zero=False)
    
    for i in range(size):
       red.data.as_ints[i]=0
       green.data.as_ints[i]=0
       blue.data.as_ints[i]=0
    
    return [red, green, blue]


