#! /bin/usr/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

f = np.linspace(1, 10e9, 800)

x_data = []
y_data = []

S11_list = []
S21_list = []

Z_0 = 50
Y_0 = 1 / Z_0

Z_P = 50 # ポートの入力インピーダンス
Y_P = 1/Z_P

w = 2.0 * np.pi * f

L_0 = 10e-9
C_0 = 1.5e-12
d_v = 0.25 / (2.0 * np.pi * 1.5e9)  # 0.25rad @1.5GHz

N = 5 # セル数

def calc():
    global x_data
    global y_data

    x_data.clear()
    y_data.clear()
    S11_list.clear()
    S21_list.clear()

    # 分散曲線
    # print("Calc Dispersion ...")
    theta = d_v * w 
    Z = - 1j / w / C_0
    Y = - 1j / w / L_0
    cos_b_d = (np.cos(theta) + Z*Y / 2.0 * np.cos(theta/2.0) * np.cos(theta/2.0) + 1j/2 * ( Z/Z_0 + Y/Y_0 ) * np.sin(theta)).real
    x_data = np.arccos(cos_b_d)
    x_data = np.concatenate([x_data, -1*x_data]).tolist()
    y_data = np.concatenate([f, f]).tolist()

    # S parameter
    # print("Calc S parameter ...")
    for w_ in w:
        theta = d_v * w_ 
        Z = - 1j / w_ / C_0
        Y = - 1j / w_ / L_0

        F_unit = np.array([[1, Z/2],[0,1]])
        F_unit = np.dot(F_unit, np.array([[np.cos(theta/2), 1j*Z_0*np.sin(theta/2)],[1j*Y_0*np.sin(theta/2), np.cos(theta/2)]]))
        F_unit = np.dot(F_unit, np.array([[1,0],[Y,1]]))
        F_unit = np.dot(F_unit, np.array([[np.cos(theta/2), 1j*Z_0*np.sin(theta/2)],[1j*Y_0*np.sin(theta/2), np.cos(theta/2)]]))
        F_unit = np.dot(F_unit, np.array([[1, Z/2],[0,1]]))
        
        F = F_unit
        for _ in range(N-1):
            F = np.dot(F,F_unit)

        A = F[0][0]
        B = F[0][1]
        C = F[1][0]
        D = F[1][1]

        S11 = 1/(A + B/Z_P + C*Z_P + D) * (A + B/Z_P - C*Z_P - D)
        S21 = 1/(A + B/Z_P + C*Z_P + D) * 2

        S11_list.append(20*np.log10(abs(S11)))
        S21_list.append(20*np.log10(abs(S21)))
    # print("Finish Calc.\n")

def main():
    calc()

    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(15,8))
    plt.subplots_adjust(left=0.1, bottom=0.25)

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

    ax_Z0 = plt.axes([0.1, 0.15, 0.8, 0.03])
    ax_L0 = plt.axes([0.1, 0.10, 0.8, 0.03])
    ax_C0 = plt.axes([0.1, 0.05, 0.8, 0.03])
    slider_Z0 = Slider(ax_Z0, r"$Z_0$[$\Omega$]", 0, 200, valinit= 50 , valstep= 1)
    slider_L0 = Slider(ax_L0, r"$L_0$[nH]"      , 0, 50 , valinit= 10 , valstep= 0.01)
    slider_C0 = Slider(ax_C0, r"$C_0$[pF]"      , 0, 10 , valinit= 1.5, valstep= 0.01)

    def update(val):
        global Z_0
        global Y_0
        global L_0
        global C_0
        Z_0 = slider_Z0.val
        Y_0 = 1/Z_0
        L_0 = slider_L0.val * 1e-9
        C_0 = slider_C0.val * 1e-12

        calc()
        data = []
        for i in range(len(x_data)):
            data.append([x_data[i], y_data[i]])
        l1.set_offsets(data)
        l2.set_ydata(S11_list)
        l3.set_ydata(S21_list)
        fig.canvas.draw_idle()

    slider_Z0.on_changed(update)
    slider_L0.on_changed(update)
    slider_C0.on_changed(update)

    plt.show()

if __name__ == "__main__":
    main()
