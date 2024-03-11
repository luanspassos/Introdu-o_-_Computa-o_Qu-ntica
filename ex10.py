"""Exercício 10: Implemente em Python uma função de conversão de coordenadas cartesianas

para coordenadas polares.
    """

import cmath

num_complexo_str = input("Digite um número complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
z=complex(parte_real,parte_imaginaria)
soma1 = abs(z)
angulo1 = (cmath.phase(z) / cmath.pi) * 180
print("A representação em coordenadas polares é ({:.2f},{:.2f})".format(soma1,angulo1))
