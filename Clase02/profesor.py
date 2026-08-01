from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, identificacion, departamento):
        super().__init__(nombre, identificacion)
        self.departamento = departamento

    def obtener_detalles(self):
        return (f"Departamento: {self.departamento}")
        