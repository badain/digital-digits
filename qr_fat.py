import argparse
from rot_givens import *

parser = argparse.ArgumentParser(description='Implements matrix QR Factorization based on Givens Rotation.')
parser.add_argument('--p', '--precision', type=int, nargs='?', const=28, default=28, help='precision of decimal operations', required=False)
args = parser.parse_args()
getcontext().prec = args.p

##########################################################
# Description: Implements matrix QR Factorization based on
#              Givens Rotation
# Dependencies: rot_givens, NumPy, math, Decimal
#
# Usage: qr_fat.py [-h] [--p [P]]
#
# optional arguments:
#  -h, --help            show help message and exit
#  --p [P], --precision [P]
#                        precision of decimal operations
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