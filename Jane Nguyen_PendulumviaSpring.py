from vpython import *
#GlowScript 3.0 VPython

scene = canvas(background=color.white)

fix_point = sphere (pos=vec(0,6,0), radius=0.5, color=color.red)  

l_0 = 1.75               # intial lenght
alpha = 10 * pi/180     # intitial angle
l_0_spring = l_0        # unstretched spring 
k_spring   = 1e4     # k constant
g = 9.79609                 # gravity
mu = 0.1                # damping coeff

ball    = sphere(pos= fix_point.pos + vec(l_0*sin(alpha),-l_0*cos(alpha),0),
        mass = .550 , v = vec(0,0,0), radius=0.1, 
        color=color.blue)  

spring  = helix(pos=fix_point.pos , axis = ball.pos-fix_point.pos,  
        radius=0.2, color=color.orange)

ball.p = ball.mass*ball.v

vg = graph(title=' Velocity ', xtitle=' t ', ytitle=' v (t) ')
vx_b = gcurve(graph=vg, color=color.cyan) # a graphics curve
vy_b = gcurve(graph=vg, color=color.magenta) # a graphics curve

myrate = 200

t = 0
dt = 0.01

ball.old_v = ball.v
ball.T = 0

while t < 40:
    
    rate(myrate)
    
    #fix_point.pos.y = 5 + cos(7*t)
    
    spring.pos = fix_point.pos
    
    spring.axis = ball.pos-fix_point.pos
    
    l = ball.pos - fix_point.pos
    
    spring.s = mag(l)- l_0_spring
    #print(spring.s) 
    
    F_s = -k_spring*spring.s*l.hat  # spring force
    
    F_g = ball.mass*vec(0,-g,0)   # gravitational force
    
    #F_d = - mu * ball.v.mag2 * ball.v.hat # quadratic drag
    F_d = - mu * ball.v.mag * ball.v.hat    # linear drag
    F = F_g + F_s 
    
    ball.p = ball.p + F*dt
    
    ball.v = ball.p/ball.mass
    ball.pos = ball.pos + ball.v * dt
    
    spring.axis = ball.pos - fix_point.pos 
    
    vx_b.plot(pos=(t,ball.v.x))
    vy_b.plot(pos=(t,ball.v.y))

    t = t + dt
    
    if ball.old_v.x > 0 and ball.v.x < 0 :
        print(ball.T, 2*pi*sqrt(l_0/g))
        ball.T = 0
            
    ball.old_v = ball.v
    ball.T = ball.T + dt


    