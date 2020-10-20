import numpy as np
import math
from multimethods import multimethod
overload = multimethod

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
# Dependencies: math, NumPy, multimethods
#
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
@overload(list, int, int, int, int, float, float)
def rot_givens(w, n, m, i, j, c, s):
    # percorre a matrix rotacionando os elementos
    # das linhas i e j coluna por coluna ate m
    for r in range(m):
        aux     = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux

    return w

# rot_gives() overload corrige frame dos indices
@overload(list, int, int, int, int, int)
def rot_givens(w, n, m, i, j, k):
    i -= 1
    j -= 1
    k -= 1
    angles = rotation_angle_for_zero(w[i][k], w[j][k])
    w = rot_givens(w, 5, 5, i, j, k, angles["c"], angles["s"])
    
    return w

### validation
#   w = np.zeros((n,m)) # zero matrix
w = [[ 2.,  1.,   1.,  -1.,   1.],
     [ 0.,  3.,   0.,   1.,   2.],
     [ 0.,  0.,   2.,   2.,  -1.],
     [ 0.,  0.,  -1.,   1.,   2.],
     [ 0.,  0.,   0.,   3.,   1.]]

print(w)
w_len = np.shape(w)
w_givens = rot_givens(w, w_len[0], w_len[1], 3, 4, 3)
print(w_givens)

a = math.sqrt(5)
print(3 / a)
print(4 / a)
print(5 / a) 