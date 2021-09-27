#! /bin/usr/python3
# coding:utf-8

from functools import partial
import numpy as np
import matplotlib.pyplot as plt

def main1():
    w = np.linspace(0.1, 3.5, 10000)

    L_R = 1
    C_R = 1
    L_L = 1
    C_L = 1

    Z = w * L_R - 1 / w / C_L
    Y = w * C_R - 1 / w / L_L
    YZ = -Y * Z

    B_T = Z / 2 * ( 2 + YZ / 2 )
    C_T = Y

    B_P = Z
    C_P = Y / 2 * ( 2 + YZ / 2 )


    Z_T = np.sqrt(B_T / C_T)
    Z_P = np.sqrt(B_P / C_P)

    plt.ylim(0, 10)

    plt.scatter(w , Z_T, label="$Z_T$", s=10)
    plt.scatter(w , Z_P, label="$Z_P$", s=10)
    plt.legend()
    plt.show()

def main2():
    f = np.linspace(1, 10e9, 1e5)
    f_GHz = f / 1e9
    w_ = 2 * np.pi * f

    Z_B = np.array([])
    A_n = np.array([])
    B_n = np.array([])
    C_n = np.array([])
    D_n = np.array([])

    for w in w_:

        Z_0 = 50
        Y_0 = 1/Z_0

        C_0 = 1.5e-12
        L_0 = 11.2e-9
        theta = 0.25 / (2.0 * np.pi * 1.5e9) * w  # 0.25 @1.5GHz 

        Z = 1/ 1j /w /C_0
        Y = 1/ 1j /w /L_0

        A = np.cos(theta) + 1j/2*(Z*Y_0+Z_0*Y)*np.sin(theta) + Z*Y/2*np.cos(theta/2)*np.cos(theta/2)
        B = Z * np.cos(theta) + 1j*Z/4 *(Z*Y_0 + Z_0*Y + 4*Z_0/Z)*np.sin(theta) + Z*Z*Y/4*np.cos(theta/2)*np.cos(theta/2) - Z_0*Z_0*Y*np.sin(theta/2)*np.sin(theta/2)
        C = Y*np.cos(theta/2)*np.cos(theta/2) + 1j*Y_0*np.sin(theta)
        D = Z*Y/2*np.cos(theta/2)*np.cos(theta/2) + 1j/2*(Z*Y_0 + Z_0*Y)*np.sin(theta) + np.cos(theta)

        Z_B = np.append(Z_B, np.sqrt(B/C))

        # 単位セルから有限セルに 5セルで
        N = 5
        F = np.array([[A,B],[C,D]])
        for _ in range(N-1):
            F = np.dot(F, F)
        A_n = np.append(A_n, F[0][0])
        B_n = np.append(B_n, F[0][1])
        C_n = np.append(C_n, F[1][0])
        D_n = np.append(D_n, F[1][1])


    S11 = 1/(A_n + B_n/Z_0 + C_n*Z_0 + D_n) * ( A_n + B_n/Z_0 - C_n*Z_0 - D_n)
    S21 = 1/(A_n + B_n/Z_0 + C_n*Z_0 + D_n) * 2
    S12 = 1/(A_n + B_n/Z_0 + C_n*Z_0 + D_n) * 2 #* (A*D - B*C) # AD-BC=1を満たしてない
    S22 = 1/(A_n + B_n/Z_0 + C_n*Z_0 + D_n) * (-A_n + B_n/Z_0 - C_n*Z_0 + D_n)

    S11_dB = 20 * np.log10(abs(S11))
    S21_dB = 20 * np.log10(abs(S21))
    S12_dB = 20 * np.log10(abs(S12))
    S22_dB = 20 * np.log10(abs(S22))

    plt.figure(figsize=(18,9))

    # Bloch impedance
    plt.subplot(1,2,1)
    plt.ylim(-300,300)
    plt.plot(f_GHz, Z_B.real)
    # plt.scatter(f_GHz, Z_B.real)
    plt.title("Real part")
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("Imepedance [$\Omega$]")

    plt.subplot(1,2,2)
    plt.ylim(-300,300)
    plt.plot(f_GHz, Z_B.imag)
    # plt.scatter(f_GHz, Z_B.imag)
    plt.title("Imaginary part")
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("Imepedance [$\Omega$]")

    plt.show()

    ## S param
    plt.figure(figsize=(18,9))
    plt.title("S parameter")
    plt.ylim(-30, 0)
    plt.xlabel("Frequency [GHz]")
    plt.ylabel("S [dB]")
    
    # plt.ylim(-1.1, 1.1)
    # plt.plot(f_GHz, S11, label="S11")
    # plt.plot(f_GHz, S21, label="S21")
    # plt.plot(f_GHz, S12, label="S12")
    # plt.plot(f_GHz, S22, label="S22")

    plt.plot(f_GHz, S11_dB, label="S11")
    plt.plot(f_GHz, S21_dB, label="S21")
    # plt.plot(f_GHz, S12_dB, label="S12")
    # plt.plot(f_GHz, S22_dB, label="S22")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    # main1()
    main2()
