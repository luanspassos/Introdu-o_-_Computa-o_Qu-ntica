"""Exercício 5: Utilize a linguagem Python e comprove as seguintes propriedades, pelo cálculo de
cada lado da igualdade. Considere que o usuário fornecerá os números complexos"""

import math
import numpy as np

def complexo_para_par_ordenado(c):
    return (c.real, c.imag)

def soma_complexos(c1, c2):
    a1, b1 = complexo_para_par_ordenado(c1)
    a2, b2 = complexo_para_par_ordenado(c2)
    return complex(a1 + a2, b1 + b2)

def multiplicacao_complexos(c1, c2):
    a1, b1 = complexo_para_par_ordenado(c1)
    a2, b2 = complexo_para_par_ordenado(c2)
    return complex(a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)

def comutatividade(c1, c2):
    soma_1 = soma_complexos(c1, c2)
    soma_2 = soma_complexos(c2, c1)
    mult_1 = multiplicacao_complexos(c1, c2)
    mult_2 = multiplicacao_complexos(c2, c1)
    return soma_1 == soma_2, mult_1 == mult_2

def associatividade(c1, c2, c3):
    soma_1 = soma_complexos(soma_complexos(c1, c2), c3)
    soma_2 = soma_complexos(c1, soma_complexos(c2, c3))
    mult_1 = multiplicacao_complexos(multiplicacao_complexos(c1, c2), c3)
    mult_2 = multiplicacao_complexos(c1, multiplicacao_complexos(c2, c3))
    return soma_1 == soma_2, mult_1 == mult_2

def distributividade(c1, c2, c3):
    esquerda = multiplicacao_complexos(c1, soma_complexos(c2, c3))
    direita = soma_complexos(multiplicacao_complexos(c1, c2), multiplicacao_complexos(c1, c3))
    return esquerda == direita

real1 = float(input("Digite a parte real do primeiro número complexo: "))
imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
c1 = complex(real1, imag1)

real2 = float(input("Digite a parte real do segundo número complexo: "))
imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
c2 = complex(real2, imag2)

real3 = float(input("Digite a parte real do terceiro número complexo: "))
imag3 = float(input("Digite a parte imaginária do terceiro número complexo: "))
c3 = complex(real3, imag3)

comut_soma, comut_mult = comutatividade(c1, c2)
ass_soma, ass_mult = associatividade(c1, c2, c3)
distrib = distributividade(c1, c2, c3)

print("Comutatividade na soma:", comut_soma)
print("Comutatividade na multiplicação:", comut_mult)
print("Associatividade na soma:", ass_soma)
print("Associatividade na multiplicação:", ass_mult)
print("Distributividade:", distrib)

print("Comutatividade na multiplicação:", comut_mult)
print("Associatividade na soma:", ass_soma)
print("Associatividade na multiplicação:", ass_mult)
print("Distributividade:", distrib)
``
