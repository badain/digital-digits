from systems_qr import *
import argparse
######################################################################
# Description: biblioteca de funcoes para resolucao de fatoracao nao
#              negativa
# Dependencies: systems_qr.py
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
######################################################################

# função que normaliza as colunas de W, ou seja a norma de cada coluna é 1
def normaliza(W, n, p):
    s = np.zeros(p)
    for j in range(p): s[j] = math.sqrt(np.sum(pow(W[0:n,j],2)))
    for j in range(p): W[0:n,j] = W[0:n,j]/s[j]
    return

# função para calcular a norma do erro entre A e WH
def erro(h, w, a):
    wh = np.matmul(w,h).copy()
    erro = np.sum(pow((a[:,:] - wh[:,:]),2))
    return erro

######################################################################
# Description: função que realiza a fatoração não negativa de a em wh
# Usage: nao_negativa(a, p, convergencia)
# 
# Pre-Condition:  a: n x m matrix
#                 p: p < m, p < n, p > 0, inteiro
#                 convergencia: [bool, int]
#                 convergencia[0]: ocorrencia de convergencia
#                 convergencia[1]: número de iterações necessárias
# Post-Condition: returns w and h satisfying wh = a
#                 w: n x p matrix
#                 h: p x m matrix
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
######################################################################
def nao_negativa(A, p, convergencia):
    # Matrix Shape
    n = A.shape[0]
    m = A.shape[1]

    # Matrix Generation
    W = np.random.rand(n, p)
    Wt = W.T.copy()
    H = np.random.rand(p,m)

    # Convergencia
    norma_erro = np.zeros(convergencia[1]) # vetor com a norma do erro de cada iteração
    
    # Fatoracao nao negativa
    for l in range(convergencia[1]):              # convergencia[1] -> max iteracoes
        normaliza(W, n, p)                        # normaliza w
        systems(H, W, A.copy())                   # qr factoration
        H = np.where(H < 0, 1e-08, H)             # substitui negativos e 0 por epslon 1e-08 (utilizar 0 pode causar instabilidade numérica)
        systems(Wt, H.T.copy(), A.T.copy())       # qr factoration (transpostas)
        W = np.where(Wt.T < 0, 1e-08, Wt.T)       # substitui pela transposta e transforma negativos e 0 em epslon 1e-08
        norma_erro[l] = erro(H, W, A.copy())      # avalia o erro entre A e WH
        
        # Critério de Convergência
        if (abs(norma_erro[l] - norma_erro[l-1]) < 1e-05): # erro 1e-05 usado para definir convergencia
            convergencia[0] = True
            convergencia[1] = l + 1
            break

    return [W, H, norma_erro]

########################################################################
# Description: System resolution based on Non-Negative Factorization
# Usage: --v, --validation validation mode
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
########################################################################
def main():
    a = np.array([[3/10, 3/5, 0],
                  [1/2, 0, 1],
                  [4/10, 4/5, 0]])
    p = 2
    convergencia = [False, 100]
    decomposicao = nao_negativa(a, p, convergencia)
    print("Seguem os resultados:\n----------------------\nO resultado convergiu?")
    if (convergencia[0]):
        print("Sim! foram necessárias",convergencia[1],"iterações para a convergência")
    else:
        print("Não...")
    print("\nMatriz W:")
    print(decomposicao[0])
    print("\nMatriz H:")
    print(decomposicao[1])
    print("\nNorma do erro para cada iteração:")
    print(decomposicao[2][:convergencia[1]])
    return
    
parser = argparse.ArgumentParser(description='System resolution based on Non-Negative Factorization')
parser.add_argument('--v', '--validationn', default=False, action='store_true', help='validation mode')
args = parser.parse_args()
if (args.v): main()