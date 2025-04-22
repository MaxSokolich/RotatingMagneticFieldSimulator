
import numpy as np
import matplotlib.pyplot as plt

f = 1
omega = 2*np.pi*f

tp = np.linspace(0, 3, 1000)
alpha = np.radians(45)
gamma = np.radians(90)


Brollx =  ((-np.sin(alpha) * np.sin(omega*tp)) + (-np.cos(alpha) * np.cos(gamma)  * np.cos(omega*tp))) 
Brolly =  ((np.cos(alpha) * np.sin(omega*tp)) + (-np.sin(alpha) * np.cos(gamma) *  np.cos(omega*tp))) 
Brollz =  np.sin(gamma) * np.cos(omega*tp)


plt.figure(figsize=(15, 8))
plt.plot(tp, Brollx, label="Bx", color="blue", linewidth=2)
plt.plot(tp, Brolly, label="By", color="red", linewidth=2)
plt.plot(tp, Brollz, label="Bz", color="green", linewidth=2)

# Add labels, title, and legend

plt.title(r"Rotating Magnetic Field Signal at 1Hz, $\alpha = 45^\circ$, $\gamma = 90^\circ$, over 3s", fontsize=16)
plt.xlabel("Time (s)", fontsize=14)
plt.ylabel("Amplitude", fontsize=14)
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")
plt.legend(fontsize=12)
plt.grid(True)
plt.show()