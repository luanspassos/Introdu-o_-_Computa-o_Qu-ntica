"""Exercício 15: Utilizando a linguagem Python, escreva três funções que realizem as operações

de adição, inversa e multiplicação escalar para C, considerando que e as respectivas

matrizes serão fornecidas pelo usuário.
    """
import numpy as np

def soma_vetores(vetor1, vetor2):
    return vetor1 + vetor2

def inverso_vetor(vetor):
    return -vetor

def mult_escalar(vetor, escalar):
    return escalar * vetor

n = int(input("Digite o tamanho dos vetores: "))
vetor1 = np.array([complex(input(f"Digite o elemento {i+1} do vetor 1 (formato a+bj): ")) for i in range(n)])
vetor2 = np.array([complex(input(f"Digite o elemento {i+1} do vetor 2 (formato a+bj): ")) for i in range(n)])
num_complexo_str = input("Digite o escalar complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
escalar=complex(parte_real,parte_imaginaria)

resultado_soma = soma_vetores(vetor1, vetor2)
resultado_inverso = inverso_vetor(vetor1)
resultado_mult_escalar = mult_escalar(vetor1, escalar)

print("Resultado da soma:", resultado_soma)
print("Resultado da inversão do vetor 1:", resultado_inverso)
print("Resultado da multiplicação escalar do vetor 1:", resultado_mult_escalar)
