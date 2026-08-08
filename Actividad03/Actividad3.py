import pandas as pd
df = pd.read_csv('./Actividad03/Estudiantes.csv')
print(df) 

print (df[['Edad', 'Estatura']].max())
print (df[['Edad', 'Estatura']].min())
