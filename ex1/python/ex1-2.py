#! /bin/python3
import numpy as np


def f(x):
    return x - np.tan(x)


# 二分法
def dichotomy(max_x, min_x, error):
    # 同符号の場合はFalseを返す
    if f(max_x) * f(min_x) > 0:
        return False, 0

    num = 0
    max_trials = 1e5
    mid_x = (max_x + min_x) / 2
    while(abs(f(mid_x)) > error):
        if(f(min_x) * f(mid_x) >= 0):
            min_x = mid_x
        else:
            max_x = mid_x

        mid_x = (max_x + min_x) / 2

        if(num > max_trials):
            return False ,0

        num = num + 1

    return True, mid_x



def main():
    step = 1e-5
    error = 1e-7
    min_x = 0
    max_x = 15
    now_x = min_x + step

    print("step  : {}".format(step))
    print("error : {}".format(error))
    print("range : {} ~ {}".format(min_x, max_x))
    print()
    print("|{:20s}|{:20s}|".format("   x", "   error"))
    print("|" + "-" * 20 + "|" + "-" * 20 + "|")

    # 範囲の両端の値の判定
    if abs(f(min_x)) < error:
        print("|{:20.15f}|{:20.15f}|".format(min_x, f(min_x)))
        min_x += step
    if abs(f(max_x)) < error:
        print("|{:20.15f}|{:20.15f}|".format(max_x, f(max_x)))

    while(now_x < max_x):
        if(f(min_x) * f(now_x) < 0):
            success , ans_x = dichotomy(now_x, min_x, error)
            if success:
                print("|{:20.15f}|{:20.15f}|".format(ans_x, f(ans_x)))
                min_x = now_x
                now_x = min_x
            else:
                min_x = now_x
                now_x = min_x + step
                continue

        now_x = now_x + step


if __name__ == "__main__":
    main()
