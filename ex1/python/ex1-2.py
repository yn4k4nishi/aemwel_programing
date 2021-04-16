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
            return False

        num = num + 1

    return mid_x


# aとbの間にtan(x)の不連続点があるかチェックする
def checkDiscontinuous(a, b):
    # 第何象限か計算する
    t_a = int(a / (np.pi / 2))
    t_a = t_a % 4 + 1

    t_b = int(b / (np.pi / 2))
    t_b = t_b % 4 + 1

    # 第1象限と第2象限を跨ぐ場合はFalse
    if(t_a == 1 and t_b == 2):
        return False
    elif(t_a == 2 and t_b == 1):
        return False

    # 第3象限と第4象限を跨ぐ場合はFalse
    if(t_a == 3 and t_b == 4):
        return False
    elif(t_a == 4 and t_b == 3):
        return False

    return True


def main():
    step = 0.00001
    min_x = -0.01
    max_x = 15
    now_x = min_x + step

    print("step : {}".format(step))
    print("range : {} ~ {}".format(min_x, max_x))
    print()
    print("|{:20s}|{:20s}|".format("   x", "   error"))
    print("|" + "-" * 20 + "|" + "-" * 20 + "|")

    while(now_x < max_x):
        if(not checkDiscontinuous(min_x, now_x)):
            min_x = now_x
            now_x = min_x + step
            continue

        if(f(min_x) * f(now_x) < 0):
            ans_x = dichotomy(now_x, min_x, 0.00001)
            print("|{:20.15f}|{:20.15f}|".format(ans_x, f(ans_x)))
            min_x = now_x
            now_x = min_x

        now_x = now_x + step


if __name__ == "__main__":
    main()
