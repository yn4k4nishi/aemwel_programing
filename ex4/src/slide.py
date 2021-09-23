#! /bin/usr/python3

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

a = 1
b = 0

f = np.linspace(1, 10e9, 1e3)

Z_0 = 50.0
Y_0 = 1.0 / Z_0

w = 2.0 * np.pi * f

L_0 = 13.2e-9
C_0 = 0.5e-12
d_v = 0.25 / (2.0 * np.pi * 1.5e9)  # 0.25rad @1.5GHz

x_data = []
y_data = []

# 分散曲線
for beta_d in np.linspace(-np.pi, np.pi, 1e3):
    def error(w):
        theta = d_v * w 
        Z = - 1j / w / C_0
        Y = - 1j / w / L_0
        return np.cos(beta_d) - (np.cos(theta) + Z*Y / 2.0 * np.cos(theta/2.0) * np.cos(theta/2.0) + 1j/2 * ( Z/Z_0 + Y/Y_0 ) * np.sin(theta))

    w0 = w[0]
    for w_ in w:
        if error(w0).real * error(w_).real < 0:
            x_data.append(beta_d)
            y_data.append(optimize.bisect(error, w0, w_))
        w0 = w_


fig, ax = plt.subplots(figsize=(12,8))
plt.subplots_adjust(left=0.1, bottom=0.3)
# plt.axis("equal")
# plt.xlim(-5,5)
# plt.ylim(-5,5)

l = plt.scatter(x_data, y_data)

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
