l=input("Enter Length:")
s=input("Enter number of sides of polygon:")
n=input("Enter number of such polygons interconnected:")
import turtle
t=turtle.Turtle()
for j in range(n):
    for i in range(s):
        t.forward(l)
        t.left(360/s)
    t.forward(l)
    t.left(360/n)
turtle.done()
