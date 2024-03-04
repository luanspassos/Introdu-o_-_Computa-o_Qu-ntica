"""Verifique que a equação abaixo não possui solução nos números reais. Faça essa

verificação utilizando Python.
x4 + 2x2 + 1 = 0  """

import math
import numpy as np

#seja a= x**2
#equacao = a**2 + 2*a + 1
a=1
b=2
c=1
delta = b**2 - 4*a*c

def f(a, b, delta):
   return   (-b+math.sqrt(delta))/2*a


def g(a,b,c):
   return   (-b-math.sqrt(b**2-4*a*c))/2*a

# Verificando se existem soluções reais
if (f(a, b, delta) < 0 and g(a, b, delta) < 0)  or delta<0:
    print("A equação não possui solução nos números reais.")
else:
    print("A equação possui solução nos números reais:")

