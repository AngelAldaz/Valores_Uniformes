import numpy as np
import pandas as pd
from scipy.stats import expon, chi2

# Calcular las probabilidades exponenciales
def calcular_probabilidades_exponenciales(x, Lambda):
    return expon.pdf(x, scale=1/Lambda)

# Calcular las frecuencias esperadas
def calcular_frecuencias_esperadas(probabilidades, total_observaciones):
    return (probabilidades * total_observaciones).round(0)

# Calcular los valores de chi-cuadrado
def calcular_chi_cuadrado(observado, esperado):
    return ((observado - esperado) ** 2) / esperado

# Calcular el chi-cuadrado observado total
def calcular_chi_cuadrado_observado(df):
    return df['chi^2'].sum()

# Calcular el valor crítico para chi-cuadrado
def calcular_valor_critico_chi_cuadrado(grados_de_libertad=2, confianza=0.95):
    return chi2.ppf(confianza, df=grados_de_libertad)

# Imprimir la tabla
def imprimir_tabla(df):
    print(df.to_string(index=False))

# Función principal para realizar el análisis de chi-cuadrado
def main():
    # Datos de entrada
    data = {
        "xi": [0, 1, 2, 3, 4, 5],
        "fi": [315, 142, 40, 9, 2, 1]
    }

    # Parámetro lambda para la distribución exponencial
    Lambda = 0.5147
    df = pd.DataFrame(data)
    total_observaciones = sum(df['fi'])

    # Calcular probabilidades exponenciales
    df['Probabilidad Exponencial'] = calcular_probabilidades_exponenciales(df['xi'], Lambda)

    # Calcular frecuencias esperadas
    df['Frecuencia esperada'] = calcular_frecuencias_esperadas(df['Probabilidad Exponencial'], total_observaciones)

    # Calcular valores de chi-cuadrado
    df['chi^2'] = calcular_chi_cuadrado(df['fi'], df['Frecuencia esperada'])

    # Imprimir la tabla
    imprimir_tabla(df)

    # Calcular e imprimir el chi-cuadrado observado
    chi2_observado = calcular_chi_cuadrado_observado(df)
    print(f"Chi-cuadrado observado: {chi2_observado:.4f}")

    # Calcular e imprimir el valor crítico de chi-cuadrado
    chi2_critico = calcular_valor_critico_chi_cuadrado()
    print(f"Valor crítico de chi-cuadrado (0.05, 2): {chi2_critico:.4f}")



# Ejecutar la función principal
if __name__ == "__main__":
    main()
