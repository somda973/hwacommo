import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

Es = 0.0001   # 기존 0.5. 가위치법이 참 근(15.923)에 도달하도록 더 narrow하게 설정.
x_r0=0 # 임의로 설정
x_l=0
x_l1=x_l
x_u=20
x_u1=x_u
i = 0
fx_l=(4+x_l)/((42-2*x_l)**2)/(28-x_l)-0.016
fx_u=(4+x_u)/((42-2*x_u)**2)/(28-x_u)-0.016
x_r=(x_l*fx_u-x_u*fx_l)/(fx_u-fx_l)
Ea = (x_r-x_r0)/x_r * 100
while Ea >= Es :
    x_r=(x_l*fx_u-x_u*fx_l)/(fx_u-fx_l)
    fx_r=(4+x_r)/((42-2*x_r)**2)/(28-x_r)-0.016
    #print("f(x_r)=",fx_r)
    if fx_r < 0: # fx_r < 0 일 때
        x_l = x_r
        #print ("x_r이 x_l이 되었습니다.",x_l)
        fx_l=(4+x_l)/((42-2*x_l)**2)/(28-x_l)-0.016
    else:
        x_u = x_r
        #print ("x_r이 x_u가 되었습니다.",x_u)
        fx_u=(4+x_u)/((42-2*x_u)**2)/(28-x_u)-0.016
    Ea = (x_r-x_r0)/x_r * 100
    i = i+1
    #print("Ea =",Ea, ", i=",i)
    Et = abs(x_r-15.923)/x_r*100
    x_r0=x_r
    #print("---")
print("False-Position")
print("Initial Approximation x_l:",x_l1)
print("Initial Approximation x_u:", x_u1)
print("Es:", Es)
print("Iteration:", i)
print("The root of the equation is:", x_r)
print("Ea:", Ea,"%")
