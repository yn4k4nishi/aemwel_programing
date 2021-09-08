#! /bin/usr/python3
# coding:utf-8

from os import CLD_TRAPPED
import numpy as np
import matplotlib.pyplot as plt

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
