#! /bin/python3
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x - np.tan(x)

def main():
    x = np.linspace(0, 15, 1000)

    plt.ylim(-50, 50)
    plt.plot(x, f(x))
    plt.show()


if __name__ == "__main__":
    main()
