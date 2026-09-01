import pandas as pd

class Estudiante:
    def __init__(self, nombre, edad, estatura, horas_estudio, calificacion):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.horas_estudio = horas_estudio
        self.calificacion = calificacion

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Estatura: {self.estatura}")
        print(f"Horas de estudio: {self.horas_estudio}")
        print(f"Calificación: {self.calificacion}")

lista_estudiantes = []
Estudiantes = [
    {"nombre": "Juan", "edad": 20, "estatura": 1.75, "horas_estudio": 10, "calificacion": 8.5},
    {"nombre": "María", "edad": 22, "estatura": 1.65, "horas_estudio": 8, "calificacion": 9.0},
    {"nombre": "Ana", "edad": 19, "estatura": 1.70, "horas_estudio": 12, "calificacion": 7.5},
    {"nombre": "Luis", "edad": 21, "estatura": 1.80, "horas_estudio": 15, "calificacion": 9.5},
    {"nombre": "Andrea", "edad": 23, "estatura": 1.68, "horas_estudio": 9, "calificacion": 8.0}
]

for estudiante_data in Estudiantes:
    estudiante = Estudiante(**estudiante_data)
    lista_estudiantes.append(estudiante)
    print(f"\nDatos del estudiante {estudiante.nombre}:")
    estudiante.mostrar_datos()

df = pd.DataFrame(Estudiantes)
print(df)


