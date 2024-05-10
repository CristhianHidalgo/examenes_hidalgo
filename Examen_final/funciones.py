from random import randint
from math import sqrt

lista = []
lista_raiz = []


def crear_fichiero():
    file = open("my_files/notas.txt", "a+")
    file.close()


def crear_lista():
    cantidad = int(input("Ingrese la cantidad de datos en la lista: "))

    while len(lista) < cantidad:
        lista.append(randint(1, 11))

    file = open("my_files/notas.txt", "w")
    file.writelines(str(lista))
    file = open("my_files/notas.txt", "r")
    print(file.read())
    file.close()


def crear_raiz():
    for i in lista:
        raiz = sqrt(i)
        lista_raiz.append(round(raiz, 2))

    file = open("my_files/notas.txt", "a+")
    file.writelines(str(lista_raiz))
    file = open("my_files/notas.txt", "r")
    print(file.read())
    file.close()
