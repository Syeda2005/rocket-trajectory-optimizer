import numpy as np

g = 9.81
rho = 1.225
Cd = 0.5
A = 0.75

T = 50000
mdot = 5

def rocket_dynamics(t, y, pitch):
    h, v, m = y
    
    thrust = T if m > 1500 else 0
    drag = 0.5 * Cd * A * rho * v**2
    
    dhdt = v
    dvdt = (thrust*np.cos(pitch) - drag)/m - g
    dmdt = -mdot if m > 1500 else 0
    
    return [dhdt, dvdt, dmdt]
