# Program to calculate the area or vol of a shape chosen by user
import Area, Vol

f = True

def choose_action():
    print("Pls choose an action ")
    print()
    print("1.Area")
    print("2.Volume")
    print("3.Exit")
    print()


def choose_shape():  # Function to print the choices
    print("Pls choose a shape: ")
    print()
    print("1.Cube")
    print("2.Cuboid")
    print("3.Cylinder")
    print("4.Sphere")
    print("5.Cone")
    print()


# Main loop
while f:
    choose_action()
    try:
        x = int(input("Make a choice (1,2,3): "))

        if x not in [1, 2, 3]:
            print("Please check your input")

        elif x == 3:
            f = False

        else:
            choose_shape()
            y = int(input("Enter shape: "))

            if y not in [1, 2, 3, 4, 5]:
                print("Please check your input")

            elif y == 1:
                s = float(input("Enter side of cube: "))

                if x == 1:
                    print(Area.tsa_cube(s))
                else:
                    print(Vol.vol_cube(s))

            elif y == 2:
                l = float(input("Enter length: "))
                b = float(input("Enter breadth: "))
                h = float(input("Enter height: "))

                if x == 1:
                    print(Area.tsa_cuboid(l, b, h))
                else:
                    print(Vol.vol_cuboid(l, b, h))

            elif y == 3:
                r = float(input("Radius of cylinder: "))
                h = float(input("Height of cylinder: "))

                if x == 1:
                    print(Area.tsa_cylinder(r, h))
                else:
                    print(Vol.vol_cylinder(r, h))

            elif y == 4:
                r = float(input("Radius of sphere: "))

                if x == 1:
                    print(Area.tsa_sphere(r))
                else:
                    print(Vol.vol_sphere(r))

            elif y == 5:
                r = float(input("Radius of cone: "))

                if x == 1:
                    s = float(input("Slant height of cone: "))
                    print(Area.tsa_cone(r, s))
                else:
                    h = float(input("Height of cone: "))
                    print(Vol.vol_cone(r, h))
                    
    except ValueError:
        print("Pls enter a number")

