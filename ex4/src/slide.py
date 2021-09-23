#! /bin/usr/python3

from matplotlib import colors
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

f = np.linspace(1, 10e9, 1e3)

x_data = []
y_data = []

S11_list = []
S21_list = []

Z_0 = 50.0
Y_0 = 1.0 / Z_0

w = 2.0 * np.pi * f

L_0 = 10e-9
C_0 = 1e-12
d_v = 0.25 / (2.0 * np.pi * 1.5e9)  # 0.25rad @1.5GHz

def calc():
    x_data.clear()
    y_data.clear()
    S11_list.clear()
    S21_list.clear()
    # 分散曲線
    for beta_d in np.linspace(-np.pi, np.pi, 1e3):
        def error(w):
            theta = d_v * w 
            Z = - 1j / w / C_0
            Y = - 1j / w / L_0
            return np.cos(beta_d) - (np.cos(theta) + Z*Y / 2.0 * np.cos(theta/2.0) * np.cos(theta/2.0) + 1j/2 * ( Z/Z_0 + Y/Y_0 ) * np.sin(theta)).real

        w0 = w[0]
        for w_ in w:
            if error(w0).real * error(w_).real < 0:
                x_data.append(beta_d)
                y_data.append( 1/(2 * np.pi) * optimize.bisect(error, w0, w_) / 1e9)
            w0 = w_

    # S parameter
    for w_ in w:
        theta = d_v * w_ 
        Z = - 1j / w_ / C_0
        Y = - 1j / w_ / L_0

        A = np.cos(theta) + 1j/2*(Z*Y_0+Z_0*Y)*np.sin(theta) + Z*Y*np.cos(theta/2)*np.cos(theta/2)
        B = Z * np.cos(theta) + 1j*Z/4 *(Z*Y_0 + Z_0*Y + 4*Z_0/Z)*np.sin(theta) + Z*Z*Y/4*np.cos(theta/2)*np.cos(theta/2) - Z_0*Z_0*Y*np.sin(theta/2)*np.sin(theta/2)
        C = Y*np.cos(theta/2)*np.cos(theta/2) + 1j*Y_0*np.sin(theta)
        D = Z*Y/2*np.cos(theta/2)*np.cos(theta/2) + 1j/2*(Z*Y_0 + Z_0*Y)*np.sin(theta) + np.cos(theta)

        S11 = 1/(A + B/Z_0 + C*Z_0 + D) * (A + B/Z_0 - C*Z_0 - D)
        S21 = 1/(A + B/Z_0 + C*Z_0 + D) * 2

        S11_list.append(20*np.log10(abs(S11)))
        S21_list.append(20*np.log10(abs(S21)))

def main():
    calc()

    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(12,8))
    plt.subplots_adjust(left=0.1, bottom=0.3)

    l1 = ax1.scatter(x_data, y_data, s=1)
    l2, = ax2.plot(f/1e9, S11_list)
    l3, = ax2.plot(f/1e9, S21_list)

    # fig.suptitle(r"$L_0 = $" + str(L_0*1e9) + r"[nH], $C_0$ = " + str(C_0*1e12) + "[pF]" )
    ax1.set_xlabel(r"$\beta d$")
    ax1.set_ylabel("Frequency [GHz]")

    ax2.set_xlabel("Frequency [GHz]")
    ax2.set_ylabel("S [dB]")
    ax2.set_ylim(-30, 0)

    ax_L0 = plt.axes([0.1, 0.15, 0.8, 0.03])
    ax_C0 = plt.axes([0.1, 0.1, 0.8, 0.03])
    slider_L0 = Slider(ax_L0, r"$L_0$[nH]", 0, 20, valinit=10, valstep=0.01)
    slider_C0 = Slider(ax_C0, r"$C_0$[pF]", 0,  2, valinit= 1, valstep=0.01)

    ax_button = plt.axes([0.8, 0.05, 0.1, 0.04])
    button = Button(ax_button, "Calc", color="green",hovercolor='0.7')

    def update(val):
        global L_0
        global C_0
        L_0 = slider_L0.val * 1e-9
        C_0 = slider_C0.val * 1e-12

    def click(event):
        calc()
        data = []
        for i in range(len(x_data)):
            data.append([x_data[i], y_data[i]])
        l1.set_offsets(data)
        l2.set_ydata(S11_list)
        l3.set_ydata(S21_list)
        fig.canvas.draw_idle()

    slider_L0.on_changed(update)
    slider_C0.on_changed(update)
    button.on_clicked(click)

    plt.show()

if __name__ == "__main__":
    main()
