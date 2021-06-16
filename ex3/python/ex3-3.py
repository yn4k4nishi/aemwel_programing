#! /usr/bin/python3
from os import error
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
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

B = 2 * w * eps / beta /( a + np.sin(2*k*a)/(2*k) + eps_r / k_0 * np.cos(k*a)**2 )
B = np.sqrt(B)
C = B * np.cos(k*a)

def E_x(x):
### Function ###
        return np.where(
        x < a,
        - beta / w / eps   * B * np.cos(  k * x ),
        - beta / w / eps_0 * C * np.exp( -k_0 * (x - a) )
    )

def E_z(x):
    return np.where(
        x < a,
        k   / w / eps   * B * np.sin( k * x ),
        k_0 / w / eps_0 * C * np.exp( -k_0 * (x - a) )
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

    plt.figure(figsize=(16.0, 12.0))
    plt.suptitle('$\omega = 10^{10}, \, \epsilon_r = 3.2, \, a = 0.5 $')

    plt.subplot(1,2,1)
    plt.title('Electric Fields $\mathbb{E}$')
    plt.plot(x, E_x(x), label="$E_x$")
    plt.plot(x, E_z(x), label="$E_z$")

    plt.legend()
    plt.xlim(0  , 2*a)
    plt.xlabel('$x$')

    plt.subplot(1,2,2)
    plt.title('Magnetic Fields $\mathbb{B}$')
    plt.plot(x, H_y(x), label="$H_y$")

    plt.legend()
    plt.xlim(0  , 2*a)
    plt.xlabel('$x$')

    plt.show()


if __name__ == '__main__':
    main()