from persona import Persona
from profesor import Profesor
from estudiante import Estudiante

def imprimir_detalles(persona):
  
    print(persona.obtener_detalles())

list_personas = []

estudiantes = [
    Estudiante(nombre="Juan", identificacion="123456789", carrera="Medicina"),
    Estudiante(nombre="Ana", identificacion="987654321", carrera="Ingeniería eléctrica")
]
for estudiante in estudiantes:
    list_personas.append(estudiante)

profesores = [
    Profesor(nombre="Carlos", identificacion="456789123", departamento="Matemáticas"),
    Profesor(nombre = "Maria", identificacion = "321654987", departamento = "Física")]
for profesor in profesores:
    list_personas.append(profesor)

for persona in list_personas:
    imprimir_detalles(persona)





