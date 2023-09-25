import turtle as t
t.bgcolor('cyan')
t.color('red','black')
t.begin_fill()
'''t.back(300)
t.left(90)
t.forward(300)'''
for i in range(4):
    t.forward(100)
    t.left(90)
t.penup()
t.right(90)
t.forward(50)
t.pendown()
for j in range(4):
    t.forward(100)
    t.left(90)
t.setheading(90)
t.forward(150)
t.end_fill()
t.done()
print('end')
