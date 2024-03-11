"""Exercício 9: Refaça o exercício anterior, mas desta vez usando a representação polar.
    """

import cmath
z1 = 2 - 1j
z2 = 1 + 1j
soma1 = abs(z1 + z2)
angulo1 = (cmath.phase(z1 + z2) / cmath.pi) * 180
soma2 = abs(z1 - z2)
angulo2 = (cmath.phase(z1 - z2) / cmath.pi) * 180
print("a) A representação em coordenadas polares (rho,theta) é ({:.2f},{:.2f})".format(soma1,angulo1))
print("b) A representação em coordenadas polares (rho,theta) é ({:.2f},{:.2f})".format(soma2,angulo2))
