from vpython import *
#GlowScript 3.0 VPython
scene = canvas(background=color.white)

fix_point = sphere(pos=vec(0,2,0), radius=0.2, color=color.red)  

l_0 = .54             # initial length
l_0_spring = .125     # unstretched spring  
k_spring = 12.9590457831      # k constant
m =  0.549
g = 9.79609
mu = 0.1            # damping coeff

ball    = sphere(pos = fix_point.pos+vec(0,-l_0,0),
        mass = m,v = vec(0,0,0), radius=0.1, 
        color=color.blue)  

spring  = helix(pos=fix_point.pos,axis = ball.pos-fix_point.pos, 
        radius=0.1, color=color.orange)

vg   = graph(title='Velocity', xtitle='t', ytitle='v (t)')
vx_b = gcurve(graph=vg,color=color.cyan) # a graphics curve
vy_b = gcurve(graph=vg,color=color.magenta) # a graphics curve

scene.waitfor('click')

myrate = 2000

ball.p = ball.mass*ball.v

t = 0
dt = 0.001
ball.old_v = ball.v
ball.T = 0

while t < 10 :
    
    rate(myrate)
    
    spring.pos = fix_point.pos
    
    spring.axis = ball.pos - fix_point.pos
    
    l = ball.pos - fix_point.pos
    
    spring.s = mag(l) - l_0_spring
    
    F_s = -k_spring * spring.s * l.hat  # spring force
    
    F_g = m * vec(0, -g, 0)      # gravitational force
    
    #F_d = - mu * ball.v.mag2 * ball.v.hat # quadratic drag
    #F_d = - mu * ball.v.mag * ball.v.hat   # linear drag
    
    F = F_g + F_s 
    
    ball.p = ball.p + F*dt
    
    ball.v = ball.p/ball.mass
    ball.pos = ball.pos + ball.v*dt
    
    spring.axis = ball.pos - fix_point.pos 
    
    vx_b.plot(pos=(t,ball.v.x))
    vy_b.plot(pos=(t,ball.v.y))

    t = t + dt

    if ball.old_v.y > 0 and ball.v.y < 0 :
        print ("period", ball.T,  2 * pi * sqrt(ball.mass/k_spring))
        ball.T = 0

    ball.old_v = ball.v
    ball.T = ball.T+dt

scene.waitfor('click')

