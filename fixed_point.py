import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# x = g(x) 형태로 변형: (42-2x)^2 = (4+x)/(0.016*(28-x))
#   -> 42-2x = sqrt((4+x)/(0.016*(28-x)))  (근 부근에서 42-2x > 0)
#   -> x = 21 - 0.5*sqrt((4+x)/(0.016*(28-x)))
x_r=18
x_r1 = x_r
i=0
Ea = 100
Es = 0.0001   # 참 근(15.923)으로 수렴하도록 설정.
x_r0=0
while Ea >= Es :
    i = i+1
    x_r = 21 - 0.5*((4+x_r)/(0.016*(28-x_r)))**0.5
    #print("x_r =",x_r)
    Ea = abs((x_r-x_r0)/x_r*100)
    x_r0 = x_r
    #print("i =",i, "x_r =", x_r,"Ea =", Ea)
print("Fixed-Point Iteration")
print("Initial Approximation x:", x_r1)
print("Es:", Es)
print("Iteration:", i)
print("The root of the equation is:", x_r)
print("Ea:", Ea,"%")
