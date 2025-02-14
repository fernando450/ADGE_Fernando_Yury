import pandas as pd
import matplotlib.pyplot as plt

# Cargar el DataFrame
df = pd.read_csv("P_Regimen_C_Bucaramanga.csv", delimiter=';')

#Cambiar nombres de las columnas a mayusculas
df.columns = df.columns.str.upper()


#Cambiar el sexo a formato numerico
def convertir_genero(genero):
    if genero == "Femenino":
        return 0
    elif genero == "Masculino":
        return 1

df['SEXO'] = df['SEXO'].apply(convertir_genero)

def cambiar_estado(estado):
    if estado == "PL":
        return "PROTECCION LABORAL"
    elif estado == "AE":
        return "ACTIVO POR EMERGENCIA"
    elif estado == "ACTIVO":
        return estado

df['ESTADO'] = df['ESTADO'].apply(cambiar_estado)

#Funcion para cambiar nombre a la categoria de afiliacion.
def cambiar_categoria(categoria):
    if categoria == "A":
        return "Ingresos menor a 2 SMMLV"
    elif categoria == "B":
        return "Ingresos Entre 2 y 5 SMMLV"
    elif categoria == "C":
        return "Ingresos mayores a 5 SMMLV"

df['CATEGORIA'] = df['CATEGORIA'].apply(cambiar_categoria)
#Graficas
# 1. Estado de afiliación
plt.figure(figsize=(8, 5))
df['ESTADO'].value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%',
    colors=['lightgreen', 'lightcoral']
)
plt.title('Estado de afiliación')
plt.ylabel('') 
plt.tight_layout()
plt.show()

# 2. Distribución de afiliados por sexo
plt.figure(figsize=(8, 5))
df['SEXO'].replace({1: 'Mujer', 0: 'Hombre'}).value_counts().plot(
    kind='pie', 
    autopct='%1.1f%%', 
    colors=['lightblue', 
    'pink']
)
plt.title('Distribución de afiliados por sexo')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 3. Distribución por categoría de afiliación
plt.figure(figsize=(8, 5))
df['CATEGORIA'].value_counts().plot(kind='bar', color='orange')
plt.title('Distribución por categoría de afiliación')
plt.xlabel('Categoría')
plt.ylabel('Número de afiliados')
plt.tight_layout()
plt.show()

