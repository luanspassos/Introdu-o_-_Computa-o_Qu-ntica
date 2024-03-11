"""Exercício 16: Implemente em Python uma função que encontre a transposta, conjugada e

dagger de uma matriz complexa fornecida pelo usuário.
    """
import numpy as np


def encontrar_transposta_conjugada_dagger(matriz):
    transposta = np.transpose(matriz)
    conjugada = np.conjugate(matriz)
    dagger = np.conjugate(transposta)
    return transposta, conjugada, dagger


n_linhas = int(input("Digite o número de linhas da matriz: "))
n_colunas = int(input("Digite o número de colunas da matriz: "))

matriz_complexa = np.array([[complex(input(
    f"Digite o elemento ({i+1},{j+1}) da matriz (formato a+bj): ")) for j in range(n_colunas)] for i in range(n_linhas)])
transposta, conjugada, dagger = encontrar_transposta_conjugada_dagger(
    matriz_complexa)
print("\nMatriz Original:")
print(matriz_complexa)

print("\nTransposta:")
print(transposta)

print("\nConjugada:")
print(conjugada)

print("\nDagger:")
print(dagger)
