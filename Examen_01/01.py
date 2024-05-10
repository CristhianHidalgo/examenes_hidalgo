# 1. Usando los tipos de datos y sus conversiones realizar lo siguiente
"""
Reglas:
- Pedir por consola nombre, apellido y edad de un usuario. Mostrar en consola el
nombre completo del trabajador
- Edad tiene que ser tipo entero, para esto apoyarse de la conversión de datos
- Identificar los tipos de datos ingresados y mostrarlos en pantalla.
- Pedir los nombres y edades para dos trabajadores y finalmente
agregarlos a una lista. Mostrar la suma de las edades de los
trabajadores localizándolos por la posición en la lista.
"""

nombre = input("\nIngrese el nombre del usuario: ")
apellido = input("Ingrese el apellido del usuario: ")
edad = int(input("Ingrese la edad del usuario: "))
print(f"El nombre completo del usuario es: {nombre} {apellido}")

print(f"\nEl tipo de dato de la variable 'nombre' es: {type(nombre)}"
      f"\nEl tipo de dato de la variable 'apellido' es: {type(apellido)}"
      f"\nEl tipo de dato de la variable 'edad' es: {type(edad)}")

nombre_1 = input("\nIngrese el nombre del primer trabajador: ")
edad_1 = int(input("Ingrese la edad del primer trabajador: "))
nombre_2 = input("Ingrese el nombre del segundo trabajador: ")
edad_2 = int(input("Ingrese la edad del segundo trabajador: "))

trabajadores = [nombre_1, edad_1, nombre_2, edad_2]
suma_edad = trabajadores[1] + trabajadores[3]
print(f"\nLa suma de las edades de los dos trabjadores es: {suma_edad}")
