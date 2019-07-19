import numpy as np
from numpy import genfromtxt
import sys

# Get the matrix from given filename.
M = genfromtxt(sys.argv[1], delimiter=',')

U, S, V = np.linalg.svd(M, full_matrices=False)
M_h = np.matmul(np.matmul(U, np.diag(S)), V)
print(np.std(M), np.std(M_h), np.std(M - M_h))

np.savetxt('output.csv', M_h, delimiter=',')
