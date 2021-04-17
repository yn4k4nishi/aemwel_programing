#! /usr/bin/python3
import numpy as np
import sys
import textwrap as tw


def main():
    args = sys.argv

    if len(args) != 2:
        print("error : invaild args ")
        print("  ex) $ python3 ex2-2.py matrix.npy")
        quit()

    M = np.load(args[1])

    print("M =")
    for m in M:
        print("\t{}".format(m))
    print()

    inv_M = np.linalg.inv(M)
    print("inv_M =")
    for m in inv_M:
        print(tw.fill("\t{}".format(m),1000))
    print()


if __name__ == "__main__":
    main()
