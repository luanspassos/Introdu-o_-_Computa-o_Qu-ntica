"""
Exercício 4: Verifique que o número complexo
−1 + i
É solução do polinômio
x2 + 2x + 2 = 0 
Utilize a linguagem Python
  """

import math
import numpy as np

z = complex(-1, 1)
polinomio = lambda x: x**2 + 2*x + 2

resultado = polinomio(z)
if resultado == 0:
    print("O número complexo (-1 + i) é uma solução do polinômio.")
else:
    print("O número complexo (-1 + i) não é uma solução do polinômio.")
