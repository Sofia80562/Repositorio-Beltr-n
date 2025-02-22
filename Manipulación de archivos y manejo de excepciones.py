#Semana 10: Manipulación de archivos y manejo de excepciones_Beltrán

import os

# Clase Producto: Representa un producto en el inventario
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = precio  # Precio por unidad del producto

    # Método para representar el producto como una cadena de texto
    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

# Clase Inventario: Gestiona la carga, guardado y modificación de los productos
class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo  # Nombre del archivo donde se guarda el inventario
        self.productos = self.cargar_inventario()  # Carga los productos desde el archivo (si existe)

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        productos = []  # Lista donde almacenaremos los productos cargados
        if os.path.exists(self.archivo):  # Verificamos si el archivo existe
            try:
                with open(self.archivo, 'r') as file:  # Intentamos abrir el archivo en modo lectura
                    lineas = file.readlines()  # Leemos todas las líneas del archivo
                    for linea in lineas:
                        datos = linea.strip().split(',')  # Dividimos la línea en partes (nombre, cantidad, precio)
                        if len(datos) == 3:  # Aseguramos que la línea contiene 3 valores
                            nombre, cantidad, precio = datos  # Asignamos los valores a las variables correspondientes
                            productos.append(Producto(nombre, int(cantidad), float(precio)))  # Añadimos el producto a la lista
            except FileNotFoundError:
                print(f"El archivo {self.archivo} no fue encontrado.")  # Si no se encuentra el archivo
            except PermissionError:
                print(f"Permiso denegado para leer el archivo {self.archivo}.")  # Si no se tienen permisos para leer
            except Exception as e:
                print(f"Ocurrió un error al leer el archivo: {e}")  # Si ocurre cualquier otro error
        else:
            print(f"El archivo {self.archivo} no existe, se creará uno nuevo.")  # Si el archivo no existe
        return productos  # Devolvemos la lista de productos cargados

    def guardar_inventario(self):
        """Guarda el inventario actual en el archivo."""
        try:
            with open(self.archivo, 'w') as file:  # Abrimos el archivo en modo escritura
                for producto in self.productos:  # Iteramos sobre todos los productos del inventario
                    file.write(f"{producto}\n")  # Escribimos la representación de cada producto en el archivo
            print("Inventario guardado exitosamente.")  # Mensaje de éxito al guardar
        except PermissionError:
            print(f"Permiso denegado para escribir en el archivo {self.archivo}.")  # Si no se tienen permisos para escribir
        except Exception as e:
            print(f"Ocurrió un error al guardar el inventario: {e}")  # Si ocurre cualquier otro error

    def agregar_producto(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario o actualiza uno existente."""
        # Comprobamos si el producto ya existe en el inventario
        for producto in self.productos:
            if producto.nombre == nombre:  # Si el nombre coincide con algún producto existente
                producto.cantidad += cantidad  # Aumentamos la cantidad del producto
                print(f"Producto '{nombre}' actualizado.")  # Mensaje de actualización
                self.guardar_inventario()  # Guardamos el inventario actualizado
                return
        # Si el producto no existe, lo agregamos como nuevo
        self.productos.append(Producto(nombre, cantidad, precio))  # Añadimos el nuevo producto
        print(f"Producto '{nombre}' agregado al inventario.")  # Mensaje de éxito
        self.guardar_inventario()  # Guardamos el inventario actualizado

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        for producto in self.productos:
            if producto.nombre == nombre:  # Si el nombre coincide con algún producto
                self.productos.remove(producto)  # Eliminamos el producto de la lista
                print(f"Producto '{nombre}' eliminado del inventario.")  # Mensaje de eliminación
                self.guardar_inventario()  # Guardamos el inventario actualizado
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")  # Si el producto no existe

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:  # Si la lista de productos está vacía
            print("El inventario está vacío.")  # Mensaje de inventario vacío
        else:
            for producto in self.productos:  # Mostramos cada producto en el inventario
                print(f"Producto: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

# Función para mostrar el menú de opciones en el programa
def mostrar_menu():
    print("\nSistema de Gestión de Inventarios")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Mostrar Inventario")
    print("4. Salir")

# Función principal que ejecuta el sistema
def main():
    inventario = Inventario()  # Creamos una instancia de la clase Inventario

    while True:  # Bucle principal para mostrar el menú
        mostrar_menu()  # Mostramos el menú
        try:
            opcion = int(input("Selecciona una opción: "))  # Leemos la opción seleccionada por el usuario
            if opcion == 1:
                nombre = input("Nombre del producto: ")  # Leemos el nombre del producto
                cantidad = int(input("Cantidad: "))  # Leemos la cantidad
                precio = float(input("Precio: "))  # Leemos el precio
                inventario.agregar_producto(nombre, cantidad, precio)  # Llamamos al método para agregar el producto
            elif opcion == 2:
                nombre = input("Nombre del producto a eliminar: ")  # Leemos el nombre del producto a eliminar
                inventario.eliminar_producto(nombre)  # Llamamos al método para eliminar el producto
            elif opcion == 3:
                inventario.mostrar_inventario()  # Mostramos todos los productos en el inventario
            elif opcion == 4:
                print("Saliendo del sistema...")  # Mensaje de salida
                break  # Salimos del bucle y terminamos el programa
            else:
                print("Opción no válida, por favor ingresa una opción correcta.")  # Si se ha ingresado una opción inválida
        except ValueError:
            print("Por favor ingresa un valor válido.")  # Si el usuario ha ingresado un valor no numérico
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")  # Si ha ocurrido un error inesperado

# Punto de entrada al programa creado
if __name__ == "__main__":
    main()  # Llamamos a la función principal para iniciar el programa :D

