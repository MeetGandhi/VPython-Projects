import turtle
n=input("enter number of sides of polygon:")
l=input("enter length of each side:")
a=360.0/n
p=turtle.Turtle()
for i in range(n):
    p.forward(l)
    p.right(a)
turtle.done()
