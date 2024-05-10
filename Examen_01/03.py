# 3. Teniendo presente el uso y concepto de diccionarios en Python, realizar un
# programa con los siguientes requerimientos

"""
Reglas:
- Crear un diccionario con los keys de nombre, apellidos, edad y dni.
- Pedir por consola los valores para estos keys.
- Mostrar en pantalla sólo los values del diccionario y aumentar en 10 solo la edad
- Agregar un key adicional con el nombre de “profesión” y un valor para este key
nuevo.
- Eliminar el key dni y mostrar el nuevo diccionario.
"""

usuario = {"nombre": "", "apellido": "", "edad": "", "dni": ""}

usuario["nombre"] = input("\nIngresa el nombre del usuario: ")
usuario["apellido"] = input("Ingresa el apellido del usuario: ")
usuario["edad"] = int(input("Ingresa la edad del usuario: "))
usuario["dni"] = input("Ingresa el dni del usuario: ")

print(f"\nLos valores del diccionario son: {list(usuario.values())}")
usuario["edad"] = usuario["edad"] + 10

usuario["profesion"] = "Ingeniería de Minas"

del usuario["dni"]
print(f"\nEl diccionario actualizado es: {usuario}")