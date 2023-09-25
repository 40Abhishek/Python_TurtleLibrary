import turtle
t=turtle.Turtle()
t.speed(0)
t.color('black')
t.penup()
t.back(300)
t.right(90)
t.forward(330)
t.pendown()
t.left(90)
for e in range(4):
    t.begin_fill()
    for j in range(4):
        for i in range(4):
            t.forward(80)
            t.left(90)
        t.penup()
        t.forward(160)
        t.pendown()
    t.end_fill()

    t.penup()
    t.left(90)
    t.forward(80)
    t.pendown()
    t.begin_fill()
    for q in range(4):
        for w in range(4):
            t.forward(80)
            t.left(90)
        t.left(90)
        t.penup()
        t.forward(160)
        t.right(90)
        t.pendown()
    t.end_fill()
    t.penup()
    t.forward(80)
    t.pendown()
    t.right(90)
for s in range(4):
    t.forward(640)
    t.right(90)
turtle.done()


