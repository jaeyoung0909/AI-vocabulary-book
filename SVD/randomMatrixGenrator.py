import numpy as np
import sys

# Generate radom matrix by the given size.
M = np.random.randint(-1, 2, size = (int(sys.argv[1]),int(sys.argv[2])))

# Save matrix as csv file.
np.savetxt("random.csv", M, delimiter=',')
