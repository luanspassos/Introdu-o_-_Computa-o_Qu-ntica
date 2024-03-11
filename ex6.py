"""Exercício 6: Utilizando a linguagem Python, com o número complexo informado pelo usuário,
calcule cada lado da expressão e verifique as propriedades informadas:
a)
| c1 || c2 | = | c1c2 |
b)
| c1 + c2 | ≤ | c1 | + | c2 |"""

import math

def modulo_complexo(c):
    return math.sqrt(c.real ** 2 + c.imag ** 2)

real1 = float(input("Digite a parte real do primeiro número complexo: "))
imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
c1 = complex(real1, imag1)

real2 = float(input("Digite a parte real do segundo número complexo: "))
imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
c2 = complex(real2, imag2)

lado_esquerdo_a = modulo_complexo(c1) * modulo_complexo(c2)
lado_direito_a = modulo_complexo(c1 * c2)
igualdade_a = abs(lado_esquerdo_a - lado_direito_a) < 1e-9

lado_esquerdo_b = modulo_complexo(c1 + c2)
lado_direito_b = modulo_complexo(c1) + modulo_complexo(c2)
desigualdade_b = lado_esquerdo_b <= lado_direito_b

print("Para a expressão a):")
print("|c1||c2| =", lado_esquerdo_a)
print("|c1c2|   =", lado_direito_a)
print("As expressões são iguais?", igualdade_a)

print("\nPara a expressão b):")
print("|c1 + c2|   =", lado_esquerdo_b)
print("|c1| + |c2| =", lado_direito_b)
print("A expressão é válida?", desigualdade_b)
