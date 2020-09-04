GlowScript 3.0 VPython
 # vectors

 # definition of vectors
 
a=vec(4,3,2)
b=vec(4**2,3**2,2**2)
c=vec(sqrt(4.6),3.14**3,3.14**(1/2))
print('a,b,c:',a,b,c)
 
 # linearity of vectors
 
alpha=2.5
beta=3.2
 
c=alpha*a+beta*b
d=alpha*a-beta*b
print('c:',c,'d:',d)
 
 # refer to components
 
a1=vec(4.6,-3.2,2.9)
b1=vec(-5.4,4.6,3.1)
 
print('a1:', a1, 'b1:', b1)
print('components:', a1.x, a1.y, a1.z, b1.x, b1.y, b1.z)
 
 # magnitude & magnitude^2
 
print ('magnitude:',mag(a1),a1.mag,sqrt(a1.x**2+a1.y**2+a1.z**2))
print('magnitude^2:',mag2(a),a.mag2,(a.x**2+a.y**2+a.z**2))
 
 #norm of vectors
 
print('a:',a)
print('norm:', norm(a), a.norm(), a/mag(a))
print(mag(norm(a)))
print('unit vector:', hat(a), a.hat, a/mag(a), mag(a.hat))
 
 #dot and crosss products
 
a=vec(2.5,-2,5)
b=vec(-3,2,1.2)
 
print('a&b:',a,b)
print('a*b:', dot(a,b), a.dot(b))
print('b*a:', dot(b,a), b.dot(a))
print('axb:', cross(a,b), a.cross(b))
print('bxa:', cross(b,a), b.cross(a))
 
 #check the orthogonality
 
c=a.cross(b)
print('c=axb:',c, dot(a,c),dot(b,c))
print('angle a-b:', diff_angle(a,b), a.diff_angle(b))
print('angle a-c:', diff_angle(a,c), a.diff_angle(c), pi/2)
print('angle b-c:', diff_angle(b,c), b.diff_angle(c), pi/2)
 
 #projection of a along b
 
print('projection:', proj(a,b), a.dot(b.hat)*(b.hat))
 
 #rotation
 
v2=rotate(a, angle=pi, axis=vec(0,0,1))
 
print('a rotated by pi around z:', a, v2)
 
 # angle between vectors
 
print ('a,b,c:', a,b,c)
print('angle(a,b):',a.diff_angle(b))
print('angle(b,a):', b.diff_angle(a))
print('angle(a,c):', a.diff_angle(c))
print('angle(b,c):', b.diff_angle(b,c))
     
 
