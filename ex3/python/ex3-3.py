#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# Parameter
w = 1e10 # omega
a = 1 

mu_0  = 1.256637e-6
mu    = 1 * mu_0
eps_0 = 8.854188e-12
eps   = 2.6 * eps_0

beta = np.sqrt( w**2 * mu * eps - np.pi**2 / 4 / a**2 )
k_0 = np.sqrt(   beta**2 - w**2 * mu_0 * eps_0 )
k   = np.sqrt( - beta**2 + w**2 * mu   * eps   )

B = np.sqrt( w * eps / beta / a ) 
C = np.sqrt( k_0 * w * eps_0 / beta )

def E_x(x):
        return np.where(
        x < a,
        - beta / w / eps   * B * np.cos( k * x ),
        - beta / w / eps_0 * C * np.exp( -k_0 * (x - a) )
    )

def E_z(x):
    return np.where(
        x < a,
        k / w / eps * B * np.sin( k * x ),
        - k_0 / w / eps_0 * C * np.exp( -k_0 * (x - a) )
    )

def H_y(x):
    return np.where(
        x < a,
        B * np.cos( k * x ),
        C * np.exp( -k_0 * (x - a) )
    )


def main():
    x = np.linspace(0, 3, 1000)

    y = E_x(x)
    # y = E_z(x)
    # y = H_y(x)

    # plt.plot(x, y)
    plt.scatter(x, y, marker='.')

    plt.ylim(-30 ,30)

    plt.show()


if __name__ == '__main__':
    main()