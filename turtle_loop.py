import turtle
dizzy = turtle.Turtle()
dizzy.color("cyan")
angles = [-90, 0, 0, -90,
          135, 0, 0, 0,
          90, 0, 0, 0,
          135, -90, 0, 0,
          90, 0, 0, 0]
for angle in angles:
    dizzy.forward(25)
    dizzy.right(angles)
