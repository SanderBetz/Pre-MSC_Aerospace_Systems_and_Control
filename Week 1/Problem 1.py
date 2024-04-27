import numpy as np
np.random.seed(7)

mat = np.random.randn(5, 5)
mat = np.array([[int(round(i, 0)) for i in mat[j]] for j, value in enumerate(mat)])
rowvector = np.arange(-2,3).reshape((1,5))
columnvector = np.arange(0,6).reshape((6, 1))

mat = np.vstack([mat, rowvector])
mat = np.hstack([mat, columnvector])
non_zeros = np.count_nonzero(mat)

print(non_zeros)

