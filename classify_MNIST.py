#####################################################################
# Description: classificacao de digitos manuscritos utilizando
#              a database MNIST
# Dependencies: time, argparse, numpy, math, systems_qr.py
# Usage: classify_MNIST.py ndig_treino n_test P --e
# Positional arguments:
#     ndig_treino   numero de imagens usadas no treinamento
#     n_test        numero de imagens a ser utilizada para teste
#     P             fator de componentes da decomposicao
# Optional arguments:
#     -h, --help    shows help message and exit
#     --e, --export exporta os dados da classificacao de cada imagem
# Post-Condition: exibe a taxa de precisao do classificador
#                 baseado no index "test_index.txt"
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import numpy as np
import math
import argparse
from systems_qr import multiple_system

# Argument Parsing
parser = argparse.ArgumentParser(description='Decompoe um conjunto de imagens em classificadores, baseado na fatoracao nao negativa')
parser.add_argument('n_test', type=int, metavar='n_test', help='numero de imagens a ser utilizada para teste')
parser.add_argument('ndig_treino', type=int, metavar='ndig_treino', help='numero de imagens usadas no treinamento')
parser.add_argument('p', type=int, metavar='P', help='fator de componentes da decomposicao')
parser.add_argument('--e', '--export', default=False, action='store_true', help='exporta os dados da classificacao de cada imagem')
args = parser.parse_args()

# Input Reading
a = np.loadtxt("dados_mnist/test_images.txt", usecols=range(args.n_test)) / 255
if(args.e): print("Loaded: dados_mnist/test_images.txt "+str(a.shape))

# For each image, Wd*H = A
classification  = np.zeros(args.n_test)
classification_err = np.zeros(args.n_test)

for digit in range(10): # Digitos a serem testados
    if(args.e): print("Loaded: output/W_"+str(digit)+"_"+str(args.ndig_treino)+"_"+str(args.p)+".txt"+str(a.shape))

    # Solving A - WH
    w = np.loadtxt("output/W_"+str(digit)+"_"+str(args.ndig_treino)+"_"+str(args.p)+".txt")
    wh = np.matmul(w, multiple_system(w.copy(), a.copy())) # obtem h que satisfaca wh = a
    err = np.subtract(a, wh) # A - WH

    # Classification
    for j in range(err.shape[1]): # imagens
        e_j = math.sqrt((np.sum(pow(err[:,j],2)))) # norma euclidiana da coluna
        if(digit == 0 or e_j < classification_err[j]):
            classification[j] = digit
            classification_err[j] = e_j
    
# Calculo da taxa de acertos
if(args.e): print("Loaded: dados_mnist/test_index.txt")
index = np.loadtxt("dados_mnist/test_index.txt")
td = [0]*10     # total de de cada dígito no gabarito
cd = [0]*10     # total de cada dígito nas classificações corretas
taxa = {"acerto": 0, "erro": 0}
for c in range(args.n_test):
    td[int(index[c])] += 1
    if (classification[c] == index[c]):
        taxa["acerto"] += 1
        cd[int(classification[c])] += 1
    else:                               taxa["erro"]   += 1
print(taxa)
print("Precisão de " + str(100*taxa["acerto"]/args.n_test) + "%")
for digit in range(10):
    print("   d" + str(digit) +": Precisao de " + str(100*cd[digit]/td[digit]) + "%. (" + str(cd[digit]) + " corretos de" + str(td[digit]) + ")")

# Exporta dados da classificacao para cada digito
if(args.e):
    t = open("output/C_" + str(args.ndig_treino) + "_" + str(args.n_test) + "_" + str(args.p) + ".txt", "w")
    for i in classification: t.write(str(int(i))+"\n")