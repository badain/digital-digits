#####################################################################
# Description: treinamento baseado em fatoracao nao negativa
#              para classificacao de digitos manuscritos utilizando
#              a database MNIST
# Dependencies: time, argparse, fatorização_nao_negativa
# Usage: training_MNIST.py ndig_treino p --t
# Positional arguments:
#     ndig_treino   numero de imagens a ser utilizada para fatoracao
#     P             fator de componentes da decomposicao
# Optional arguments:
#     -h, --help    shows help message and exit
#     --t, --times  guarda o tempo de treinamento para cada digito
# Post-Condition: armazena as matrizes Wd decompostas para cada
#                 digito
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import time
from nnmf import *

## Decompoe A = Wd*H por fatoracao nao negativa
def treino(ndig_treino, p, d):
    convergencia = [False, 100] # pode mudar
    a = np.loadtxt("dados_mnist/train_dig" + str(d) + ".txt", usecols=range(ndig_treino)) / 255
    decomp = nao_negativa(a, p, convergencia)
    return decomp[0] # é a matriz Wd

# Grava o tempo despendido no treinamento para cada digito
ndig = [100, 1000, 4000]
componentes = [5, 10, 15]

for ndig_treino in ndig:
    for p in componentes:
        t = open("output/train_times"+ "_" + str(ndig_treino) + "_" + str(p) +".txt", "w")
        t.write("Tempos para o treinamento de cada digito (em s):\nndig_treino: "+str(ndig_treino)+" p: "+str(p)+"\n")

        # Gera a matriz wd para cada digito
        start_total = time.time()
        for d in range(10):
            start = time.time()
            wd = treino(ndig_treino, p, d)
            elapsed_time = time.time() - start
            t.write("d" + str(d) + ": " + str(elapsed_time) + "\n")
            np.savetxt("output/W_" + str(d) + "_" + str(ndig_treino) + "_" + str(p) + ".txt", wd)
        elapsed_total = time.time() - start_total
        t.write("total: " + str(elapsed_total))
        t.close()