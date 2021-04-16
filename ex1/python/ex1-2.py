#! /bin/python3
import numpy as np


def f(x):
    return x - np.tan(x)


# 二分法
def dichotomy(max_x, min_x, error):
    # 同符号の場合はFalseを返す
    if f(max_x) * f(min_x) > 0:
        return False

    num = 0
    mid_x = (max_x + min_x) / 2
    while(abs(f(mid_x)) > error):
        if(f(min_x) * f(mid_x) >= 0):
            min_x = mid_x
        else:
            max_x = mid_x

        mid_x = (max_x + min_x) / 2

        if(num > 1000):
            print("error : time out")
            return

        num = num + 1

    return mid_x


def main():
    step = 0.0001
    min_x = 0
    max_x = min_x + step

    while(max_x < 15):
        if(f(min_x) == 0.0):
            min_x = min_x + step
            max_x = max_x + step
            continue

        if(f(min_x) * f(max_x) < 0):
            print(min_x, max_x, f(min_x), f(max_x))
            # min_x = dichotomy(f, max_x, min_x, 0.001)
            print(dichotomy(max_x, min_x, 0.01))
            min_x = max_x
            max_x = min_x
        max_x = max_x + step


if __name__ == "__main__":
    main()
    # min_x = 4.3
    # max_x = 4.6

    # print("f(min_x) = " + str(f(min_x)))
    # print("f(max_x) = " + str(f(max_x)))
    # print(dichotomy(f, 4.3, 4.6, 0.0001))
