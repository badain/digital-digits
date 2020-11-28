#####################################################################
# Description: treinamento baseado em fatoracao nao negativa
#              para classificacao de digitos manuscritos utilizando
#              a database MNIST
# Automatizado para:
#              ndig 100, 1000, 4000 imagens
#              p    5, 10, 15
# Dependencies: time, nnmf.py
# Usage: training_MNIST_deluxe.py --t
# Optional arguments:
#     --t, --times  guarda o tempo de treinamento para cada digito
# Post-Condition: armazena as matrizes Wd decompostas para cada
#                 digito
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import time
from nnmf import *

# Decompoe A = Wd*H por fatoracao nao negativa
def treino(ndig_treino, p, d):
    convergencia = [False, 100] # pode mudar
    a = np.loadtxt("dados_mnist/train_dig" + str(d) + ".txt", usecols=range(ndig_treino)) / 255
    decomp = nao_negativa(a, p, convergencia)
    return decomp[0] # é a matriz Wd

# Argument Parsing
parser = argparse.ArgumentParser(description='Decompoe um conjunto de imagens em classificadores, baseado na fatoracao nao negativa')
parser.add_argument('--t', '--times', default=False, action='store_true', help='guarda o tempo de treinamento para cada digito')
args = parser.parse_args()

ndig = [100, 1000, 4000]
componentes = [5, 10, 15]

# Grava o tempo despendido no treinamento para cada digito
if(args.t):
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
# Executa o treinamento sem computar o tempo de execucao
else:
    for ndig_treino in ndig:
        for p in componentes:
            for d in range(10): # Gera a matriz wd para cada digito
                wd = treino(ndig_treino, p, d)
                np.savetxt("output/W_" + str(d) + "_" + str(ndig_treino) + "_" + str(p) + ".txt", wd)