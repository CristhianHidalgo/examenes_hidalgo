"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad, saldo y de nacionalidad peruana (use el manejo de errores para el
tipo de dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo instanciar la clase 2 veces, mostrar por
pantalla dicha edad actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
"""

from datetime import datetime, date

class Persona:
    def __init__(self, nombre, edad, saldo, nacionalidad):
        self.nombre = nombre
        self.edad = self.validar_edad(edad)
        self.saldo = saldo
        self.nacionalidad = self.validad_nacionalidad(nacionalidad)

    def validar_edad(self, edad):
        try:
            edad = int(edad)
            if edad < 0:
                raise ValueError("La edad no puese ser negativa")
            return edad
        except ValueError:
            print("Error: La edad debe ser un número entero: ")
            return 0

    def validad_nacionalidad(self, nacionalidad):
        if nacionalidad.lower() != "peruana":
            print("Error: La nacinalidad debe ser peruana")
            return 'Peruana'
        return nacionalidad.capitalize()

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.edad = self.validar_edad(input("Ingrese si edad: "))

    def cumpleaños(self):
        self.edad = self.edad + 1
        return self.edad

    def fecha_registro(self):
        self.fecha = date.today()
        self.tiempo = datetime.now()
        self.hora = self.tiempo.hour
        self.minuto = self.tiempo.minute

        print(f"El registo fue el día {persona_1.fecha} a las {persona_1.hora} horas con {persona_1.minuto} minutos")


persona_1 = Persona()
persona_1.ingresar_datos()
persona_1.cumpleaños()
persona_1.cumpleaños()
print(f"{persona_1.nombre} tiene actualmente {persona_1.edad}")
persona_1.fecha_registro()

persona_2 = Persona()
persona_2.ingresar_datos()
persona_2.cumpleaños()
persona_2.cumpleaños()
persona_2.cumpleaños()
persona_2.cumpleaños()
print(f"{persona_2.nombre} tiene actualmente {persona_2.edad}")
persona_2.fecha_registro()