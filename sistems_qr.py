from rot_givens_simples import *
# single sistem solution
def single_sistem(w, b):
    # w: n x m coefficients matrix
    # b: n x 1 constant terms matrix 
    w_len = np.shape(w)
    n = w_len[0]
    m = w_len[1]
    # QR factorization
    for k in range(m):  # percorre horizontalmente
        for j in range((n - 1), k, -1):  # percorre verticalmente, de baixo para cima
            i = j - 1  # se o elemento é != aplica rot_givens
            if abs(w[j][k]) > pow(10, -8):  # intervalo de erro
                angles = rotation_angle_for_zero(w[i][k], w[j][k])
                w = rot_givens(w, m, i, j, k, angles["c"], angles["s"])
                b = rot_givens(b, 1, i, j, k, angles["c"], angles["s"])

    # x: solution vector
    x = np.zeros((m,1))
    x[m - 1][0] = b[m - 1][0] / w[m - 1][m - 1]
    for k in range((m - 2), -1, -1):  # back substitution
        S = 0
        for j in range((k + 1), m):
            S += w[k][j] * x[j]
        x[k][0] = (b[k][0] - S) / w[k][k]
    return x;


# simultaneous sistems solution: WH = A --> finds the H matrix
def multiple_sistem(w, A):
    # w: n x p coefficients matrix
    # A: n x m constant terms matrix
    w_len = np.shape(w)
    A_len = np.shape(A)
    m = A_len[1]
    n = w_len[0]
    p = w_len[1]
    # QR factorization
    for k in range(p):  # percorre horizontalmente
        for j in range((n - 1), k, -1):  # percorre verticalmente, de baixo para cima
            i = j - 1  # se o elemento é != aplica rot_givens
            if abs(w[j][k]) > pow(10, -8):  # possível problem
                angles = rotation_angle_for_zero(w[i][k], w[j][k])
                w = rot_givens(w, p, i, j, k, angles["c"], angles["s"])
                A = rot_givens(A, m, i, j, k, angles["c"], angles["s"])

    # H solution matrix
    H = np.zeros((p,m))
    for j in range(m):
        H[p - 1][j] = A[p - 1][j] / w[p - 1][p - 1]

    # Back substitution
    for k in range(p - 2, -1, -1):
        for j in range(m):
            S = 0
            for i in range((k + 1), p):
                S += w[k][i] * H[i][j]
            H[k][j] = (A[k][j] - S) / w[k][k]
    return H

def sistems(H, w, A):
    # w: n x p coefficients matrix
    # A: n x m constant terms matrix
    w_len = np.shape(w)
    A_len = np.shape(A)
    m = A_len[1]
    n = w_len[0]
    p = w_len[1]
    # QR factorization
    for k in range(p):  # percorre horizontalmente
        for j in range((n - 1), k, -1):  # percorre verticalmente, de baixo para cima
            i = j - 1  # se o elemento é != aplica rot_givens
            if abs(w[j,k]) > pow(10, -8):  # possível problem
                angles = rotation_angle_for_zero(w[i,k], w[j,k])
                w = rot_givens(w, p, i, j, k, angles["c"], angles["s"])
                A = rot_givens(A, m, i, j, k, angles["c"], angles["s"])

    # H solution matrix
    for j in range(m):
        H[p - 1,j] = A[p - 1,j] / w[p - 1,p - 1]

    # Back substitution
    for k in range(p - 2, -1, -1):
        for j in range(m):
            S = 0
            for i in range((k + 1), p):
                S += w[k,i] * H[i,j]
            H[k,j] = (A[k,j] - S) / w[k,k]
    return

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
    # a) Single sistem Wx = b: n = m = 64; W = wa, b = ba
    wa = np.zeros((64,64))
    for i in range(64):
        for j in range(64):
            if (i == j):
                wa[i][j] = 2
            elif (abs(i - j) == 1):
                wa[i][j] = 1
    ba = np.ones((64, 1))
    wc = wa.copy()  # useful copy for example c
    xa = single_sistem(wa, ba)

    # b) Single sistem Wx = b: n = 20, m = 17; W = wb, b = bb
    wb = np.zeros((20,17))
    bb = np.zeros((20,1))
    for i in range(20):
        bb[i] = i + 1
        for j in range(17):
            if (abs(i - j) <= 4):
                wb[i][j] = 1 / (i + j + 1)
    wd = wb.copy()  # useful copy for example d
    xb = single_sistem(wb, bb)

    # c) Multiple sistems WH = A; n = p = 63, m = 3, W = wc, A = Ac
    Ac = create_A_matrix(64, 3)
    hc = multiple_sistem(wc, Ac)

    # d) Multiple sistems WH = A; n = 20, p = 17; m = 3, W = wd, A = Ad
    Ad = create_A_matrix(20, 3)
    hd = multiple_sistem(wd, Ad)
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
