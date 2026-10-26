import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

x_r=18
x_r0 = x_r
x_r1 = x_r
i=0
Ea = 100
Es = 0.0001   # 발표 원본은 0.5. 세 방법의 근을 일치시키기 위해 더 엄격하게 설정.
x_r0=0
while Ea >= Es :
    i = i+1
    fx_r=(4+x_r)/((42-2*x_r)**2)/(28-x_r)-0.016
    dfx_r= -(-448 - 8*x_r + x_r**2)/(2 * ((21 - x_r)**3)*(-28 + x_r)**2)
    x_r = x_r-fx_r/dfx_r
    #print("x_r =",x_r)
    Ea = abs((x_r-x_r0)/x_r*100)
    x_r0 = x_r
    #print("i =",i, "x_r =", x_r,"Ea =", Ea)
print("Newton-Raphson")
print("Initial Approximation x:", x_r1)
print("Es:", Es)
print("Iteration:", i)
print("The root of the equation is:", x_r)
print("Ea:", Ea,"%")
