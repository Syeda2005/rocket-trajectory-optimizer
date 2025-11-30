from scipy.optimize import minimize
from rocket_dynamics import rocket_dynamics
from scipy.integrate import solve_ivp
import numpy as np

def simulate(pitch):
    y0 = [0, 0, 2000]
    sol = solve_ivp(rocket_dynamics, [0, 200], y0, args=(pitch,), max_step=0.1)
    h_final = sol.y[0, -1]
    return -h_final

def optimize_pitch():
    result = minimize(lambda p: simulate(p[0]), x0=[0.2])
    return result.x[0]
