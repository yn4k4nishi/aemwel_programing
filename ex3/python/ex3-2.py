#! /usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# 分散曲線
def dispersion_curve():
    w = np.linspace(0,1000, 100000)

    A_prime = 1
    mu = 1
    mu_0 = 1
    ep = 1
    ep_0 = 1
    a = 1

    beta2a = np.arctan2( 
        A_prime * np.sin(w**2 * mu * ep * a) - np.cos(w**2 * mu_0 * ep_0 * a ),
        A_prime * np.sin(w**2 * mu * ep * a) + np.sin(w**2 * mu_0 * ep_0 * a ),
        )
    
    beta = np.sqrt(beta2a / 2)


if __name__ == "__main__":
    dispersion_curve()
