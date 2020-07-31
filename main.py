from scipy.integrate import ode
import numpy as np
from odeFunctions import odeFunctions
import matplotlib.pyplot as plt

# Initial Condition
v0 = 0
w0 = 0
x0 = 0
y0 = 0
tetha0 = 0
init = [v0, w0, x0, y0, tetha0]
tm = 500

# main function
fun = odeFunctions()

# ode solver
ODE = ode(fun.f)
ODE.set_integrator('dop853', max_step=0.1)
ODE.set_solout(fun.fout)
ODE.set_initial_value(init, t=0.)
result = ODE.integrate(tm)


tt = np.array(fun.ts)
yy = np.array(fun.ys)


plt.figure(figsize=(10, 7))
plt.plot(tt, yy[:,0])
plt.title('speed (V), m/s')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 7))
plt.plot(tt, yy[:,1])
plt.title('Angular velocity (w), rad/s')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 7))
plt.plot(tt, yy[:,2])
plt.title('position X, m')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 7))
plt.plot(tt, yy[:,3])
plt.title('position Y, m')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 7))
plt.plot(tt, yy[:,4])
plt.title('angle tetha, rad')
plt.grid(True)
plt.show()






