
from random import randint
lista_normal = []
no_repetidos = []
lista_ordenada = []


def lista_aleatoria():
    while len(lista_normal) < 10:
        lista_normal.append(randint(1, 11))
    return lista_normal


def lista_no_repetidos(lista_normal):
    for num in lista_normal:
        if lista_normal.count(num) == 1:
            no_repetidos.append(num)
    return no_repetidos


def crear_lista_ordenada(no_repetidos):
    lista_ordenada = no_repetidos.copy()
    lista_ordenada.sort()
    return lista_ordenada.sort()


lista_aleatoria()
lista_no_repetidos(lista_normal)
crear_lista_ordenada(no_repetidos)

print(lista_normal)
print(no_repetidos)
print(lista_ordenada)
