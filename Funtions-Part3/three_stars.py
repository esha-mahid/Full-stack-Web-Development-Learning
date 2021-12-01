import turtle

def star(color, sides, length, angle, distance):
    galileo = turtle.Turtle()
    galileo.color(color)  # colorful!
    galileo.width(1)  # visible!
    galileo.speed(2)  # fast!
    galileo.penup()
    galileo.left(angle)  # away from center
    galileo.forward(distance)
    galileo.pendown()  # start drawing
    for side in range(sides):
        galileo.forward(length)
        galileo.left(720 / sides)
    galileo.hideturtle()  # just the star
#star("yellow", 5, 50, 0, 0)   #outside the loop draws a single star
#star("blue", 7, 50, 45, 100)

for angle in [180, 135, 90, 45, 0]:
    star("red", 5, 50, angle, 100)
for angle in [180, 135, 90, 45, 0]:
    star("purple", 5, 30, angle, 60)
