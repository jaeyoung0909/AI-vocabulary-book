# svd.py : Python program for SVD.
# Created on 18/07/2019 by Shawn Park.
# Lastest modification : 18/07/2019.

import numpy as np
from numpy import genfromtxt
import sys

# Get the matrix from given filename.
M = genfromtxt(sys.argv[1], delimiter=',')

# SVD and generate augmented matrix M_h
U, S, V = np.linalg.svd(M, full_matrices=False)
M_h = np.matmul(np.matmul(U, np.diag(S)), V)

# See the differences between M and M_h
#print(np.std(M), np.std(M_h), np.std(M - M_h))

# Save M_h as a csv file.
np.savetxt('output.csv', M_h, delimiter=',')
