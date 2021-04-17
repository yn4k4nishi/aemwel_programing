#! /usr/bin/python3
import numpy as np


M = [[  3+4j, -9j , 6-5j, 8+1j ],
     [ -4+5j,  7  , 2+3j, 4+1j ],
     [  7-3j, 4-7j, -3j , 5-3j ],
     [  1+8j, 9-6j, 1-1j,  -3  ]]


def main():
    det_M = np.linalg.det(np.array(M))
    print("det(M) = {:.4f} {:.4f}j".format(det_M.real, det_M.imag) )


if __name__ == "__main__":
    main()
