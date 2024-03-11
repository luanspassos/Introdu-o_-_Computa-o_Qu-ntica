"""Exercício 17: Implemente em Python uma função que realize o produto cartesiano de duas

matrizes complexas fornecidas pelo usuário.
    """
import numpy as np
def produto_cartesiano(matriz1, matriz2):
    m, n = matriz1.shape
    p, q = matriz2.shape
    resultado = np.zeros((m*p, n*q), dtype=np.complex128)
    for i in range(m):
        for j in range(n):
            resultado[i*p:(i+1)*p, j*q:(j+1)*q] = matriz1[i, j] * matriz2
    return resultado
n_linhas1 = int(input("Digite o número de linhas da primeira matriz: "))
n_colunas1 = int(input("Digite o número de colunas da primeira matriz: "))
n_linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
n_colunas2 = int(input("Digite o número de colunas da segunda matriz: "))

matriz1 = np.array([[complex(input(f"Digite o elemento ({i+1},{j+1}) da primeira matriz (formato a+bj): ")) for j in range(n_colunas1)] for i in range(n_linhas1)])
matriz2 = np.array([[complex(input(f"Digite o elemento ({i+1},{j+1}) da segunda matriz (formato a+bj): ")) for j in range(n_colunas2)] for i in range(n_linhas2)])

resultado = produto_cartesiano(matriz1, matriz2)

print("\nProduto Cartesiano:")
print(resultado)
