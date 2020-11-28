#####################################################################
# Description: classificacao de digitos manuscritos utilizando
#              a database MNIST
# Dependencies: time, argparse
# Usage: classify_MNIST.py ndig_treino n_test P
# Positional arguments:
#     ndig_treino   numero de imagens usadas no treinamento
#     n_test        numero de imagens a ser utilizada para teste
#     P             fator de componentes da decomposicao
# Optional arguments:
#     -h, --help    shows help message and exit
#     --d, --debug  debug mode
# Post-Condition: armazena as matrizes Wd decompostas para cada
#                 digito
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import numpy as np
import math
import argparse
import time
from systems_qr import multiple_system

# Argument Parsing
parser = argparse.ArgumentParser(description='Decompoe um conjunto de imagens em classificadores, baseado na fatoracao nao negativa')
parser.add_argument('n_test', type=int, metavar='n_test', help='numero de imagens a ser utilizada para teste')
parser.add_argument('--d', '--debug', default=False, action='store_true', help='debug mode')
args = parser.parse_args()

ndig_treino = [100, 1000, 4000]
componentes = [5,10,15]

# Input Reading
a = np.loadtxt("dados_mnist/test_images.txt", usecols=range(args.n_test)) / 255
if(args.d): print("Loaded: dados_mnist/test_images.txt "+str(a.shape))

# Output Writing
r = open("output/classify_index"+ "_" + str(args.n_test) + ".txt", "w")
r.write("Taxas de acerto para n_test: "+str(args.n_test)+"\n")

# For each image, Wd*H = A
classification  = np.zeros(args.n_test)
classification_err = np.zeros(args.n_test)

for ndig in ndig_treino:
    for p in componentes:
        r.write("\nndig_treino: "+str(ndig)+" e p: "+str(p)+"\n")
        start = time.time()
        # Digitos a serem testados
        for digit in range(10):
            if(args.d): print("Loaded: output/W_"+str(digit)+"_"+str(ndig)+"_"+str(p)+".txt"+str(a.shape))

            # Solving A - WH
            w = np.loadtxt("output/W_"+str(digit)+"_"+str(ndig)+"_"+str(p)+".txt")
            wh = np.matmul(w, multiple_system(w.copy(), a.copy())) # obtem h que satisfaca wh = a
            err = np.subtract(a, wh) # A - WH

            # Classification
            for j in range(err.shape[1]): # imagens
                e_j = math.sqrt((np.sum(pow(err[:,j],2)))) # norma euclidiana da coluna
                if(digit == 0 or e_j < classification_err[j]):
                    classification[j] = digit
                    classification_err[j] = e_j
        elapsed_time = time.time() - start
        # Calculo da taxa de acertos
        if(args.d): print("Loaded: dados_mnist/test_index.txt")
        index = np.loadtxt("dados_mnist/test_index.txt")
        taxa = {"acerto": 0, "erro": 0}
        for c in range(args.n_test):
            if (classification[c] == index[c]): taxa["acerto"] += 1
            else:                               taxa["erro"]   += 1
        r.write(str(taxa))
        r.write("\nPrecisao de " + str(100*taxa["acerto"]/args.n_test) + "%")
        r.write("\nTempo de Classificacao: " + str(elapsed_time) + "s\n")

        # Exporta dados da classificacao para cada digito
        if(args.d):
            t = open("output/C_" + str(ndig) + "_" + str(args.n_test) + "_" + str(p) + ".txt", "w")
            for i in classification: t.write(str(int(i))+"\n")