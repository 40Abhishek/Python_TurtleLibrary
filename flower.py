import turtle
t=turtle.Turtle()
t.color('orange','red')
t.begin_fill()
t.speed(0)
t.back(500)
for i in range(1000):
    t.forward(700)
    t.left(179)
t.end_fill()
turtle.done()
