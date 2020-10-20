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

##########################################################
# Description: calculating  c and s based on wik and wjk
# Usage: rotation_sine_for_zero(wik, wjk)
#        rotation_cossine_for_zero(wik, wjk)
# 
# Pre-Condition: wik,wjk:int
# Post-Condition: returns sine and cossine values that
#                 make wjk = 0 when applied in a Givens
#                 Rotation
#
# Author: Rafael Badain @ University of Sao Paulo
##########################################################

import numpy as np