""" Exercício 5: Utilize a linguagem Python e comprove as seguintes propriedades, pelo cálculo de
cada lado da igualdade. Considere que o usuário fornecerá os números complexos"""

import math
import numpy as np

def complexo_para_par_ordenado(c):
    return (c.real, c.imag)

def soma_complexos(c1, c2):
    return complexo_para_par_ordenado(c1) + complexo_para_par_ordenado(c2)

def multiplicacao_complexos(c1, c2):
    a1, b1 = complexo_para_par_ordenado(c1)
    a2, b2 = complexo_para_par_ordenado(c2)
    return (a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)

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

c1 = complex(input("Digite a parte real do primeiro número complexo: "), input("Digite a parte imaginária do primeiro número complexo: "))
c2 = complex(input("Digite a parte real do segundo número complexo: "), input("Digite a parte imaginária do segundo número complexo: "))
c3 = complex(input("Digite a parte real do terceiro número complexo: "), input("Digite a parte imaginária do terceiro número complexo: "))

comut_soma, comut_mult = comutatividade(c1, c2)
ass_soma, ass_mult = associatividade(c1, c2, c3)
distrib = distributividade(c1, c2, c3)

print("Comutatividade na soma:", comut_soma)
print("Comutatividade na multiplicação:", comut_mult)
print("Associatividade na soma:", ass_soma)
print("Associatividade na multiplicação:", ass_mult)
print("Distributividade:", distrib)
``
