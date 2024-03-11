"""Exercício 7: Utilizando a linguagem Python, com o número complexo informado pelo usuário,
calcule cada lado da expressão e verifique as propriedades informadas:
a)conjugado(c1) +conjugado( c2) = conjugado(c1 + c2)
b)conjugado(c1) xconjugado( c2) = conjugado(c1 x c2)"""

def conjugado(c):
    return complex(c.real, -c.imag)

real1 = float(input("Digite a parte real do primeiro número complexo: "))
imag1 = float(input("Digite a parte imaginária do primeiro número complexo: "))
c1 = complex(real1, imag1)

real2 = float(input("Digite a parte real do segundo número complexo: "))
imag2 = float(input("Digite a parte imaginária do segundo número complexo: "))
c2 = complex(real2, imag2)

# Calculando cada lado da expressão a)
lado_esquerdo_a = conjugado(c1) + conjugado(c2)
lado_direito_a = conjugado(c1 + c2)

# Calculando cada lado da expressão b)
lado_esquerdo_b = conjugado(c1) * conjugado(c2)
lado_direito_b = conjugado(c1 * c2)

# Verificando as propriedades
propriedade_a = lado_esquerdo_a == lado_direito_a
propriedade_b = lado_esquerdo_b == lado_direito_b

# Imprimindo os resultados
print("Para a expressão a):")
print("Conjugado(c1) + Conjugado(c2) =", lado_esquerdo_a)
print("Conjugado(c1 + c2)           =", lado_direito_a)
print("A propriedade é válida?", propriedade_a)

print("\nPara a expressão b):")
print("Conjugado(c1) * Conjugado(c2) =", lado_esquerdo_b)
print("Conjugado(c1 * c2)           =", lado_direito_b)
print("A propriedade é válida?", propriedade_b)
