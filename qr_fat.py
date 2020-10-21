from rot_givens import rot_givens
import numpy as np

##########################################################
# Description: Implements matrix QR Factorization based on
#              Givens Rotation
# Dependencies: NumPy, rot_givens
#
# Usage: qr_factorization(w)
#        W: two-dimensional array
#
# Pre-Condition: W(n,m): array length n of lists length m
#
# Post-Condition: Returns the decomposition of a matrix
#                 as a upper triangular matrix R
#
# Author: Rafael Badain @ University of Sao Paulo
##########################################################

def qr_factorization(w):
    # obtains matrix size
    w_len = np.shape(w)
    n = w_len[0]
    m = w_len[1]
    
    for k in range(m):
        for j in range((n-1), k, -1):
            i = j - 1
            if w[j][k] != 0:
                w = rot_givens(w, n, m, i+1, j+1, k+1)
    
    return w

### validation
w = [[ 2.,  1.,   1.,  -1.,   1.],
     [ 0.,  3.,   0.,   1.,   2.],
     [ 0.,  0.,   2.,   2.,  -1.],
     [ 0.,  0.,  -1.,   1.,   2.],
     [ 0.,  0.,   0.,   3.,   1.]]
print(w)
r = qr_factorization(w)
print(r)