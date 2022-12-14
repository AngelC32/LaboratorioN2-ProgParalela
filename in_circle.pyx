def in_circle( int Cent_x,  int Cent_y , int coord_x,  int coord_y,  int radio):
    cdef  int x = Cent_x
    cdef  int y = Cent_y
    cdef  int Cx = coord_x
    cdef  int Cy = coord_y
    cdef  int r = radio
    return ((Cx-x)**2 + (Cy-y)**2) <= (r**2)

def test():
    print("Module")