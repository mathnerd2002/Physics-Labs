GlowScript 3.0 VPython
from vpython import *
#GlowScript 3.0 VPython
 
scene = canvas(background=color.white)

ground = box (pos=vec(0,-0.02,0), size= vec(3,0.02,0.4), color=color.green )

v0 = 2.649
g  = 9.8
h  = 0.4
x0 = -1
alpha = 35 * pi/180

ball = sphere ( pos=vec(x0,h,0 ), mass = 0.5 , angle = alpha , radius=0.01, 
    color=color.red, make_trail=True, trail_type="points")

ball.v = v0*vec(cos(ball.angle), sin(ball.angle), 0)
ball.p = ball.mass*ball.v

stone = sphere ( pos=vec(x0,h,0 ), mass = 0.5 , angle = alpha, radius=0.01, 
    color=color.purple, make_trail=True, trail_type="points")

stone2 = sphere ( pos=vec(x0,h,0 ), mass = 0.5 , angle = alpha, radius=0.01, 
    color=color.cyan, make_trail=True, trail_type="points")

stone.v = v0*vec(cos(stone.angle), sin(stone.angle),0)
stone.p = stone.mass*stone.v

v_graph = graph(title='Velocity', xtitle=' t ', ytitle=' v ' )

v_b_x = gcurve(graph= v_graph, color=color.red)
v_b_y = gcurve(graph= v_graph, color=color.green)

v_s_x = gcurve(graph= v_graph, color=color.blue)
v_s_y = gcurve(graph= v_graph, color=color.cyan)

myrate = 200

t = 0
dt = .01

while stone.pos.y > 0 :
    
    rate(myrate)
    
    F_ball = ball.mass*vec(0,-g,0)
    
    ball.p = ball.p+F_ball*dt
    ball.v = ball.p/ball.mass
    ball.pos = ball.pos+ball.v*dt
    
    F_stone = stone.mass*vec(0,-g,0)
    
    stone.p = stone.p+F_stone*dt
    stone.v = stone.p/stone.mass
    stone.pos = stone.pos+stone.v*dt
    
    stone2.pos = vec(x0+v0*cos(alpha)*t, h+ v0*sin(alpha)*t - g/2*t**2, 0)
    
    v_b_x.plot(pos=(t,ball.v.x))
    v_b_y.plot(pos=(t,ball.v.y))

    v_s_x.plot(pos=(t,stone.v.x))
    v_s_y.plot(pos=(t,stone.v.y))

    t = t + dt
     
d = stone.pos.x - x0
print(" distance ", d )
    
    
