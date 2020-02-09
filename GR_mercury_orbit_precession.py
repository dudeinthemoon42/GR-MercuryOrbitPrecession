from visual import *
from visual.graph import *

scene.title = "Solar System Simulator 5000"
scene.width = 640
scene.height = 480

dt = 0.01;
GM = 1
rlast = 50*GM
r = 50*GM
l = r/sqrt(r/GM - 3)*1
phi = 0
rnext = 2*r - rlast + dt**2*((-GM/r^2) + (l**2/r**3) - 3*((GM*l**2)/r**4))
mercury = sphere(pos = (r*cos(phi),r*sin(phi),0), radius = 5, color=color.red, make_trail=True)
sun = sphere(pos = (0,0,0), radius = 5, color=color.yellow)
g1 = gdisplay(x = 700, y = 0, title='R vs Phi', xtitle = 'Phi', ytitle = 'R',
              width = 640, height = 480)
f = gcurve(color = color.red)

while True:
    rate(9001)
    phi += dt*l / (0.25 * (rnext + r)**2)
    rlast = r
    r = rnext
    rnext = 2*r - rlast + dt**2*((-GM/r**2) + (l**2/r**3) - 3*((GM*l**2)/r**4))

    mercury.pos.x = rnext*cos(phi)
    mercury.pos.y = rnext*sin(phi)

    f.plot(pos = (phi,rnext))
