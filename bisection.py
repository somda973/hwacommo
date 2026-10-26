import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x_l=0
x_l1=0
x_u=20
x_u1=20
x_r0=0
x_r=(x_l+x_u)/2
Ea = (x_r-x_r0)/x_r * 100
Es = 0.0001   # 기존 0.5. 세 방법의 근을 일치시키기 위해 더 엄격하게 설정.
i=0
while abs(Ea) >= Es :
    x_r=(x_l+x_u)/2
    fx_r=(4+x_r)/((42-2*x_r)**2)/(28-x_r)-0.016
    #print("f(x_r) =",fx_r)
    if fx_r < 0: # fx_r < 0 일 때
        x_l = x_r
        #print ("x_r이 x_l이 되었습니다.",x_l)
    else:
        x_u = x_r
        #print ("x_r이 x_u가 되었습니다.",x_u)
    i=i+1
    Ea = (x_r-x_r0)/x_r * 100
    x_r0=x_r
    #print("i is", i,"," , "Ea is",Ea)
    #print("---")
print("Bisection")
print("Initial Approximation x_l:",x_l1)
print("Initial Approximation x_u:", x_u1)
print("Es:", Es)
print("Iteration:", i)
print("The root of the equation is:", x_r)
print("Ea:", Ea)
