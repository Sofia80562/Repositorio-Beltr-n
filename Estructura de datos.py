#Tarea Semana 9 Beltrán

# Clase Producto que representa un artículo en el inventario
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Constructor que inicializa un producto con ID, nombre, cantidad y precio
        self.id_producto = id_producto  # ID único
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener valores de los atributos
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos para modificar los atributos de cantidad y precio
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    # Método especial para mostrar los datos del producto como una cadena
    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

# Clase Inventario que gestiona una lista de productos
class Inventario:
    def __init__(self):
        self.productos = []  # Lista de productos en el inventario

    # Método para agregar un producto, verificando que el ID sea único
    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: ID de producto ya existe.")
            return
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.get_id() != id_producto]
        print("Producto eliminado correctamente.")

    # Método para actualizar la cantidad o el precio de un producto por ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    # Método para buscar productos por nombre (coincidencias parciales incluidas)
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    # Método para mostrar todos los productos en el inventario
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

# Función que proporciona un menú interactivo en la consola
def menu():
    inventario = Inventario()  # Crear una instancia de Inventario
    while True:
        # Mostrar las opciones del menú
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":  # Agregar producto
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":  # Eliminar producto
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":  # Actualizar producto
            id_producto = input("ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            nuevo_precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":  # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":  # Mostrar inventario completo
            inventario.mostrar_inventario()

        elif opcion == "6":  # Salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Verificar si el script se ejecuta directamente y llamar al menú
if __name__ == "__main__":
    menu()
