#### Kris' Runge-Kutta Methods####
import numpy as np
from math import sin, cos

def rk4(tsteps, tend, y0, F):
    dt = (tend)/(tsteps)
    yrk4 =  np.zeros(tsteps+1,dtype=np.float)
    yrk4[0] = y0
    for ti in range(0,tsteps):
        t = ti*dt
        y1 = yrk4[ti]
        y2 = yrk4[ti] + dt/2 * F(t,y1)
        y3 = yrk4[ti] + dt/2 * F(t+dt/2,y2)
        y4 =  yrk4[ti] + dt * F(t+dt/2,y3)
        yrk4[ti+1] = yrk4[ti] + dt/6 * (
                                        F(t,y1)
                                        + 2*F(t+dt/2,y2)
                                        + 2*F(t+dt/2,y3)
                                        + F(t+dt,y4))
    return yrk4