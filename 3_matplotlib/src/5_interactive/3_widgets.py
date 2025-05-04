from matplotlib import pyplot as plt
from matplotlib.widgets import Slider, Button

# Create a simple plot
x = range(0, 100)
y = [i**2 for i in x]

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(x, y, lw=2)

# Add sliders for interactive control
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(ax_slider, 'Scale', 0.1, 10.0, valinit=1)

# Update function for the slider
def update(val):
    scale = slider.val
    line.set_ydata([i**2 * scale for i in x])
    fig.canvas.draw_idle()

slider.on_changed(update)

# Add a button to reset the plot
ax_button = plt.axes([0.8, 0.1, 0.1, 0.04])
button = Button(ax_button, 'Reset', color=axcolor, hovercolor='0.975')

# Reset function for the button
def reset(event):
    slider.reset()

button.on_clicked(reset)

plt.show()