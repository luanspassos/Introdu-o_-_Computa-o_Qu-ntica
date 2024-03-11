"""Exercício 8: Utilizando a linguagem Python, calcule graficamente as equações abaixo:
a) (2, -1) + (1,1)
b) (2, -1) - (1,1)"""

import numpy as np
import matplotlib.pyplot as plt
import math

z1 = np.array([2, -1])
z2 = np.array([1, 1])

soma = z1 + z2
subtracao = z1 - z2

plt.plot([0, z1[0]], [0, z1[1]], 'ro-', label='z1 = (2, -1)')
plt.plot([0, z2[0]], [0, z2[1]], 'bo-', label='z2 = (1, 1)')
plt.plot([0, soma[0]], [0, soma[1]], 'go-', label='Soma: z1 + z2')
plt.plot([0, subtracao[0]], [0, subtracao[1]], 'yo-', label='Subtração: z1 - z2')

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Operações com Números Complexos')
plt.legend()
plt.grid(True)
plt.axis('equal')

plt.show()
