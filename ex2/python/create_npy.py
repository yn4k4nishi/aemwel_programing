#! /usr/bin/python3
import numpy as np


M = np.array([[  3+4j, -9j , 6-5j, 8+1j ],
              [ -4+5j,  7  , 2+3j, 4+1j ],
              [  7-3j, 4-7j, -3j , 5-3j ],
              [  1+8j, 9-6j, 1-1j,  -3  ]])

np.save("matrix",M)
