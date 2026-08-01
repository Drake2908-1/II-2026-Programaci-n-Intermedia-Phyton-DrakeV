class Persona ():
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
    def obtener_detalles(self):
        return (
            f"Nombre: {self.nombre}, "
            f"Identificación: {self.identificacion}"
        )
