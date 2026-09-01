
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv("estudiantes.csv")

# 2. Eliminar registros duplicados
df.drop_duplicates(inplace=True)

# 3. Corregir datos erróneos
df.loc[27, "Edad"] = 22
df.loc[28, "Edad"] = 20

# Convertir la columna Edad a número
df["Edad"] = pd.to_numeric(df["Edad"])

# 4. Reemplazar valores nulos usando la media
x = df["Edad"].mean()
df.fillna({"Edad": x}, inplace=True)

x = df["Estatura"].mean()
df.fillna({"Estatura": x}, inplace=True)

x = df["Peso"].mean()
df.fillna({"Peso": x}, inplace=True)

x = df["HorasEstudio"].mean()
df.fillna({"HorasEstudio": x}, inplace=True)

x = df["Calificacion"].mean()
df.fillna({"Calificacion": x}, inplace=True)

print("--- CONTENIDO DEL DATASET ---")
print(df)

# 5. Calcular los promedios solicitados
print("\nPromedio Edad:", df["Edad"].mean())
print("Promedio Peso:", df["Peso"].mean())
print("Promedio HorasEstudio:", df["HorasEstudio"].mean())
print("Promedio Calificacion:", df["Calificacion"].mean())

# 6. Matriz de correlación
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(df.corr())

# 7. Graficar Estatura y Peso
df.plot(x="Estatura", y="Peso", kind="line")
plt.show()

