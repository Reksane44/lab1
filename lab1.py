import math
x = float(input("x="))
eps = 0.01
z = 1
p = 0
i = 1
z1 = 1
while math.fabs(z)>eps:
    z1 = i*z1
    z = (-1**(i+1))*math.sin(x**i)/z1
    p=p+z
    i=i+1

print(p)
