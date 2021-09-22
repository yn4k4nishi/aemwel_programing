#! /bin/usr/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

a = 1
b = 0

x = np.linspace(-15,15,10)
y = a*x + b

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.3)
plt.axis("equal")
plt.xlim(-5,5)
plt.ylim(-5,5)

l, = plt.plot(x, y)

ax_a = plt.axes([0.1, 0.15, 0.8, 0.03])
ax_b = plt.axes([0.1, 0.1, 0.8, 0.03])
slider_a = Slider(ax_a, "a", -5, 5, valinit=0, valstep=0.01)
slider_b = Slider(ax_b, "b", -5, 5, valinit=0, valstep=0.01)

def update(val):
    a = slider_a.val
    b = slider_b.val
    y = a*x + b
    l.set_ydata(y)
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()
