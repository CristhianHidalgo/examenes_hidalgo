
def funcionD(funcionP):
    def funcionI(*args, **kwargs):
        print("Se ejecutará la operación, cuyo resultado es: ")
        funcionP(*args, **kwargs)
        print("La operación ha terminado correctamente\n")
    return funcionI


@funcionD
def multiplicacion(a, b, c, d):
    resultado = a * b * c * d
    print(resultado)


multiplicacion(a=5, b=8, c=7, d=10)
multiplicacion(a=12, b=10, c=6, d=2)
multiplicacion(1, 3, 5, 7)
