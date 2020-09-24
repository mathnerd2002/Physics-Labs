from vpython import *
#GlowScript 3.0 VPython
scene = canvas (background=color.white)

fix_point = sphere ( pos=vec(0,2,0), radius=0.2, color=color.red )  
m =.549
g = -9.796
l_0 = .125        # initial length
l_0_spring = .54     # unstretched spring  
k_spring   = (m * g)/(l_0 - l_0_spring)      # k constant
mu = 0.1            # damping coeff

ball    = sphere ( pos = fix_point.pos + vec(0,-l_0,0),
        mass = m , v = vec(0,0,0), radius=0.1, 
        color=color.blue)  

spring  = helix( pos=fix_point.pos , axis = ball.pos-fix_point.pos, 
        radius=0.1, color=color.orange  )

vg   = graph(title=' Velocity ', xtitle=' t ', ytitle=' v (t) ')
vx_b = gcurve(graph=vg, color=color.cyan) 
vy_b = gcurve(graph=vg, color=color.magenta) 

scene.waitfor('click')

myrate = 2000

ball.p = ball.mass*ball.v

t = 0
dt = 0.001
ball.old_v = ball.v
ball.T = 0

while t < 15 :
    
    rate(myrate)
    
    spring.pos = fix_point.pos
    
    spring.axis = ball.pos-fix_point.pos
    
    l = ball.pos - fix_point.pos
    
    spring.s = mag(l)- l_0_spring
    
    F_s = -k_spring * spring.s * l.hat   # spring force
    
    F_g = m*vec(0,g,0)    # gravitational force
    
    F = F_g + F_s 
    
    ball.p = ball.p + F*dt
    
    ball.v = ball.p/ball.mass
    ball.pos = ball.pos + ball.v * dt
    
    spring.axis = ball.pos - fix_point.pos 
    
    vx_b.plot(pos=(t,ball.v.x))
    vy_b.plot(pos=(t,ball.v.y))

    t = t + dt
       
    if ball.old_v.y > 0 and ball.v.y < 0 :
        print (" period ", ball.T,  2*pi*sqrt(m/k_spring))
        ball.T = 0

    ball.old_v = ball.v
    ball.T = ball.T + dt


scene.waitfor('click')