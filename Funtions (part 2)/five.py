import turtle
t = turtle.Turtle()
t.color("red")

for side in range(20):
    t.forward(side) #    Change t.forward(side) to t.forward(side * 10) to create a large spiral
    t.right(45)


#to draw a spiral triangle
#import turtle
#t = turtle.Turtle()
#t.color("cyan")

#for side in range(19):
#    t.forward(side*10)
#    t.right(120)
