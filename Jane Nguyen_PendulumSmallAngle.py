from vpython import *
#GlowScript 3.0 VPython

scene = canvas(background=color.white)

fixed_point = sphere (pos=vec(0,6,0), radius=0.5, color=color.red)

l_0 = 1.75
theta_0 = 10*pi/180 
omega_0 = 0
g = 9.79609

ball = sphere(pos= fixed_point.pos+vec(l_0*sin(theta_0),-l_0*cos(theta_0),0), 
    mass = .550 ,  radius=0.2, color=color.blue )#, make_trail=True ) 

spring = helix(pos= fixed_point.pos, axis = ball.pos -fixed_point.pos,
    radius =0.2, color=color.orange)

ball.omega = omega_0
ball.p = ball.mass*l_0*ball.omega

a_graph = graph(title=' Theta - Omega', xtitle=' t ', ytitle='  ')

theta_plot = gcurve(graph= a_graph, color=color.red)
omega_plot = gcurve(graph= a_graph, color=color.green)

#scene.waitfor('click')

myrate = 2000

ball.theta = theta_0
t = 0
dt = 0.001

ball.omega_old = ball.omega
ball.T = 0

while t  <  40 :
    
    rate(myrate)
    
    spring.pos = fixed_point.pos
    
    spring.axis = ball.pos - fixed_point.pos
    
    F = -ball.mass*g*sin(ball.theta)
    
    ball.p = ball.p + F * dt
    ball.omega = ball.p / (l_0 * ball.mass)
    ball.theta = ball.theta + ball.omega * dt
    
    ball.pos = fixed_point.pos +vec(l_0*sin(ball.theta),-l_0*cos(ball.theta),0)
    
    theta_plot.plot(pos=(t,ball.theta))
    omega_plot.plot(pos=(t,ball.omega))
    
    t = t + dt
            
    if ball.omega_old > 0 and ball.omega < 0 :
        print (ball.T, 2*pi*sqrt(l_0/g))
        ball.T = 0

    ball.omega_old = ball.omega
    ball.T = ball.T + dt



    
