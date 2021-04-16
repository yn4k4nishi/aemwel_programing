#! /bin/python3
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 15, 1000)
    f = x - np.tan(x)

    plt.plot(x, f)
    plt.show()


if __name__ == "__main__":
    main()
