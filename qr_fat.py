import argparse
import sys
from rot_givens import *

parser = argparse.ArgumentParser(description='Implements matrix QR Factorization based on Givens Rotation.')
parser.add_argument('--p', '--precision', type=int, nargs='?', const=28, default=28, help='precision of decimal operations', required=False)
parser.add_argument('--r', '--representation', type=int, nargs='?', const=16, default=16, help='precision of decimal representation', required=False)
args = parser.parse_args()
if args.r > args.p:
    print("usage: qr_fat.py [-h] [--p [P]] [--r [R]](--r <= --p)")
    print("qr_fat.py: error: argument --r/--representation: --r must be <= --p")
    sys.exit(1)
getcontext().prec = args.p

##########################################################
# Description: Implements matrix QR Factorization based on
#              Givens Rotation
# Dependencies: rot_givens, NumPy, math, Decimal
#
# Usage: qr_fat.py [-h] [--p [P]] [--r [R]](--r <= --p)
#
# optional arguments:
#  -h, --help            show help message and exit
#  --p [P], --precision [P]
#                        precision of decimal operations
#  --r [R], --representation [R]
#                        precision of decimal representation
#                        --r must be <= --p
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
    
    for k in range(m):                                  # percorre horizontalmente
        for j in range((n-1), k, -1):                   # percorre verticalmente, de baixo para cima 
            i = j - 1                                   # se o elemento é != aplica rot_givens
            if w[j][k] != 0:
                w = rot_givens(w, n, m, i+1, j+1, k+1)  # desloca os indices para inicio em 1

    if args.p == args.r:
        return w
        
    return matrix_representation_round(w, args.r)

def matrix_representation_round(w, precision):
    w_len = np.shape(w)
    n = w_len[0]
    m = w_len[1]
    
    precision_str = '1E-' + str(precision)
    for i in range(n):
        for j in range(m):
            w[i][j] = Decimal(w[i][j]).quantize(Decimal(precision_str)).normalize()
            
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