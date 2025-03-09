#Semana 12_Tarea_Beltrán

# Clase para representar un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Los atributos del libro: título, autor (como tupla), categoría y ISBN.
        self.titulo = titulo
        self.autor = tuple(autor)  # El autor se almacena como una tupla (nombre, apellido, etc.)
        self.categoria = categoria
        self.isbn = isbn

    # Método para representar el libro como una cadena de texto
    def __str__(self):
        return f"{self.titulo} por {', '.join(self.autor)} - Categoría: {self.categoria}, ISBN: {self.isbn}"


# Clase para representar a un usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        # Atributos del usuario: nombre, ID de usuario y libros prestados
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los libros actualmente prestados

    # Método para representar al usuario como una cadena de texto
    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Clase para gestionar la biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para almacenar los libros con el ISBN como clave
        self.libros = {}
        # Diccionario para almacenar los usuarios con el ID de usuario como clave
        self.usuarios = {}

    # Método para añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro  # Guardamos el libro en el diccionario usando el ISBN como clave
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    # Método para quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            libro = self.libros.pop(isbn)  # Eliminamos el libro del diccionario usando su ISBN
            print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
        else:
            print("Libro no encontrado.")  # Si el libro no existe, mostramos un mensaje de error

    # Método para registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        self.usuarios[usuario.id_usuario] = usuario  # Guardamos al usuario en el diccionario usando su ID
        print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    # Método para dar de baja a un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]  # Eliminamos al usuario del diccionario usando su ID
            print(f"Usuario con ID '{id_usuario}' dado de baja.")
        else:
            print("Usuario no encontrado.")  # Si el usuario no existe, mostramos un mensaje de error

    # Método para prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print("Libro no encontrado.")  # Si el libro no está en la biblioteca, mostramos un mensaje de error
            return
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")  # Si el usuario no está registrado, mostramos un mensaje de error
            return

        libro = self.libros[isbn]  # Obtenemos el libro usando su ISBN
        usuario = self.usuarios[id_usuario]  # Obtenemos al usuario usando su ID
        usuario.libros_prestados.append(libro)  # Añadimos el libro a la lista de libros prestados del usuario
        print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")

    # Método para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")  # Si el usuario no está registrado, mostramos un mensaje de error
            return
        usuario = self.usuarios[id_usuario]  # Obtenemos al usuario usando su ID
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:  # Si el libro está en la lista de prestados del usuario
                usuario.libros_prestados.remove(libro)  # Lo eliminamos de la lista
                print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                return
        print("El libro no está en los libros prestados.")  # Si el libro no está prestado, mostramos un mensaje de error

    # Método para buscar libros por título, autor o categoría
    def buscar_libro(self, criterio, valor):
        resultados = []  # Lista para almacenar los libros encontrados
        for libro in self.libros.values():
            # Buscar por título
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            # Buscar por autor
            elif criterio == "autor" and any(valor.lower() in autor.lower() for autor in libro.autor):
                resultados.append(libro)
            # Buscar por categoría
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados  # Devolvemos la lista de libros encontrados

    # Método para listar los libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")  # Si el usuario no está registrado, mostramos un mensaje de error
            return
        usuario = self.usuarios[id_usuario]  # Obtenemos al usuario usando su ID
        if usuario.libros_prestados:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"- {libro.titulo}")  # Imprimimos el título de cada libro prestado
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")  # Si no tiene libros prestados, mostramos un mensaje

# Ejemplo de uso:

# Crear objetos de libros
libro1 = Libro("El Quijote", ("Miguel", "de Cervantes"), "Ficción", "12345")
libro2 = Libro("1984", ("George", "Orwell"), "Ficción", "67890")
libro3 = Libro("Python para todos", ("Charles", "Severance"), "Educación", "11223")

# Crear objeto biblioteca
biblioteca = Biblioteca()

# Crear usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("12345", "001")
biblioteca.prestar_libro("67890", "002")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libros
biblioteca.devolver_libro("12345", "001")

# Buscar libros
resultados = biblioteca.buscar_libro("autor", "Cervantes")
for libro in resultados:
    print(libro)

# Quitar libro
biblioteca.quitar_libro("11223")




