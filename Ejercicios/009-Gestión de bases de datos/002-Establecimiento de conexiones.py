# Clase Libro
class Libro:
    def __init__(self, isbn, titulo, autor, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def prestar_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            if libro.disponible:
                libro.prestar()
                print(f"El libro '{libro.titulo}' ha sido prestado correctamente.")
            else:
                print(f"El libro '{libro.titulo}' no está disponible.")
        else:
            print("No se encontró un libro con ese ISBN.")

    def devolver_libro(self, isbn):
        libro = self.buscar_libro(isbn)
        if libro:
            if not libro.disponible:
                libro.devolver()
                print(f"El libro '{libro.titulo}' ha sido devuelto correctamente.")
            else:
                print(f"El libro '{libro.titulo}' ya estaba disponible.")
        else:
            print("No se encontró un libro con ese ISBN.")


# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro(1234567890, "El Señor de los Anillos", "J.R.R. Tolkien")
libro2 = Libro(987654321, "Harry Potter y la Piedra Filosofal", "J.K. Rowling")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Prestar "El Señor de los Anillos"
biblioteca.prestar_libro(1234567890)

# Devolver "El Señor de los Anillos"
biblioteca.devolver_libro(1234567890)