from rot_givens import *
######################################################################
# Description: single system solution wx = b based on QR Factorization
# Usage: single_system(w, b)
# 
# Pre-Condition:  w: n x m matrix,
#                 b: n x 1 matrix
# Post-Condition: returns x satisfying wx = b
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
######################################################################
def single_system(w, b):
    # Matrix Shape
    n = w.shape[0]
    m = w.shape[1]

    # QR factorization
    for k in range(m):                      # percorre horizontalmente
        for j in range((n - 1), k, -1):     # percorre verticalmente, de baixo para cima
            i = j - 1                       # se o elemento é != aplica rot_givens
            if abs(w[j][k]) > pow(10, -8):  # verifica se w[j][k] é nulo usando intervalo de erro
                angles = rotation_angle_for_zero(w[i][k], w[j][k])
                w = rot_givens(w, m, i, j, k, angles["c"], angles["s"])
                b = rot_givens_unopt(b, 1, i, j, angles["c"], angles["s"])

    # Generating x solution vector
    x = np.zeros((m,1))
    x[m - 1][0] = b[m - 1][0] / w[m - 1][m - 1]

    # Back substitution
    for k in range((m - 2), -1, -1):
        s = 0
        for j in range((k + 1), m):
            s += w[k][j] * x[j]
        x[k][0] = (b[k][0] - s) / w[k][k]
    return x
   
########################################################################
# Description: multiple system solution wh = a based on QR Factorization
# Usage: single_system(w, a)
# 
# Pre-Condition:  w: n x m matrix,
#                 a: n x p matrix
# Post-Condition: returns h satisfying wh = a
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
########################################################################
def multiple_system(w, a):
    # Matrix Shapes
    m = a.shape[1]
    n = w.shape[0]
    p = w.shape[1]

    # QR factorization
    for k in range(p):                      # percorre horizontalmente
        for j in range((n - 1), k, -1):     # percorre verticalmente, de baixo para cima
            i = j - 1                       # se o elemento é != aplica rot_givens
            if abs(w[j][k]) > pow(10, -8):  # verifica se w[j][k] é nulo usando intervalo de erro
                angles = rotation_angle_for_zero(w[i][k], w[j][k])
                w = rot_givens(w, p, i, j, k, angles["c"], angles["s"])
                a = rot_givens_unopt(a, m, i, j, angles["c"], angles["s"])
    
    # H solution matrix
    h = np.zeros((p,m))
    for j in range(m):
        h[p - 1][j] = a[p - 1][j] / w[p - 1][p - 1]

    # Back substitution
    for k in range(p - 2, -1, -1):
        for j in range(m):
            s = 0
            for i in range((k + 1), p):
                s += w[k][i] * h[i][j]
            h[k][j] = (a[k][j] - s) / w[k][k]
    return h

def systems(h, w, a):
    # Matrix Shapes
    m = a.shape[1]
    n = w.shape[0]
    p = w.shape[1]

    # QR factorization
    for k in range(p):                     # percorre horizontalmente
        for j in range((n - 1), k, -1):    # percorre verticalmente, de baixo para cima
            i = j - 1                      # se o elemento é != aplica rot_givens
            if abs(w[j,k]) > pow(10, -8):  # verifica se w[j][k] é nulo usando intervalo de erro
                angles = rotation_angle_for_zero(w[i,k], w[j,k])
                w = rot_givens(w, p, i, j, k, angles["c"], angles["s"])
                a = rot_givens_unopt(a, m, i, j, angles["c"], angles["s"])

    # H solution matrix
    for j in range(m):
        h[p - 1,j] = a[p - 1,j] / w[p - 1,p - 1]

    # Back substitution
    for k in range(p - 2, -1, -1):
        for j in range(m):
            s = 0
            for i in range((k + 1), p):
                s += w[k,i] * h[i,j]
            h[k,j] = (a[k,j] - s) / w[k,k]
    return

########################################################################
# Description: Validation
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
########################################################################
def create_A_matrix(n, m):  # create the A matrix for examples c and d
    A = np.zeros((n,m))
    for j in range(m):
        for i in range(n):
            if (j == 0):
                A[i][j] = 1
            elif (j == 1):
                A[i][j] = i + 1
            else:
                A[i][j] = 2 * (i + 1) - 1
    return A


def main():
    # client test
    # a) Single system Wx = b: n = m = 64; W = wa, b = ba
    wa = np.zeros((64,64))
    for i in range(64):
        for j in range(64):
            if (i == j):
                wa[i][j] = 2
            elif (abs(i - j) == 1):
                wa[i][j] = 1
    ba = np.ones((64, 1))
    wc = wa.copy()  # useful copy for example c
    xa = single_system(wa, ba)

    # b) Single system Wx = b: n = 20, m = 17; W = wb, b = bb
    wb = np.zeros((20,17))
    bb = np.zeros((20,1))
    for i in range(20):
        bb[i] = i + 1
        for j in range(17):
            if (abs(i - j) <= 4):
                wb[i][j] = 1 / (i + j + 1)
    wd = wb.copy()  # useful copy for example d
    xb = single_system(wb, bb)

    # c) Multiple systems WH = A; n = p = 63, m = 3, W = wc, A = Ac
    Ac = create_A_matrix(64, 3)
    hc = multiple_system(wc, Ac)

    # d) Multiple systems WH = A; n = 20, p = 17; m = 3, W = wd, A = Ad
    Ad = create_A_matrix(20, 3)
    hd = multiple_system(wd, Ad)
    print("teste A")
    print(xa)
    print()
    print("teste B")
    print(xb)
    print()
    print("teste C")
    print(hc)
    print()
    print("teste D")
    print(hd)

    return

teste = False
if (teste):
    main()
