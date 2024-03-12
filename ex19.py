"""Exercício 19: Repita o exercício 17 para verificar se a matriz é hermitiana
    """
import numpy as np
def verificar_hermitiana(matriz):
    return np.allclose(matriz, matriz.conj().T)
n_linhas = int(input("Digite o número de linhas da matriz: "))
n_colunas = int(input("Digite o número de colunas da matriz: "))
matriz = np.array([[complex(input(f"Digite o elemento ({i+1},{j+1}) da matriz (formato a+bj): ")) for j in range(n_colunas)] for i in range(n_linhas)])
if matriz.shape[0] != matriz.shape[1]:
    print("A matriz não é quadrada e, portanto, não pode ser Hermitiana.")
else:
    if verificar_hermitiana(matriz):
        print("A matriz é Hermitiana.")
    else:
        print("A matriz não é Hermitiana.")
