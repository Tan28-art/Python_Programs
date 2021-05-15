'''Module with area functions'''

'''constant'''
pi = 3.14

def tsa_cube(s):
    '''Finds total surface area of cube'''
    return 6*(s**2)

def tsa_cuboid(l,b,h):
    '''Finds total surface area of cuboid'''
    return 2*((1*b)+(b*h)+(l*h))

def tsa_cylinder(r,h):
    '''Finds total surface area of cylinder'''
    return 2*pi*r*(r+h)

def tsa_sphere(r):
    '''Finds total surface area of sphere'''
    return 4*pi*(r**2)

def tsa_cone(r,s):
    '''Finds total surface area of cone'''
    return pi*r*(r+s)