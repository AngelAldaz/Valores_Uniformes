import numpy as np
import pandas as pd
from scipy.stats import poisson, chi2

def calcular_chi_cuadrado(datos, Lambda):
    # Calcular las probabilidades de Poisson para k = 0, 1, 2, y 3 o más (agrupando el resto)
    prob_poisson = [poisson.pmf(k, Lambda) if k < 4 else 1 - poisson.cdf(2, Lambda) for k in range(5)]
    datos['Probabilidad Poisson'] = prob_poisson

    # Calcular las frecuencias esperadas
    total_observaciones = sum(datos['Frecuencia observada'])
    datos['Frecuencia esperada'] = (datos['Probabilidad Poisson'] * total_observaciones).round(0)

    # Calcular los valores de chi-cuadrado
    datos['Chi-cuadrado'] = ((datos['Frecuencia observada'] - datos['Frecuencia esperada']) ** 2) / datos['Frecuencia esperada']

    # Total observado de chi-cuadrado
    chi2_observado = datos['Chi-cuadrado'].sum()

    return datos, chi2_observado

def imprimir_resultados(datos, chi2_observado, chi2_critico):
    # Imprimir la tabla
    print(datos.to_string(index=False))
    print(f"Chi-cuadrado observado: {chi2_observado:.4f}")

    # Imprimir el valor crítico de chi-cuadrado con 3 grados de libertad y 95% de confianza
    print(f"Valor crítico de chi-cuadrado (0.05, 2): {chi2_critico:.4f}")

def main():
    # Datos de entrada
    datos = {
        "xi": [0, 1, 2, 3, 4],
        "Frecuencia observada": [60, 20, 7, 2, 1]
    }

    # Crear un DataFrame de pandas
    df = pd.DataFrame(datos)

    # Valor de Lambda para la distribución de Poisson
    Lambda = 0.5577

    # Calcular los valores de chi-cuadrado
    df, chi2_observado = calcular_chi_cuadrado(df, Lambda)

    # Valor crítico de chi-cuadrado con 3 grados de libertad y 95% de confianza
    chi2_critico = chi2.ppf(0.95, df=2)

    # Imprimir resultados
    imprimir_resultados(df, chi2_observado, chi2_critico)

if __name__ == "__main__":
    main()
