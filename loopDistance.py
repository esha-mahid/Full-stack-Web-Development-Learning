import turtle
willow = turtle.Turtle()
for x in [1, 2, 3]:
    willow.forward(1)  #3 pixels
    for y in [4, 5, 6, 7]:
        willow.forward(1) #12 pixels
    willow.forward(1) #3 pixels

#it covers a total distance of 18 pixels
