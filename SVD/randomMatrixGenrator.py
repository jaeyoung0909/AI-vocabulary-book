# randomMatrixGenerator.py : Python program for create randomly generated matrix by given size.
# Created on 18/07/2019 by Shawn Park.
# Lastest modification : 18/07/2019.

import numpy as np
import sys

# Generate radom matrix by the given size.
M = np.random.randint(-1, 2, size = (int(sys.argv[1]),int(sys.argv[2])))

# Save matrix as csv file.
np.savetxt("random.csv", M, delimiter=',')
