import turtle as t
t.speed(0)
t.bgcolor('black')
t.color('red')
t.penup()
t.back(70)
t.right(90)
t.forward(345)
t.left(90)
t.left(90)
t.pendown()
x=24
c=8.5
b=60
for j in range(3):
    for i in range(x):
        t.forward(c)
        t.right(8)
    t.penup()
    t.left(90)
    t.forward(b)
    t.left(90)
    t.pendown()
    x+=2
    c+=8.5
    b-=(10)
    for i in range(x):
       t.forward(c)
       t.left(8)
    t.penup()
    t.right(90)
    t.forward(b)
    t.right(90)
    t.pendown()
    x+=2
    c+=8.5
    b-=(10)
'''for i in range(38):
   t.forward(28.5)
   t.right(8)
   '''
t.done()
