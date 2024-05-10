# 2. Usando el concepto y funciones de listas, realizar un programa con las siguientes características
"""
Reglas:
- Crear una lista con 10 valores random o aleatorios (Pista: Usar el método
append y for)
- Llenar otra lista con sus cubos.
- Llenar una lista nueva con sus cuadrados.
- Mostrar de manera inversa la suma de ambas listas creadas.
"""

import random    #Se importo módulo 'random' para obtener números aleatorios
enteros = []
cubos = []
cuadrados = []

for num_aleatorio in range(1, 11):
    num_aleatorio = random.randint(1, 10)   # Se emplea la función random.randint(1,11) para
    enteros.append(num_aleatorio)                 # obtener 10 números aleatorios entre 1 y 11.
    cubos.append(pow(num_aleatorio, 3))
    cuadrados.append(pow(num_aleatorio, 2))

print(f"\nLa lista de los números enteros aleatorios es: {enteros}"
      f"\nLa lista de los cubos de los números enteros aleatorios es: {cubos}"
      f"\nLa lista de los cuadrados de los números enteros aleatorios es: {cuadrados}")

suma = cubos + cuadrados
suma.reverse()
print(f"\nLa inversa de la suma de la lista 'cubos' y 'cuadrados' es: {suma}")
