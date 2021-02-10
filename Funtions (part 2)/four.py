
import turtle

# Set the number of sides here.
sides = 5

# Set the length of a side here.
length = 100

t = turtle.Turtle()
t.color("orange")
for side in range(sides):
    t.forward(length)
    t.right(360 / sides)
#The important part is the last line: dividing 360 by sides will give the correct turning angle for any number of sides. For instance, 360 / 8 equals 45, which is the correct turning-angle to draw an eight-sided figure (an octagon). You can test this by changing the sides variable to 8 or any other positive number! (Keep in mind that if the number of sides is very large, the shape will just end up looking like a circle.)
