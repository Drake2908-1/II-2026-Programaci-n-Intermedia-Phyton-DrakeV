class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_informacion(self):
        print(f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio_publicacion}")