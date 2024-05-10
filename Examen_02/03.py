"""
Escribir un programa para gestionar los errores en Python (3 ptos):
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente.
"""
def ingresar_datos():
    while True:
        try:
            dato_1 = float(input("Ingrese el primer dato: "))
            dato_2 = float(input("Ingrese el segundo dato: "))
            return dato_1, dato_2
        except ValueError:
            print("Error: Ingrese números validos (decimales)")

def dividir_cero(dato_1, dato_2):
    try:
            division = dato_1 / dato_2
            print(f"El resultado de la división es: {division: .2f}")
    except ZeroDivisionError:
            print("Error: No se puede dividir un número entre 0")

def evaluar_suma(dato_1, dato_2):
    if dato_1 + dato_2 < 0:
        print("Error: La suma es negativa")

def lista_error():
    lista = []
    while True:
        try:
            dato_ingresar = int(input("Ingrese un número para la lista (o 0 para terminar): "))
            if dato_ingresar == 0:
                break
            lista.append(dato_ingresar)
        except ValueError:
            print("Error: Ingrese un número entero")

    while True:
        try:
            indice = int(input("Ingresa el indice a buscar: "))
            print(f"El número buscado es: {lista[indice]}")
            break
        except IndexError:
            print("Error: El índice sobrepasa el rango de la lista")
        except ValueError:
            print(f"Error: Ingrese un número entero como índice")

#Función Principal:
def main():
    while True:
        dato_1, dato_2 = ingresar_datos()
        dividir_cero(dato_1, dato_2)
        evaluar_suma(dato_1, dato_2)
        lista_error()

        opcion_continuar = input(f"¿Desea continuar? (s/n): ")
        if opcion_continuar.lower() != "s":
            break

#if __name__ == "__main__":
main()
