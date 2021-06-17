#! /usr/bin/python3
# coding: utf-8
from os import error
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
from numpy.lib.function_base import kaiser


### Parameter ###
a = 0.5

### Const ###
mu_0  = 1.256637e-6
mu    = 1 * mu_0
eps_0 = 8.854188e-12
eps_r = 3.2
eps   = eps_r * eps_0

c = 1 / np.sqrt(mu_0 * eps_0)

## 分散曲線より
# x   | y
# 4.8 |	2.803790771 
# 4.8 |	3.6061875   
# 4.8 |	4.65028125  

beta = 4.8 / a
w = 2.8038 * c / a
# w = 3.6062 * c / a
# w = 4.6503 * c / a

k_0 = np.sqrt(   beta**2 - w**2 * mu_0 * eps_0 )
k   = np.sqrt( - beta**2 + w**2 * mu   * eps   )

B = 2 * w * eps / beta /( a + np.sin(2*k*a)/(2*k) + eps_r / k_0 * np.cos(k*a)**2 )
B = np.sqrt(B)
C = B * np.cos(k*a)

def update_param(x ,y):
    global beta,w, k_0, k, B, C

    beta = x / a
    w = y * c / a

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

    ########## モード比較 ##############
    plt.figure(figsize=(16.0, 12.0))
    plt.suptitle('compare mode\n $\epsilon_r = {}, \, a = {} $'.format(eps_r, a))

    # 分散曲線より 同一の周波数
    # x     y
    # 8.82	5.001897554
    # 7.755	5.006641846
    # 5.475	5.000141602

    # E_x
    plt.subplot(3,1,1)
    plt.ylabel('$E_x$')
    update_param(8.82, 5.001897554) 
    plt.plot(x, E_x(x), label="basic mode")
    update_param(7.755, 5.006641846 )  
    plt.plot(x, E_x(x), label="2nd mode")
    update_param(5.475, 5.000141602)  
    plt.plot(x, E_x(x), label="3rd mode")
    
    plt.legend()
    plt.xlim(0  , 2*a)
    # plt.xlabel('$x$')

    # E_z
    plt.subplot(3,1,2)
    plt.ylabel('$E_z$')
    update_param(8.82, 5.001897554) 
    plt.plot(x, E_z(x), label="basic mode")
    update_param(7.755, 5.006641846 )  
    plt.plot(x, E_z(x), label="2nd mode")
    update_param(5.475, 5.000141602)  
    plt.plot(x, E_z(x), label="3rd mode")

    plt.legend()
    plt.xlim(0  , 2*a)
    # plt.xlabel('$x$')

    # H_y
    plt.subplot(3,1,3)
    plt.ylabel('$H_y$')
    update_param(8.82, 5.001897554) 
    plt.plot(x, H_y(x), label="basic mode")
    update_param(7.755, 5.006641846 )  
    plt.plot(x, H_y(x), label="2nd mode")
    update_param(5.475, 5.000141602)  
    plt.plot(x, H_y(x), label="3rd mode")

    plt.legend()
    plt.xlim(0  , 2*a)
    plt.xlabel('$x$')

    plt.show()


    ########## 周波数比較 ##############
    plt.figure(figsize=(16.0, 12.0))
    plt.suptitle('compare freq\n $\epsilon_r = {}, \, a = {} $'.format(eps_r, a))

    # 分散曲線より 同一の周波数
    # mode  x       y
    # 1     4.005	2.377813568
    # 1     8.01	4.555540009
    # 1     12	    6.762003407

    # E_x
    plt.subplot(3,1,1)
    plt.ylabel('$E_x$')
    update_param(4.005, 2.377813568) 
    plt.plot(x, E_x(x), label="$\omega={:.3e}$".format(w))
    update_param(8.01, 4.555540009)  
    plt.plot(x, E_x(x), label="$\omega={:.3e}$".format(w))
    update_param(12, 6.762003407)  
    plt.plot(x, E_x(x), label="$\omega={:.3e}$".format(w))
    
    plt.legend()
    plt.xlim(0  , 2*a)
    # plt.xlabel('$x$')

    # E_z
    plt.subplot(3,1,2)
    plt.ylabel('$E_z$')
    update_param(4.005, 2.377813568) 
    plt.plot(x, E_z(x), label="$\omega={:.3e}$".format(w))
    update_param(8.01, 4.555540009)  
    plt.plot(x, E_z(x), label="$\omega={:.3e}$".format(w))
    update_param(12, 6.762003407)  
    plt.plot(x, E_z(x), label="$\omega={:.3e}$".format(w))

    plt.legend()
    plt.xlim(0  , 2*a)
    # plt.xlabel('$x$')

    # H_y
    plt.subplot(3,1,3)
    plt.ylabel('$H_y$')
    update_param(4.005, 2.377813568) 
    plt.plot(x, H_y(x), label="$\omega={:.3e}$".format(w))
    update_param(8.01, 4.555540009)  
    plt.plot(x, H_y(x), label="$\omega={:.3e}$".format(w))
    update_param(12, 6.762003407)  
    plt.plot(x, H_y(x), label="$\omega={:.3e}$".format(w))

    plt.legend()
    plt.xlim(0  , 2*a)
    plt.xlabel('$x$')

    plt.show()


if __name__ == '__main__':
    main()