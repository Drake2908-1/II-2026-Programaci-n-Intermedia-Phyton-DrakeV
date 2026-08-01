from entidades.libro import Libro

def ejecutar():
    catalogo = []

    print("--- REGISTRO DE LIBROS ---")
    for i in range(1, 4):
        print(f"\nIngresando libro #{i}:")
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        anio = input("Año de publicación: ")
        
        nuevo_libro = Libro(titulo, autor, anio)
        catalogo.append(nuevo_libro)

    print("\n====================================")
    print("      CATÁLOGO DE LIBROS")
    print("====================================")
    
    for libro in catalogo:
        libro.mostrar_informacion()

if __name__ == "__main__":
    ejecutar()