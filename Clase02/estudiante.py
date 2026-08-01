from persona import Persona
class Estudiante (Persona):
    def __init__(self, nombre, identificacion, carrera):
        super().__init__(nombre, identificacion)
        self.carrera = carrera

    def obtener_detalles(self):
        detalles_persona = super().obtener_detalles()
        return f"{detalles_persona}, Carrera: {self.carrera}"