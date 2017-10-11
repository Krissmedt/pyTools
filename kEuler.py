#### Kris' Euler Methods####
import numpy as np
    
def eulerForward(tsteps, tend, y0, F):
    dt = (tend)/(tsteps)
    yfe =  np.zeros(tsteps+1,dtype=np.float)
    yfe[0] = y0
    for ti in range(0,tsteps):
        t = ti*dt
        yfe[ti+1] = yfe[ti] + dt*F(t,yfe[ti])

    return yfe

"""
def eulerBackward(self,tsteps, tend, y0, F):
    dt = (tend)/(tsteps)
    yfe =  np.zeros(tsteps+1,dtype=np.float)
    yfe[0] = y0
    for ti in range(0,tsteps):
        t = ti*dt
        yfe[ti+1] = yfe[ti] + dt*F(t,yfe[ti])

    return yfe
"""
