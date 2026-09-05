#se importan librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
#se crean las clases:
class Pelicula:
    def __init__(self,
        titulo: str,
        genero: str,
        duracion: int,
        presupuesto: float,
        calificacion: float
    ):
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.presupuesto = presupuesto
        self.calificacion = calificacion

    def mostrar_datos(self):
        print("El titulo de la pelicua es: ", self.titulo)
        print("El genero de la pelicula es: ", self.genero)
        print("La duracion de la pelicula es: ", self.duracion)
        print("El presupuesto de la pelicula es: ", self.presupuesto)
        print("La calificacion de la pelicula es: ", self.calificacion)
#se crea una lista para almacenar las peliculas
peliculas = []
for i in range(5):
    titulo = input("Ingrese el titulo de la pelicula: ")
    genero = input("Ingrese el genero de la pelicula: ")
    duracion = int(input("Ingrese la duracion de la pelicula: "))
    presupuesto = float(input("Ingrese el presupuesto de la pelicula: "))
    calificacion = float(input("Ingrese la calificacion de la pelicula: "))
    pelicula = Pelicula(titulo, genero, duracion, presupuesto, calificacion)
    peliculas.append(pelicula)
    print (pelicula.mostrar_datos())
#se crea un dataframe para almacenar los datos de las peliculas
data = []
for pelicula in peliculas:
    data.append([pelicula.titulo, pelicula.genero, pelicula.duracion, pelicula.presupuesto, pelicula.calificacion])
df = pd.DataFrame(data, columns=['Titulo', 'Genero', 'Duracion', 'Presupuesto', 'Calificacion'])
print(df)
print(df.info())
#el promedio de la pelicula es 
print (df['Calificacion'].mean())
print (df["Presupuesto"].mean())
print (df["Duracion"].mean())
# la maxima duracion de la pelicula es
print (df["Duracion"].max())
# la pelicula con menos duracion es 
print (df["Duracion"].min())
# calculo de la matrix de correalcion
print (df.corr())
#la correlcion entre duracion y calificacion es:
print (df[["Duracion", "Calificacion"]].corr())
#la relacion entre presupuesto y calificacion es:
print (df[["Presupuesto", "Calificacion"]].corr())
#se crea un grafico de barras para mostrar la dispersion entre presupuesti y calificacion
df.plot(kind = "scatter",
        x = "Presupuesto",
        y = "Calificacion",)
plt.show()










