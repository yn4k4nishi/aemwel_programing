#! /usr/bin/python3
import numpy as np
import sys


def main():
    args = sys.argv

    if len(args) != 2:
        print("error : invaild args ")
        print("  ex) $ python3 ex2-1.py matrix.npy")
        quit()

    M = np.load(args[1])

    print("M =\n{}".format(M))
    print()

    det_M = np.linalg.det(np.array(M))
    print("det(M) = {:.4f} {:.4f}j".format(det_M.real, det_M.imag) )


if __name__ == "__main__":
    main()
