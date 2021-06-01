import math

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return int(input("Entrada {}: ".format(label)))

# Calcula o Delta através dos valores númericos a, b, c e por meio deste
# retorna uma resposta com a quantidade de raízes reais
def Bhaskara(a, b, c):
    delta = (b**2) - (4*a*c)

    if delta >= 0:
        raizes = (-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)
        raizesEmOrdem = tuple(sorted(raizes))

        if delta > 0:
            return "as raízes da equação são {} e {}".format(raizesEmOrdem[0], raizesEmOrdem[1])
        else:
            return "a raiz desta equação é {}".format(raizes[0])
    else:
        return "esta equação não possui raízes reais"


entradas = PegarEntrada("A"), PegarEntrada("B"), PegarEntrada("C")
print(Bhaskara(entradas[0], entradas[1], entradas[2]))