'''Module with vol functions'''

'''constant'''
pi = 3.14

def vol_cube(s):
    '''Finds volume of cube''' 
    return s**3

def vol_cuboid(l,b,h):
    '''Finds volume of cuboid'''
    return l*b*h

def vol_cylinder(r,h):
    '''Finds volume of cylinder'''
    pi*(r**2)*h

def vol_sphere(r):
    '''Finds volume of sphere'''
    return (4/3)*pi*(r**3)

def vol_cone(r,h):
    '''Finds volume of cone'''
    return (1/3)*pi*(r**2)*h