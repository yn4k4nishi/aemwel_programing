#! /bin/usr/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

f = np.linspace(1, 10e9, 800)

x_data = []
y_data = []

S11_list = []
S21_list = []

Z_0 = 50        # 直列の特性インピーダンス
Y_0 = 1 / Z_0

Z_1 = 50        # 並列の特性インピーダンス
Y_1 = 1 / Z_1

Z_P = 50        # ポートの入力インピーダンス
Y_P = 1/Z_P

w = 2.0 * np.pi * f

c     = 299792458   # 光速
eps_r = 2.62        # 誘電率
mu_r  = 1           # 透磁率

d_0 = 0.01  # 直列の伝送線路長さ
d_1 = 0.01  # 並列の伝送線路長さ

L_0 = 10e-9
C_0 = 1.5e-12

N = 5           # セル数

def calc():
    global x_data
    global y_data

    x_data.clear()
    y_data.clear()
    S11_list.clear()
    S21_list.clear()

    for w_ in w:
        k = w_ / c * np.sqrt(eps_r * mu_r)
        theta_0 = k * d_0
        theta_1 = k * d_1 
        Z = - 1j / w_ / C_0
        # Y = - 1j / w_ / L_0
        Y = 1 / (1j * Z_1 * np.tan(theta_1))

        F_unit = np.array([[1, Z/2],[0,1]])
        F_unit = np.dot(F_unit, np.array([[np.cos(theta_0/2), 1j*Z_0*np.sin(theta_0/2)],[1j*Y_0*np.sin(theta_0/2), np.cos(theta_0/2)]]))
        F_unit = np.dot(F_unit, np.array([[1,0],[Y,1]]))
        F_unit = np.dot(F_unit, np.array([[np.cos(theta_0/2), 1j*Z_0*np.sin(theta_0/2)],[1j*Y_0*np.sin(theta_0/2), np.cos(theta_0/2)]]))
        F_unit = np.dot(F_unit, np.array([[1, Z/2],[0,1]]))
        
        # 分散曲線
        x_data.append(np.arccos( 1/2*(F_unit[0][0] + F_unit[1][1]) ))

        F = F_unit
        for _ in range(N-1):
            F = np.dot(F,F_unit)

        A = F[0][0]
        B = F[0][1]
        C = F[1][0]
        D = F[1][1]

        # S parameter
        S11 = 1/(A + B/Z_P + C*Z_P + D) * (A + B/Z_P - C*Z_P - D)
        S21 = 1/(A + B/Z_P + C*Z_P + D) * 2

        S11_list.append(20*np.log10(abs(S11)))
        S21_list.append(20*np.log10(abs(S21)))

    x_data[len(x_data):len(x_data)] = [-i for i in x_data]
    y_data = np.concatenate([f/1e9, f/1e9]).tolist()

def main():
    calc()

    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,8))
    plt.subplots_adjust(left=0.1, bottom=0.30)

    l1 = ax1.scatter(x_data, y_data, s=1)
    l2, = ax2.plot(f/1e9, S11_list, label="S11")
    l3, = ax2.plot(f/1e9, S21_list, label="S21")

    # fig.suptitle(r"$L_0 = $" + str(L_0*1e9) + r"[nH], $C_0$ = " + str(C_0*1e12) + "[pF]" )
    ax1.set_title("Dispersion Diagram")
    ax1.set_xlabel(r"$\beta d$")
    ax1.set_ylabel("Frequency [GHz]")

    ax2.set_xlabel("Frequency [GHz]")
    ax2.set_ylabel("S [dB]")
    ax2.set_ylim(-30, 3)
    ax2.legend()

    ax_4 = plt.axes([0.1, 0.20, 0.8, 0.03])
    ax_3 = plt.axes([0.1, 0.15, 0.8, 0.03])
    ax_2 = plt.axes([0.1, 0.10, 0.8, 0.03])
    ax_1 = plt.axes([0.1, 0.05, 0.8, 0.03])

    slider_Z1 = Slider(ax_4, r"$Z_1$[$\Omega$]", 0, 200, valinit= 50 , valstep= 1)
    slider_Z0 = Slider(ax_3, r"$Z_0$[$\Omega$]", 0, 200, valinit= 50 , valstep= 1)
    slider_d1 = Slider(ax_2, r"$d_1$[mm]"      , 0, 20 , valinit= 5 ,  valstep= 0.1)
    slider_d0 = Slider(ax_1, r"$d_0$[mm]"      , 0, 20 , valinit= 5 ,  valstep= 0.1)

    def update(val):
        global Z_1
        global Z_0
        global Y_1
        global Y_0
        global d_1
        global d_0

        Z_0 = slider_Z0.val
        Y_0 = 1/Z_0

        Z_1 = slider_Z1.val
        Y_1 = 1/Z_1

        d_0 = slider_d0.val / 1000
        d_1 = slider_d1.val / 1000

        calc()
        data = []
        for i in range(len(x_data)):
            data.append([x_data[i], y_data[i]])
        l1.set_offsets(data)
        l2.set_ydata(S11_list)
        l3.set_ydata(S21_list)
        fig.canvas.draw_idle()

    slider_Z1.on_changed(update)
    slider_Z0.on_changed(update)
    slider_d1.on_changed(update)
    slider_d0.on_changed(update)

    plt.show()

if __name__ == "__main__":
    main()
