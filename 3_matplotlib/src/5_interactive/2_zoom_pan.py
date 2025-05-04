import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

# Sample data
x = range(100)
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y, label='y = x^2')
ax.set_title('Zoom and Pan Example')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()

# Function to be called when the rectangle is drawn
def onselect(eclick, erelease):
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    ax.set_xlim(min(x1, x2), max(x1, x2))
    ax.set_ylim(min(y1, y2), max(y1, y2))
    plt.draw()

# Create a RectangleSelector
rectangle_selector = RectangleSelector(ax, onselect, useblit=True,
                                       button=[1],  # Left mouse button
                                       minspanx=5, minspany=5,
                                       spancoords='pixels', interactive=True)

plt.show()