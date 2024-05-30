import numpy as np
import pandas as pd
from scipy.stats import norm, chi2

# Calcular la media de los datos
def calcular_media(dataframe):
    return (dataframe['marca'] * dataframe['fi']).sum() / dataframe['fi'].sum()

# Calcular la desviación estándar de los datos
def calcular_desviacion_estandar(dataframe, media):
    sum_fi_xi2 = (dataframe['fi'] * dataframe['marca']**2).sum()
    total_observaciones = dataframe['fi'].sum()
    return np.sqrt((sum_fi_xi2 - total_observaciones * media**2) / (total_observaciones - 1))

# Calcular los límites Z inferiores y superiores
def calcular_limites_z(dataframe, media, desviacion):
    dataframe[['inferior', 'superior']] = dataframe['clase'].str.split('-', expand=True)
    dataframe['Límite Z inferior'] = (dataframe['inferior'].astype(float) - media) / desviacion
    dataframe['Límite Z superior'] = (dataframe['superior'].astype(float) - media) / desviacion

# Calcular las probabilidades normales
def calcular_probabilidades_normales(dataframe):
    dataframe['P límite inferior'] = norm.cdf(dataframe['Límite Z inferior'])
    dataframe['P límite superior'] = norm.cdf(dataframe['Límite Z superior'])
    dataframe['P teórica (normal)'] = dataframe['P límite superior'] - dataframe['P límite inferior']

# Calcular las frecuencias esperadas
def calcular_frecuencias_esperadas(dataframe, total_observaciones):
    dataframe['fi (esperado)'] = (dataframe['P teórica (normal)'] * total_observaciones).round(4)

# Calcular el chi-cuadrado
def calcular_chi_cuadrado(dataframe):
    dataframe['x * fi'] = dataframe['marca'] * dataframe['fi']
    dataframe['fi * xi^2'] = dataframe['fi'] * dataframe['marca']**2
    dataframe['chi2'] = ((dataframe['fi'] - dataframe['fi (esperado)'])**2 / dataframe['fi (esperado)']).round(4)

def main():
    # Definir los datos
    datos = {
        "clase": ["10-30", "30-50", "50-70", "70-90", "90-110"],
        "marca": [20, 40, 60, 80, 100],
        "fi": [10, 22, 50, 25, 10]
    }

    # Crear un DataFrame de pandas
    df = pd.DataFrame(datos)

    # Calcular la media y la desviación estándar
    media = calcular_media(df)
    desviacion = calcular_desviacion_estandar(df, media)

    # Calcular los límites Z
    calcular_limites_z(df, media, desviacion)

    # Calcular las probabilidades normales
    calcular_probabilidades_normales(df)

    # Calcular las frecuencias esperadas
    total_observaciones = df['fi'].sum()
    calcular_frecuencias_esperadas(df, total_observaciones)

    # Calcular el chi-cuadrado
    calcular_chi_cuadrado(df)

    # Calcular el chi-cuadrado observado
    chi2_observado = df['chi2'].sum()

    # Calcular el valor crítico del chi-cuadrado
    chi2_critico = chi2.ppf(0.95, df=len(df)-3)  # 2 parámetros estimados (media y desviación estándar)

    # Imprimir los resultados
    columnas_a_mostrar = df.drop(columns=['inferior', 'superior', 'x * fi', 'fi * xi^2', 'Límite Z superior', 'P límite superior'])
    print(columnas_a_mostrar.to_string(index=False))
    print(f"Chi-cuadrado total observado: {chi2_observado:.4f}")
    print(f"Valor crítico de Chi-cuadrado (0.05, {len(df)-3}): {chi2_critico:.4f}")

if __name__ == "__main__":
    main()
