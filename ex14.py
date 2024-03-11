"""Exercício 14: Implemente em Python a transformação de Möebis com a = d = 0 e b = c = 1
    """
import cmath
def operador(a,b,c,d,x):
    return (a*x+b)/(c*x+d)
num_complexo_str = input("Digite o número complexo a+bj no formato (a, b): ")
num_complexo_str = num_complexo_str.replace('(', '').replace(')', '')
partes = num_complexo_str.split(',')

if len(partes) != 2:
    print("Número complexo inválido. Certifique-se de que está no formato (a, b).")
else:
    parte_real = float(partes[0])
    parte_imaginaria = float(partes[1])
z=complex(parte_real,parte_imaginaria)
ans = operador(0,1,1,0,z)
print("Transformada de Moebius para a=d=0,b=c=1 : {:.2f}".format(ans))
