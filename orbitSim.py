import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define gravitational constant
G = 6.6743e-11

# Define initial conditions
m1 = 5.97e24  # mass of Earth
m2 = 7.34e22  # mass of Moon
r1 = np.array([0, 0, 0])  # initial position of Earth
r2 = np.array([384400000, 0, 0])  # initial position of Moon
v1 = np.array([0, 0, 0])  # initial velocity of Earth
v2 = np.array([0, 1022, 0])  # initial velocity of Moon

# Define time step and total time
dt = 1000  # time step in seconds
T = 86400 * 30  # total time in seconds (30 days)

# Initialize arrays for positions and velocities
r1_array = [r1]
r2_array = [r2]
v1_array = [v1]
v2_array = [v2]

# Define a function to update the simulation
def update(t):
    global r1, r2, v1, v2, r1_array, r2_array, v1_array, v2_array

    # Calculate distance between planets
    r = np.linalg.norm(r1 - r2)

    # Calculate gravitational force
    F = G * m1 * m2 / r**2
    F1 = -F * (r1 - r2) / r
    F2 = -F1

    # Update positions and velocities using Euler method
    r1 = r1 + v1 * dt
    v1 = v1 + F1 / m1 * dt
    r2 = r2 + v2 * dt
    v2 = v2 + F2 / m2 * dt

    # Append positions and velocities to arrays
    r1_array.append(r1)
    r2_array.append(r2)
    v1_array.append(v1)
    v2_array.append(v2)

    # Update the plot
    ax.clear()
    ax.plot([r[0] for r in r1_array], [r[1] for r in r1_array], [r[2] for r in r1_array])
    ax.plot([r[0] for r in r2_array], [r[1] for r in r2_array], [r[2] for r in r2_array])
    ax.set_xlim(-400000000, 400000000)
    ax.set_ylim(-400000000, 400000000)
    ax.set_zlim(-400000000, 400000000)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Animate the simulation
ani = FuncAnimation(fig, update, frames=np.arange(dt, T, dt), interval=1)

# Show the plot
plt.show()
