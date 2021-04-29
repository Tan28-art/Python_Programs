import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(15)
def square(length,angle):
    for i in range(8):
        bob.forward(length)
        bob.right(angle)

for i in range(100):
    square(120, 100)
    bob.right(11)

