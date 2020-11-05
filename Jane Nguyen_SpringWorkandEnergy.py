from vpython import *
#GlowScript 3.0 VPython
  
scene = canvas(background=color.white)

fix_point = sphere ( pos=vec(0,6,0), radius=0.5, color=color.red )  

l_0 = 17.5                # intial lenght
alpha = 90 * pi/180     # intitial angle
l_0_spring = 1.5*l_0    # unstretched spring 
k_spring   = 9.769         # k constant
g = 10                  # gravity
mu = 0.01               # damping coeff

ball    = sphere ( 
        pos= fix_point.pos + vec(l_0*sin(alpha),-l_0*cos(alpha),0),
        mass = 0.5 , v = vec(0,0,0), radius=0.1, 
        color=color.blue,make_trail=True,trail_radius=0.01) 

spring  = helix( pos=fix_point.pos , axis = ball.pos-fix_point.pos,  
        radius=0.2, color=color.orange  )

ball.p = ball.mass*ball.v

vg   = graph(title=' Velocity ', xtitle=' t ', ytitle=' v (t) ')
vx_b = gcurve(graph=vg, color=color.cyan) # a graphics curve
vy_b = gcurve(graph=vg, color=color.magenta) # a graphics curve

work_g  = graph(title=' Work ', xtitle=' t ', ytitle=' v (t) ')
w_g     = gdots(graph=work_g, color=color.cyan, size = 2) 
e_g     = gcurve(graph=work_g, color=color.green  )
w_s     = gdots(graph=work_g, color=color.magenta, size = 2) 
e_s     = gcurve(graph=work_g, color=color.blue  )

l = ball.pos - fix_point.pos    
spring.s = mag(l)- l_0_spring
spring_e_0 = 1/2 * k_spring * spring.s**2
work_s = 0

grav_e_0 = ball.mass * g * ball.pos.y
work_g = 0

energy_g   = graph(title=' Energy ', xtitle=' t ', ytitle=' E (t) ')
kin_e_g    = gcurve(graph=energy_g, color=color.red)  
grav_e_g   = gcurve(graph=energy_g, color=color.green)  
spring_e_g = gcurve(graph=energy_g, color=color.purple)  
total_e_g  = gcurve(graph=energy_g, color=color.blue)  

myrate = 1600

t = 0
dt = 0.0005

while t < 10 :
    
    rate(myrate)
    
    #fix_point.pos.y = l_0 + sin(7*t)
    
    spring.pos = fix_point.pos
    
    spring.axis = ball.pos-fix_point.pos
    
    l = ball.pos - fix_point.pos
    
    spring.s = mag(l)- l_0_spring
    #print( spring.s) 
    
    F_s = - k_spring * spring.s * l.hat    # spring force
    
    F_g = ball.mass*vec(0,-g,0)         # gravitational force
    
    #F_d = - mu * ball.v.mag2 * ball.v.hat   # quadratic drag
    F_d = - mu * ball.v.mag * ball.v.hat    # linear drag
    
    F = F_g + F_s #+ F_d
    
    ball.p = ball.p + F*dt
    
    ball.v = ball.p/ball.mass
    ball.pos = ball.pos + ball.v * dt
    
    work_g = work_g + F_g.dot(ball.v) * dt
    work_s = work_s + F_s.dot(ball.v) * dt
    
    spring.axis = ball.pos - fix_point.pos 
    
    vx_b.plot(pos=(t,ball.v.x))
    vy_b.plot(pos=(t,ball.v.y))
    
    grav_e = ball.mass * g * ball.pos.y
    spring_e = 1/2 * k_spring * spring.s**2
    kin_e = 1/2 * ball.mass * ball.v.mag2
    total_e = kin_e + grav_e + spring_e
   
   
    w_g.plot(pos=(t, work_g))    
    e_g.plot(pos=(t,grav_e - grav_e_0))
    
    w_s.plot(pos=(t, work_s))    
    e_s.plot(pos=(t,spring_e - spring_e_0))


    grav_e_g.plot(pos=(t,grav_e))
    spring_e_g.plot(pos=(t,spring_e))
    kin_e_g.plot(pos=(t,kin_e))
    total_e_g.plot(pos=(t,total_e))

    t = t+dt
    
