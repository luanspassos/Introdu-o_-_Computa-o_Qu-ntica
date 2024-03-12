"""Exercício 21: Implemente em Python uma função que forneça o produto tensorial de duas

matrizes complexas fornecidas pelo usuário.
    """
import numpy as np
n_linhas1 = int(input("Digite o número de linhas da primeira matriz: "))
n_colunas1 = int(input("Digite o número de colunas da primeira matriz: "))
n_linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
n_colunas2 = int(input("Digite o número de colunas da segunda matriz: "))
matriz1 = np.array([[complex(input(
    f"Digite o elemento ({i+1},{j+1}) da primeira matriz (formato a+bj): ")) for j in range(n_colunas1)] for i in range(n_linhas1)])
matriz2 = np.array([[complex(input(
    f"Digite o elemento ({i+1},{j+1}) da segunda matriz (formato a+bj): ")) for j in range(n_colunas2)] for i in range(n_linhas2)])
resultado = np.kron(matriz1, matriz2)
print("\nProduto Tensorial:")
print(resultado)
