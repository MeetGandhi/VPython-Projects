from visual import *
ball=sphere(pos=(-1,0,0),color=color.yellow,radius=0.5)
wall_right=box(pos=(6,0,0),size=(0.2,12,12),color=color.blue)
wall_left=box(pos=(-6,0,0),size=(0.2,12,12),color=color.blue)
wall_top=box(pos=(0,6,0),size=(12,0.2,12),color=color.red)
wall_bottom=box(pos=(0,-6,0),size=(12,0.2,12),color=color.red)
wall_deep=box(pos=(0,0,-6),size=(12,12,0.2),color=color.black)
print("""
Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.
""")

ball.velocity=vector(15, -23, 27)
deltat=0.005
t=0
vscale=0.1
varr=arrow(pos=ball.pos,axis=vscale*ball.velocity,color=color.yellow)
scene.autoscale=True
ball.trail=curve(color=ball.color)
while t<100:
    rate(100)
    if abs(ball.pos.x)>abs(wall_right.pos.x):
        ball.velocity.x=-ball.velocity.x
    ball.pos=ball.pos+ball.velocity*deltat
    t=t+deltat
    ball.trail.append(pos=ball.pos)
    if abs(ball.pos.z)>6:
        ball.velocity.z=-ball.velocity.z
    if abs(ball.pos.y)>abs(wall_top.pos.y):
        ball.velocity.y=-ball.velocity.y
