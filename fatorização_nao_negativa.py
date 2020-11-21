from sistems_qr import *

# função que normaliza as colunas de W, ou seja a norma de cada coluna é 1
def normaliza(W,n,p):
    s = np.zeros(p)
    for j in range(p):
        s[j] = math.sqrt(np.sum(pow(W[0:n,j],2)))
    for j in range(p):
        W[0:n,j] = W[0:n,j]/s[j]
    return

# função que redefine a matriz: troca elementos negativos por 0
def eliminar_negativos(H,m,n):
    epslon = 0.00000001 # trocar por efetivamente zero pode causar instabilidade numérica, portanto colocamos um epslon muito pequeno
    for i in range(m):
        for j in range(n):
            if H[i,j] < 0:
                H[i,j] = epslon

# função para calcular a norma do erro entre A e WH
def erro(H,W,A):
    WH = np.matmul(W,H).copy()
    erro = np.sum(pow((A[:,:] - WH[:,:]),2))
    return erro

# função que realiza a fatoração não negativa de A em WH, com W n x p
def nao_negativa(A, p,convergencia):
    # convergencia é uma lista com o primeiro termo como booleano se houve a convergencia ou não e o segundo o número de iterações necessárias
    A_len = np.shape(A)
    n = A_len[0]
    m = A_len[1]
    W = np.random.rand(n, p)
    Wt = W.T.copy()
    H = np.random.rand(p,m)
    A_copy = A.copy()
    epslon = 0.00001 # erro usado para definir convergencia
    itmax = convergencia[1]
    norma_erro = np.zeros(itmax) # vetor com a norma do erro de cada iteração
    for l in range(itmax):
        normaliza(W, n, p)
        sistems(H,W,A)
        A = A_copy.copy()
        eliminar_negativos(H,p,m)
        At = A.T.copy()
        Ht = H.T.copy()
        sistems(Wt,Ht,At)
        W = Wt.T.copy()
        eliminar_negativos(W,n,p)
        norma_erro[l] = erro(H,W,A)
        # critério de convergência
        if (abs(norma_erro[l] - norma_erro[l-1]) < epslon):
            convergencia[0] = True
            convergencia[1] = l + 1
            break
    return [W,H,norma_erro]

def main():
    #client test
    a = [[3/10, 3/5, 0],
         [1/2, 0, 1],
         [4/10, 4/5, 0]]
    A = np.array(a)
    p = 2
    convergencia = [False, 100]
    decomposicao = nao_negativa(A, p, convergencia)
    print("Seguem os resultados:")
    print("----------------------")
    print("O resultado convergiu?")
    if (convergencia[0]):
        print("Sim! foram necessárias",convergencia[1],"iterações para a convergência")
    else:
        print("Não...")
    print()
    print("Matriz W:")
    print(decomposicao[0])
    print()
    print("Matriz H:")
    print(decomposicao[1])
    print()
    print("Norma do erro para cada iteração:")
    print(decomposicao[2][:convergencia[1]])
    return

teste = False
if(teste):
    main()

