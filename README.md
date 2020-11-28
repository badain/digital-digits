# digital-digits
Classifica dígitos manuscritos utilizando fatoração QR\
Authors: Carlo Bellinati & Rafael Badain @ University of Sao Paulo

## training_MNIST.py
**Description**: treinamento baseado em fatoracao nao negativa para classificacao de digitos manuscritos utilizando a database MNIST\
**Dependencies**: *time, argparse, fatorização_nao_negativa*\
**Usage**: training_MNIST.py *ndig_treino* *p* *--t*\
**Positional arguments**:\
    *ndig_treino*   numero de imagens a ser utilizada para fatoracao\
    *P*             fator de componentes da decomposicao\
**Optional arguments**:\
    *--t, --times*  guarda o tempo de treinamento para cada digito em "output/train_times_ndig_treino_p.txt"\
**Post-Condition**: armazena as matrizes Wd decompostas para cada digito em "output/W_digito_ndig_treino_p.txt"

## training_MNIST_deluxe.py
**Description**: treinamento baseado em fatoracao nao negativa para classificacao de digitos manuscritos utilizando a database MNIST\
**Automatizado para**:\
    *ndig* 100, 1000, 4000 imagens\
    *p*    5, 10, 15\
**Dependencies**: time, argparse, math, nnmf.py\
**Usage**: training_MNIST_deluxe.py --t\
**Optional arguments**:\
    *--t, --times*  guarda o tempo de treinamento para cada digito em "output/train_times_ndig_treino_p.txt"\
**Post-Condition**: armazena as matrizes Wd decompostas para cada digito  em "output/W_digito_ndig_treino_p.txt"

## classify_MNIST.py
**Description**: classificacao de digitos manuscritos utilizando a database MNIST\
**Dependencies**: argparse, numpy, math, systems_qr.py\
**Usage**: classify_MNIST.py *ndig_treino* *n_test* *P* *--e*\
**Positional arguments**:\
    *ndig_treino*   numero de imagens usadas no treinamento\
    *n_test*        numero de imagens a ser utilizada para teste\
    *P*             fator de componentes da decomposicao\
**Optional arguments**:\
    *--e, --export* exporta os dados da classificacao de cada imagem em "output/C_ndig_treino_n_test_p.txt"\
**Post-Condition**: exibe a taxa de precisao do classificador, baseado no index "test_index.txt"

## classify_MNIST_deluxe.py
**Description**: classificacao de digitos manuscritos utilizando a database MNIST\
**Automatizado para**:\
    *ndig_treino* 100, 1000, 4000\
    *componentes* 5, 10, 15\
**Dependencies**: time, argparse, numpy, math, systems_qr.py\
**Usage**: classify_MNIST_deluxe.py *n_test* *--e*\
**Positional arguments**:\
    *n_test*        numero de imagens a ser utilizada para teste\
**Optional arguments**:\
    *--e, --export* exporta os dados da classificacao de cada imagem em "output/C_ndig_treino_n_test_p.txt"\
Post-Condition: armazena a taxa de precisao e o tempo do classificador em "output/classify_index_n_test.txt"

## Bibliotecas
### nnmf.py
**Description**: biblioteca de funcoes para implementacao da fatoracao nao negativa de matrizes\
**Dependencies**: numpy, math, systems_qr.py

### systems_qr.py
**Description**: biblioteca de funcoes para implementacao da fatoracao QR de matrizes\
**Dependencies**: numpy, math, rot_givens.py

### rot_givens.py
**Description**: biblioteca de funcoes para implementacao da rotacao de givens de matrizes\
**Dependencies**: numpy, math