import numpy as np
import math
####################################################################
# Description: calculating c and s based on wik and wjk
# Usage: rotation_angle_for_zero(wik, wjk)
# 
# Pre-Condition:  wik, wjk
# Post-Condition: returns a dictionary storing sine and
#                 cossine values that makes wjk = 0 when
#                 applied in a Givens Rotation
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
####################################################################
def rotation_angle_for_zero(wik, wjk):
    if abs(wik) >= abs(wjk):
        tal = (wjk / wik) * (-1)
        c = 1 / math.sqrt(1 + (tal * tal))
        s = c * tal
    else:
        tal = (wik / wjk) * (-1)
        s = 1 / math.sqrt(1 + (tal * tal))
        c = s * tal

    return {'c': c, 's': s}

####################################################################
# Description: Implements a Givens Rotation Method
# Usage: rot_givens(W,m,i,j,k,c,s)
#        W: matrix to be rotated
#        m: # of collumns
#        i, j: plane of rotation coordinates
#        k: column coordinate to be zero
#        c, s: cossine and sine of rotation angle
#
# Pre-Condition: m,i,j,k:int
#                c,s:real
#                W(n,m): array length n of lists length m
# Post-Condition: Returns a W(n,m) matrix Givens Rotated.
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
####################################################################
def isOptimizable(w, i, j, k):
    for l in range(0, k):           # percorre as linhas i e j
        if w[i][l] or w[j][l] != 0: # busca por elementos nao nulos
            return False            # existe elemento nao nulo em i e j
    return True                     # todos os elementos sao nulos em i e j

def rot_givens(w, m, i, j, k, c, s):
    # verifica se os elementos de 0..(k-1) sao nulos nas linhas i e j
    optimizable = isOptimizable(w, i, j, k)
    
    # percorre a matriz rotacionando os elementos das linhas i e j coluna por coluna ate m
    if optimizable: r = k           # percorre a partir de k, pois os restantes sao nulos
    else: r = 0                     # percorre a partir do inicio, pois existem nao nulos

    w[i, r:m], w[j, r:m] = c * w[i][r:m] - s * w[j][r:m], s * w[i][r:m] + c * w[j][r:m]

    return w

def rot_givens_unopt(w, m, i, j, c, s):
    w[i, 0:m], w[j, 0:m] = c * w[i][0:m] - s * w[j][0:m], s * w[i][0:m] + c * w[j][0:m]

    return w