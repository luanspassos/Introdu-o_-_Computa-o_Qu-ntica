"""Exercício 2: Utilizando a linguagem Python, encontre o valor da expressão abaixo.

           i**15

Para este cálculo, siga os seguintes passos:

a) Faça o cálculo das expressões: i**2, i**3, i**4, i**5,...

b) Analise estes valores e encontre o padrão da operação

c) Implemente este padrão, tendo como entrada a potência do número. """

import math
import numpy as np

i = complex(0, 1)
print("O valor de i elevado a 15 é:", i**15)

def i_pow(n):
    if n%4==0:
        return 1
    if n%4==1:
        return i
    if n%4==2:
        return -1
    if n%4==3:
        return -i
print("O valor de i elevado a 15 é:", i_pow(15))
