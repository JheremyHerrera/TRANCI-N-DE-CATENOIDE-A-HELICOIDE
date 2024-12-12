import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

a = 1
u = np.linspace(0, 2 * np.pi, 100) 
v = np.linspace(-2, 2, 100) 
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

def get(u, v, alpha):
    U, V = np.meshgrid(u, v)
    X = a * ((1 - alpha) * np.cosh(V) + alpha * np.sinh(V)) * np.cos(U)
    Y = a * ((1 - alpha) * np.cosh(V) + alpha * np.sinh(V)) * np.sin(U)
    Z = a * ((1 - alpha) * V + alpha * U)
    return X, Y, Z

def update(frame):
    ax.clear()
    alpha = frame / 200.0
    X, Y, Z = get(u, v, alpha)

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title(f"Transición de Catenaria a Helicoide - Frame {frame}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-3, 3])
    ax.set_ylim([-3, 3])
    ax.set_zlim([-3, 3])

ani = FuncAnimation(fig, update, frames=200, interval=20)
plt.show()
