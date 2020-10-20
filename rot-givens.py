import numpy as np
import math

##########################################################
# Description: calculating  c and s based on wik and wjk
# Dependencies: math
# Usage: rotation_angle_for_zero(wik, wjk)
# 
# Pre-Condition: wik,wjk:real
# Post-Condition: returns a dictionary storing sine and
#                 cossine values that make wjk = 0 when
#                 applied in a Givens Rotation
#
# Author: Rafael Badain @ University of Sao Paulo
##########################################################

def rotation_angle_for_zero(wik, wjk):
    if abs(wik) >= abs(wjk):
        tal = (wjk / wik) * (-1)
        c = 1 / math.sqrt(1+(tal*tal))
        s = c * tal
    else:
        tal = (wik / wjk) * (-1)
        s = 1 / math.sqrt(1+(tal*tal))
        c = s * tal

    return {'c': c, 's': s}

##########################################################
# Description: Implements a Givens Rotation Method
# Dependencies: NumPy
# Usage: rot_givens(W,n,m,i,j,c,s)
#        W: matrix to be rotated
#        n: # of lines of W
#        m: # of collumns of W
#        i, j: plane of rotation coordinates
#        c, s: cossine and sine of rotation angle
#
# Pre-Condition: n,m,i,j:int
#                c,s:real
#                W(n,m): array length n of lists length m
#
# Post-Condition: Returns a W(n,m) matrix Givens Rotated.
#
# Author: Rafael Badain @ University of Sao Paulo
##########################################################
def rot_givens(w, n, m, i, j, c, s):
    # percorre a matrix rotacionando os elementos
    # das linhas i e j coluna por coluna ate m
    for r in range(m):
        aux     = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux

    return w

### debug
def generate_matrix(n,m):
    w = [[ 2.,  1.,   1.,  -1.,   1.],
         [ 0.,  3.,   0.,   1.,   2.],
         [ 0.,  0.,   2.,   2.,  -1.],
         [ 0.,  0.,  -1.,   1.,   2.],
         [ 0.,  0.,   0.,   3.,   1.]]
#   w = np.zeros((n,m)) # zero matrix
    return w

w = generate_matrix(5,5)
print(w)
angles = rotation_angle_for_zero(w[3-1][3-1], w[4-1][3-1])
w_givens = rot_givens(w, 5, 5, 3-1, 4-1, angles["c"], angles["s"])
print(w_givens)
a = math.sqrt(5)
print(3 / a)
print(4 / a)
print(5 / a)