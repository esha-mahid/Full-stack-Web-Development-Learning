import turtle

def spiral():
    t = turtle.Turtle()
    t.color("cyan")
    for n in range(50):
        t.forward(n)
        t.right(20)
spiral()
spiral()
