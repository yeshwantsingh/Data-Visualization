import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis
fig, ax = plt.subplots()
xdata = np.linspace(0, 2 * np.pi, 100)
ydata = np.sin(xdata)
line, = ax.plot(xdata, ydata)

# Setting the limits and labels
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)
ax.set_title('Sine Wave Animation')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Animation function
def animate(i):
    line.set_ydata(np.sin(xdata + i / 10.0))  # Update the data
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Show the animation
plt.show()