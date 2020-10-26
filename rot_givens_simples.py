# não otimizado com decimal
import numpy as np
import math
from multimethods import multimethod

overload = multimethod


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


#@overload(np.array, int, int, int, float, float)
#def rot_givens(w, m, i, j, c, s):
    # percorre a matrix rotacionando os elementos
    # das linhas i e j coluna por coluna ate m
    #for r in range(m):
        #aux = c * w[i][r] - s * w[j][r]
        #w[j][r] = s * w[i][r] + c * w[j][r]
        #w[i][r] = aux

    #return w

# rot_givens() overload otimizado para [1, k-1] nulo
#@overload(np.array, int, int, int, int, float, float)
def rot_givens(w, m, i, j, k, c, s):
    # verifica se os elementos de 0..(k-1) sao nulos
    # nas linhas i e j
    optimizable = True
    for l in range(0, k):  # nao roda para k=0 pois nao existe elementos a esquerda
        if w[i][l] or w[j][l] != 0:
            optimizable = False
            break

    # percorre a matrix rotacionando os elementos
    # das linhas i e j coluna por coluna ate m
    if optimizable:
        column_range = range(k, m)
    else:
        column_range = range(m)

    for r in column_range:
        aux = c * w[i][r] - s * w[j][r]
        w[j][r] = s * w[i][r] + c * w[j][r]
        w[i][r] = aux

    return w
