#Semana 7 tarea Beltrán

class Coche:
    # # Paso 1: Constructor (__init__) - Inicializamos los atributos del objeto
    def __init__(self, marca, modelo, año):
        self.marca = marca  # Asignamos la marca del coche
        self.modelo = modelo  # Asignamos el modelo del coche
        self.año = año  # Asignamos el año del coche
        print(f"El coche {self.año} {self.marca} {self.modelo} ha sido creado.")  # Mensaje de creación

    # # Paso 2: Destructor (__del__) - Limpiamos o cerramos recursos cuando el objeto es destruido
    def __del__(self):
        print(f"El coche {self.año} {self.marca} {self.modelo} está siendo destruido.")  # Mensaje de destrucción


# # Paso 3: Crear un objeto de la clase Coche con la marca Renault
coche1 = Coche("Renault", "Clio", 2022)  # Asignamos los valores de marca, modelo y año

# # Paso 4: El destructor se activará cuando el objeto sea destruido
del coche1  # Destruimos el objeto explícitamente, lo que activa el destructor
