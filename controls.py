from visual import *
from visual.controls import *
def set_dir(direction):
    shape.dir=direction
def change_shape_color():
    if c.value:
        shape.color=color.blue
    else:
        shape.color=color.green
def shape_color(value):
    shape.color=value
    if shape.color==color.green:
        c.value=0
    else:
        c.value=1
def setrate(obj):
    shape_rate(obj.value)
def shape_rate(value):
    shape.dtheta=2*value*pi/1e4
w=350
display(x=w,y=0,width=w,height=w,range=1.5,forward=-vector(1,1,1))
shape=ring(color=color.green)

f=controls(x=0,y=0,width=w,height=w,range=60)

b_left=button(pos=(-30,30),height=30,width=50,text="Left",action=lambda:set_dir(-5))
b_right=button(pos=(30,30),height=30,width=50,text="Right",action=lambda:set_dir(1))
c= toggle(pos=(40,-30), width=10, height=10, text0='Green', text1='Blue', action=lambda: change_shape_color())
s2 = slider(pos=(-30,-50), width=7, length=50, axis=(0,1,0), action=lambda: setrate(s2))

s2.value=70
setrate(s2)
set_dir(-1)
while True:
    rate(100)
    shape.rotate(axis=(0,0,1),angle=shape.dir*shape.dtheta)
    
