from fatorização_nao_negativa import*
import time

## fazer a decomposição Wd*H = A
def treino(ndig_treino, p, d):
    convergencia = [False, 100] # pode mudar
    A = np.loadtxt("dados_mnist/train_dig" + str(d) + ".txt")
    A = A[:,:ndig_treino]
    decomp = nao_negativa(A,p,convergencia)
    return decomp[0] # é a matriz Wd

def main():
    # Dados de entrada
    ndig_treino = int(input("Número de dígitos para o treinamento: "))
    p = int(input("Número de componentes (p): "))

    # Treinamento de todos os dígitos
    t = open("tempos de treinamento.txt", "w")
    t.write("Tempos para o treinamento de cada dígito (em s):\n")
    for d in range(9):
        start = time.time()
        Wd = treino(ndig_treino,p,d)
        elapsed_time = time.time() - start
        t.write("Dígito " + str(d) + ": " + str(elapsed_time) + "\n")
        # Output
        output = "W_" + str(d) + "_" + str(ndig_treino) + "_" + str(p) + ".txt"
        with open(output, "w") as f:
            np.savetxt(f, Wd) # problema: muitas casas decimai
    t.close()
main()

