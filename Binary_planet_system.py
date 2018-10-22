from visual import *
print("""
Right button drag or Ctrl-drag to rotate "camera" to view scene.
Middle button or Alt-drag to drag up or down to zoom in or out.
  On a two-button mouse, middle is left + right.
""")


star=sphere(pos=(-1e11,0,0),radius=2e10,color=color.yellow,make_trail=True,mass=2e30)
planet=sphere(pos=(1e11,0,0),radius=1e10,material=materials.BlueMarble,make_trail=True,mass=1e30)
star.p=vector(0,0,-1e4)*star.mass
planet.p=-star.p
dt=1e5
while True:
    rate(100)
    d=planet.pos-star.pos
    f=((6.7e-11)*star.mass*planet.mass*d)/mag(d)**3
    star.p+=f*dt
    planet.p-=f*dt
    for x in [star,planet]:
        x.pos=x.pos+((x.p/x.mass)*dt)
