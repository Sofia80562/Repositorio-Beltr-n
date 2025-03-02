#Tarea semana 11: Fundamentos de colecciones_Beltrán

import json

# Clase que representa un producto en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener los valores de los atributos
    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    # Métodos para actualizar los atributos del producto:
    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    # Representación en forma de cadena del objeto producto:
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase que maneja el inventario de productos:
class Inventario:
    def __init__(self):
        # Inicializa el inventario como un diccionario vacío
        self.inventario = {}

    # Método para agregar un producto al inventario:
    def agregar_producto(self, producto):
        self.inventario[producto.obtener_id()] = producto

    # Método para eliminar un producto del inventario mediante su ID:
    def eliminar_producto(self, id_producto):
        if id_producto in self.inventario:
            del self.inventario[id_producto]
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Método para actualizar la cantidad y/o precio de un producto:
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.inventario:
            producto = self.inventario[id_producto]
            if cantidad is not None:
                producto.actualizar_cantidad(cantidad)
            if precio is not None:
                producto.actualizar_precio(precio)
        else:
            print(f"Producto con ID {id_producto} no encontrado.")

    # Método para buscar productos por su nombre (parcial):
    def buscar_producto(self, nombre):
        productos_encontrados = [producto for producto in self.inventario.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return productos_encontrados

    # Método para mostrar todos los productos en el inventario:
    def mostrar_inventario(self):
        for producto in self.inventario.values():
            print(producto)

    # Método para guardar el inventario en un archivo denominado "JSON"
    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            # Serializa el inventario y guarda en el archivo
            json.dump({id_producto: vars(producto) for id_producto, producto in self.inventario.items()}, f)

    # Método para cargar el inventario desde el archivo "JSON"
    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                # Deserializa los datos del archivo y crea los objetos Producto
                data = json.load(f)
                for id_producto, producto_data in data.items():
                    producto = Producto(producto_data['id_producto'], producto_data['nombre'], producto_data['cantidad'], producto_data['precio'])
                    self.inventario[id_producto] = producto
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado.")

# Función que muestra el menú y permite al usuario interactuar con el sistema:
def menu():
    inventario = Inventario()
    archivo = "inventario.json"  # Archivo donde se guardará el inventario
    inventario.cargar_inventario(archivo)  # Cargar inventario desde el archivo al inicio

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Agregar un nuevo producto al inventario
            id_producto = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            # Eliminar un producto del inventario por su ID
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar un producto existente
            id_producto = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (dejar en blanco si no desea cambiarla): ")
            cantidad = int(cantidad) if cantidad else None
            precio = input("Ingrese nuevo precio (dejar en blanco si no desea cambiarlo): ")
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            # Buscar productos por nombre
            nombre = input("Ingrese nombre del producto a buscar: ")
            productos = inventario.buscar_producto(nombre)
            for producto in productos:
                print(producto)

        elif opcion == "5":
            # Mostrar todos los productos en el inventario
            inventario.mostrar_inventario()

        elif opcion == "6":
            # Guardar el inventario en el archivo y salir
            inventario.guardar_inventario(archivo)
            print("Inventario guardado.")
            break

        else:
            # Manejar opción inválida
            print("Opción inválida, intente de nuevo.")

# Llamada al menú para ejecutar el programa:
if __name__ == "__main__":
    menu()
