#! /bin/python3
from textwrap import wrap
import numpy as np
import matplotlib.pyplot as plt
import time
import tqdm

# 分散曲線の関数
def f(x,y):
    eps_r = 3.2 

    if (-x**2 + eps_r * y**2) < 0:
        return False

    if (x**2 - y**2) == 0:
        return False

    if (-x**2 + eps_r * y**2)/(x**2 - y**2) < 0:
        return False

    return np.tan(np.sqrt(-x**2 + eps_r * y**2)) - np.sqrt((-x**2 + eps_r * y**2)/(x**2 - y**2))


# 二分法
def dichotomy(x, min_y, max_y, error):
    # 同符号の場合はFalseを返す
    if f(x, max_y) * f(x, min_y) > 0:
        return False, 0

    num = 0
    max_trials = 1e4
    mid_y = (max_y + min_y) / 2
    while(abs(f(x, mid_y)) > error):
        if(f(x, min_y) * f(x, mid_y) >= 0):
            min_y = mid_y
        else:
            max_y = mid_y

        mid_y = (max_y + min_y) / 2

        if(num > max_trials):
            return False ,0

        num = num + 1

    return True, mid_y


def main():
    error = 1e-2

    start = time.time() # 時間計測 開始

    for x in tqdm.tqdm(np.linspace(0,100,100)): # xを固定

        y_0 = 0 # 一つ前のyの値
        for y in np.linspace(0,100,100): # yの値を動かして解を探す
            if (f(x, y_0) == False) or (f(x, y_0) == False) :
                y_0 = y
                continue

            if f(x, y_0) * f(x, y) < 0:
                success, ans = dichotomy(x, y_0, y, error)
                if success:
                    # print( "x={} , y={} , error={}".format(x, ans, f(x,ans)) )
                    plt.scatter(x, ans)
            y_0 = y

    plt.show()

    # 実行時間
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == "__main__":
    main()
