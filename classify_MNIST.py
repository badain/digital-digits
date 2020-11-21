#####################################################################
# Description: treinamento baseado em fatoracao nao negativa
#              para classificacao de digitos manuscritos utilizando
#              a database MNIST
# Dependencies: time, argparse
# Usage: classify_MNIST.py n_test
# Positional arguments:
#     n_test   numero de imagens a ser utilizada para teste
#     P        fator de componentes da decomposicao
# Optional arguments:
#     -h, --help    shows help message and exit
#     --t, --times  guarda o tempo de treinamento para cada digito
# Post-Condition: armazena as matrizes Wd decompostas para cada
#                 digito
#
# Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo
#####################################################################

# Dependencies
import numpy as np
import argparse
import time
from sistems_qr import multiple_sistem

# Argument Parsing
parser = argparse.ArgumentParser(description='Decompoe um conjunto de imagens em classificadores, baseado na fatoracao nao negativa')
parser.add_argument('n_test', type=int, metavar='n_test', help='numero de imagens a ser utilizada para teste')
parser.add_argument('p', type=int, metavar='P', help='fator de componentes da decomposicao')
parser.add_argument('--d', '--debug', default=False, action='store_true', help='debug mode')
parser.add_argument('--t', '--times', default=False, action='store_true', help='guarda o tempo de treinamento para cada digito')
args = parser.parse_args()

# Input Reading
a = np.loadtxt("dados_mnist/test_images.txt", usecols=range(args.n_test)) / 255
if(args.d): print(a.shape)

# For each image, Wd*H = A
classification  = np.zeros(args.n_test)
classification_err = np.zeros(args.n_test)

for d in range(10): #digitos
    w = np.loadtxt("output/W_"+str(d)+"_"+str(args.n_test)+"_"+str(args.p)+".txt")
    h = multiple_sistem(w, a)
    wh = np.matmul(w, h)
    err = np.subtract(a, wh) # A - WH
    if(args.d): print(str(d)+": "+str(err.shape))
    for j in range(err.shape[1]): #imagens
        e_j = np.sqrt((np.sum(pow(err[:,j],2))))
        if(d == 0 or e_j < classification_err[j]):
            classification[j] = d
            classification_err[j] = e_j
        if(args.d): print(str(j)+": "+str(e_j))
    if(args.d):
        print(classification_err)
        print(classification)
    
