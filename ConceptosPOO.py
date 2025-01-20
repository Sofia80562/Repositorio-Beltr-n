#Semana 6 TAREA BELTRAN

# Definición de la clase base "Vehículo"
class Vehiculo:
    # Atributo de la clase Vehículo
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo público
        self.__modelo = modelo  # Atributo privado (Encapsulación)

    # Método para obtener el modelo (Encapsulación)
    def obtener_modelo(self):
        return self.__modelo

    # Método para mostrar información del vehículo
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}, Modelo: {self.__modelo}")

# Clase derivada "Coche", que hereda de "Vehiculo"
class Coche(Vehiculo):
    # Constructor de la clase Coche
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.num_puertas = num_puertas  # Atributo específico de la clase Coche

    # Método sobrescrito (Polimorfismo) para mostrar información
    def mostrar_informacion(self):
        # Llamada al método de la clase base y agregamos información específica del coche
        print(f"Marca: {self.marca}, Modelo: {self.obtener_modelo()}, Puertas: {self.num_puertas}")

# Clase derivada "Motocicleta", que hereda de "Vehiculo"
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)  # Llamada al constructor de la clase base
        self.tipo_motor = tipo_motor  # Atributo específico de la clase Motocicleta

    # Método sobrescrito (Polimorfismo) para mostrar información
    def mostrar_informacion(self):
        # Llamada al método de la clase base y agregamos información específica de la motocicleta
        print(f"Marca: {self.marca}, Modelo: {self.obtener_modelo()}, Tipo de Motor: {self.tipo_motor}")

# Creación de objetos de las clases Coche y Motocicleta
vehiculo1 = Coche("Renault", "Clio", 5)  # Cambié la marca a Renault
vehiculo2 = Motocicleta("Yamaha", "YZF-R3", "Deportiva")

# Llamada a los métodos para mostrar la información de los vehículos
print("Información del Coche:")
vehiculo1.mostrar_informacion()

print("\nInformación de la Motocicleta:")
vehiculo2.mostrar_informacion()

# Ejemplo de polimorfismo con una función que puede manejar diferentes tipos de vehículos
def mostrar_detalles(vehiculo):
    vehiculo.mostrar_informacion()

# Llamada a la función con diferentes objetos (polimorfismo)
print("\nDetalles desde función de polimorfismo:")
mostrar_detalles(vehiculo1)
mostrar_detalles(vehiculo2)
