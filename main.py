import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from rocket_dynamics import rocket_dynamics
from optimizer import optimize_pitch

m0 = 2000
pitch = optimize_pitch()

y0 = [0, 0, m0]
t_span = [0, 200]

sol = solve_ivp(rocket_dynamics, t_span, y0, args=(pitch,), max_step=0.1)

h, v, m = sol.y

print("Optimal pitch angle (deg):", np.degrees(pitch))

plt.plot(sol.t, h)
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.title("Altitude vs Time")
plt.grid()
plt.savefig("plots/altitude_vs_time.png")
plt.close()

plt.plot(sol.t, v)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time")
plt.grid()
plt.savefig("plots/velocity_vs_time.png")
plt.close()

plt.plot(sol.t, m)
plt.xlabel("Time (s)")
plt.ylabel("Mass (kg)")
plt.title("Mass vs Time")
plt.grid()
plt.savefig("plots/mass_vs_time.png")
plt.close()
