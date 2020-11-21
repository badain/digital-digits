#####################################################################
# Description: treinamento baseado em fatoracao nao negativa
#              para classificacao de digitos manuscritos utilizando
#              a database MNIST
# Dependencies: time, argparse, fatorização_nao_negativa
# Usage: training_MNIST.py ndig_treino p --t
# 
# Pre-Condition: wik,wjk:real
# Post-Condition: returns a dictionary storing sine and
#                 cossine values that make wjk = 0 when
#                 applied in a Givens Rotation
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import argparse
import time
from fatorização_nao_negativa import*

## Decompoe A = Wd*H por fatoracao nao negativa
def treino(ndig_treino, p, d):
    convergencia = [False, 100] # pode mudar
    a = np.loadtxt("dados_mnist/train_dig" + str(d) + ".txt")
    decomp = nao_negativa(a[:,:ndig_treino], p, convergencia)
    return decomp[0] # é a matriz Wd

# Argument Parsing
parser = argparse.ArgumentParser(description='Decompoe um conjunto de imagens em classificadores, baseado na fatoracao nao negativa')
parser.add_argument('ndig_treino', type=int, metavar='ndig_treino', help='numero de imagens a ser utilizada para fatoracao')
parser.add_argument('p', type=int, metavar='P', help='fator de componentes da decomposicao')
parser.add_argument('--t', '--times', default=False, action='store_true', help='guarda o tempo de treinamento para cada digito')
args = parser.parse_args()

# Grava o tempo despendido no treinamento para cada digito
if(args.t):
    t = open("train_times.txt", "w")
    t.write("Tempos para o treinamento de cada digito (em s):\n")

    # Gera a matriz wd para cada digito
    start_total = time.time()
    for d in range(10):
        start = time.time()
        wd = treino(args.ndig_treino, args.p, d)
        elapsed_time = time.time() - start
        t.write("d" + str(d) + ": " + str(elapsed_time) + "\n")
        output = "W_" + str(d) + "_" + str(args.ndig_treino) + "_" + str(args.p) + ".txt"
        with open(output, "w") as f: np.savetxt(f, wd) # problema: muitas casas decimais
    elapsed_total = time.time() - start_total
    t.write("total: " + str(elapsed_total))
    t.close()
# Executa o treinamento sem computar o tempo de execucao
else:
    # Gera a matriz wd para cada digito
    for d in range(10):
        wd = treino(args.ndig_treino, args.p, d)
        output = "W_" + str(d) + "_" + str(args.ndig_treino) + "_" + str(args.p) + ".txt"
        with open(output, "w") as f: np.savetxt(f, wd) # problema: muitas casas decimais