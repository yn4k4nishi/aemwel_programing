#! /usr/bin/python3
from os import error
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import kaiser


### Parameter ###
w = 1e10 # omega
a = 0.5

mu_0  = 1.256637e-6
mu    = 1 * mu_0
eps_0 = 8.854188e-12
eps_r = 3.2
eps   = eps_r * eps_0

c = 1 / np.sqrt(mu_0 * eps_0)

## 分散曲線より
#  x = beta * a = 8.00999999999992
#  y = w * a / c = 4.92479062500169
beta = 8.01 / a
w = 4.925 * c / a

k_0 = np.sqrt(   beta**2 - w**2 * mu_0 * eps_0 )
k   = np.sqrt( - beta**2 + w**2 * mu   * eps   )

B = 2 * k_0 * w * eps_0 / beta / ( k_0 * a / eps_r + (k_0**2/k**2 + 1)* np.cos(k*a)**2 )
B = np.sqrt(B)
C = B * np.cos(k*a)

### Function ###
def E_x(x):
        return np.where(
        x < a,
        - beta / w / eps   * B * np.cos(  k * x ),
        - beta / w / eps_0 * C * np.exp( -k_0 * (x - a) ) /eps_r
    )

def E_z(x):
    return np.where(
        x < a,
        k   / w / eps   * B * np.sin( k * x ),
        k_0 / w / eps_0 * C * np.exp( -k_0 * (x - a) ) /eps_r**2
    )

def H_y(x):
    return np.where(
        x < a,
        B * np.cos( k * x ),
        C * np.exp( -k_0 * (x - a) )
    )

### main ###
def main():
    x = np.linspace(0, 2*a, 1000)

    # y = E_x(x)
    # y = E_z(x)
    # y = H_y(x)

    # x1 = np.linspace(0, a  , 100)
    # x2 = np.linspace(a, 2*a, 100)

    # plt.plot(x1, k / w / eps * B * np.sin( k * x1 ))
    # plt.plot(x2, k_0 / w / eps_0 * C * np.exp(-k_0 * (x2 - a)))

    plt.plot(x, E_x(x), label="$E_x$")
    plt.plot(x, E_z(x), label="$E_z$")
    # plt.plot(x, H_y(x), label="$H_y$")
    # plt.scatter(x, y, marker='.')

    plt.legend()
    plt.xlim(0  , 2*a)
    # plt.ylim(-2 , 2  )
    plt.xlabel('$x$')
    plt.ylabel('Amp')

    plt.show()


if __name__ == '__main__':
    main()