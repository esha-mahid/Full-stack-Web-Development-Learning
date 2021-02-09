import turtle

rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

stars = turtle.Turtle()
stars.width(5)
stars.speed(3)
for prettycolor in rainbow:
    stars.color(prettycolor)
    for side in [1,2,3,4,5]:
        stars.forward(50)
        stars.right(144)
    stars.right(60)
    stars.penup()
    stars.forward(50)
    stars.pendown()
