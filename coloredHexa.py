import turtle
hexa = turtle.Turtle()

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

hexa.width(5)
hexa.penup()
hexa.back(100)
hexa.pendown()
for prettycolor in rainbow:
    hexa.color(prettycolor)
    hexa.forward(100)
    hexa.right(60)
hexa.hideturle()
