from cpython cimport array, bool

def in_circle( int Cent_x,  int Cent_y , int coord_x,  int coord_y,  int radio):
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


def test():
    print("Module")


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


