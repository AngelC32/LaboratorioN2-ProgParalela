from cpython cimport array, bool

def in_circle( int Cent_x,  int Cent_y , int coord_x,  int coord_y,  int radio):
    cdef  int x = Cent_x
    cdef  int y = Cent_y
    cdef  int Cx = coord_x
    cdef  int Cy = coord_y
    cdef  int r = radio
    cdef  bool result =  ((Cx-x)**2 + (Cy-y)**2) <= (r**2)
    return result


def test():
    print("Module")


def draw_canvas( unsigned int width, unsigned int height ):
    cdef unsigned int i
    cdef unsigned int w = width
    cdef unsigned int h = height
    cdef unsigned int size = w*h

    cdef  array.array red = array.array('i', [])
    cdef  array.array green = array.array('i', [])
    cdef  array.array blue = array.array('i', [])

    for i in range(size):
        red.append(0)
        green.append(0)
        blue.append(0)
    
    return [red, green, blue]


