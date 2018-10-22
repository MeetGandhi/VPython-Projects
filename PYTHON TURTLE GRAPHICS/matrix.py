import turtle
r=input("enter number of rows:")
c=input("enter number of columns:")
di=input("enter distance between dots in pixels:")
d=turtle.Turtle()
d.penup()
for j in range(r):
    for i in range(c):
        d.dot()
        d.forward(di)
    d.backward(di*c)
    d.right(90)
    d.forward(di)
    d.left(90)
turtle.done()
