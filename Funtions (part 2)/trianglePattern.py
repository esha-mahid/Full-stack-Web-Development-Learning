import turtle


def tri_pattern(prettycolor, start):
    t = turtle.Turtle()
    t.width(3)
    t.color(prettycolor)
    t.right(start)
    t.speed(0)
    for shape in range(6):
        for side in range(3):
            t.forward(100)
            t.right(120)
        t.right(15)
    t.hideturtle()

tri_pattern("red", 0)
tri_pattern("yellow", 120)
tri_pattern("blue", 240)
