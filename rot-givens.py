import numpy as np
import math

##########################################################
# Description: calculating  c and s based on wik and wjk
# Dependencies: math
# Usage: rotation_angle_for_zero(wik, wjk)
# 
# Pre-Condition: wik,wjk:int
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
#                c,s:float
#                W(n,m): array length n of lists length m
#
# Post-Condition: Returns a W(n,m) matrix Givens Rotated.
#
# Author: Rafael Badain @ University of Sao Paulo
##########################################################