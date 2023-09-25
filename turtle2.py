import turtle as t
t.speed(0)
t.bgcolor('black')
t.color(.9,.1,.6)
t.penup()
t.back(70)
t.right(90)
t.forward(345)
t.left(90)
t.left(90)
t.pendown()
x=48
c=128.5
for j in range(7):
    for i in range(x):
        t.forward(c)
        t.right(8)
    t.penup()
    t.left(90)
    t.forward(60)
    t.left(90)
    t.pendown()
    x-=2
    c-=10
    for i in range(x):
       t.forward(c)
       t.left(8)
    t.penup()
    t.right(90)
    t.forward(60)
    t.right(90)
    t.pendown()
    x-=2
    c-=10
'''for i in range(38):
   t.forward(28.5)
   t.right(8)
   '''
t.done()
