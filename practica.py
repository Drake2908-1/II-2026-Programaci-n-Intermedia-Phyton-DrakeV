class Estudiante:
    def___init__(
        self,
        nombre: str,
        edad: int,
        estatura: float,
        horas_estudio: int,
        calificacion: float
    ):
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
        print(f"calificacion: {self.calificacion}")

estudiantes =[]

for i in range(5):
    print(f"\n--- Estudiante {i + 1}")
        estudiante = Estudiante(
        input("Nombre: "),
        int(input("Edad: ")),
        float(input("Estatura: ")),
        int(input("Horas de estudio: ")),
    float(input("Calificacion:"))

estudiantes.append(estudiante)
datos = []
for estudiante in estudiantes:
    datos.append(estudiante.__dict__)
df = pd.DataFrame(datos)

print("\n--- Datos de los estudiantes ---")
print(df)

print("\n--- Promedios ---")
print(df.mean(numeric_only=True))
print("\n--- Nota más alta ---")
indice = df[calificacion"].idxmax()
print(f"calificacion más alta: {df['calificacion']}.max()}")
print ("Datos del estudiante")
print(df.loc)
