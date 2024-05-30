import numpy as np
import pandas as pd
from scipy.stats import poisson

# Calculo la función de masa de probabilidad (PMF) de la distribución de Poisson.
def calculate_poisson_probability(Lambda, k):
    return poisson.pmf(k, Lambda)

# Calculo la probabilidad acumulada teórica de la distribución de Poisson para cada valor observado.
def calculate_poisson_cumulative_probability(Lambda, data):
    data['Poisson theoretical probability (i)'] = [calculate_poisson_probability(Lambda, k) for k in range(len(data))]
    data['Cumulative theoretical probability'] = np.cumsum(data['Poisson theoretical probability (i)']).round(4)
    return data

# Calculo la función de distribución acumulada (CDF) observada basada en las probabilidades observadas.
def calculate_observed_poisson_cdf(data):
    data['Observed cumulative probability'] = data['Observed probability (i)'].cumsum().round(4)
    return data

# Calculo la diferencia absoluta entre las probabilidades acumuladas observadas y teóricas.
def calculate_absolute_difference_poisson(data):
    data['|D|'] = (abs(data['Observed cumulative probability'] - data['Cumulative theoretical probability'])).round(4)
    return data

# Encuentro la diferencia absoluta máxima entre las probabilidades acumuladas observadas y teóricas.
def find_maximum_difference_poisson(data):
    return data['|D|'].max().round(4)

def calculate_mean(data):
    # Calculo la media de los datos.
    mean = ((data['Class (i)'] * data['Observed frequency']).sum() / data['Observed frequency'].sum()).round(4)
    return mean

def calculate_total_frequency(data):
    # Calculo la suma total de frecuencias.
    n = data['Observed frequency'].sum().round(4)
    return n

def calculate_sum_fi_xi2(data):
    # Calculo la suma de (fi * xi^2).
    data['(i) * Observed frequency^2'] = data['Observed frequency'] * (data['Class (i)'] ** 2)
    sum_fi_xi2 = data['(i) * Observed frequency^2'].sum()
    return sum_fi_xi2

def calculate_standard_deviation(mean, sum_fi_xi2, n):
    # Calculo la desviación estándar.
    s = ((sum_fi_xi2 - ((mean ** 2) * n)) / (n - 1)).round(4)
    return s

def calculate_lambda(mean, s):
    # Calculo el parámetro Lambda de la distribución de Poisson.
    Lambda = ((mean + s) / 2).round(4)
    return Lambda

def main():
    # Clases y frecuencias dadas
    data = {
        "Class (i)": [0, 1, 2, 3, 4],
        "Observed frequency": [30, 13, 5, 1, 1],
        "Observed probability (i)": [0.6, 0.26, 0.1, 0.02, 0.02]
    }

    # Creo un DataFrame de Pandas con los datos
    df = pd.DataFrame(data)

    # Calculo estadísticas
    n = calculate_total_frequency(df)
    mean = calculate_mean(df)
    sum_fi_xi2 = calculate_sum_fi_xi2(df)
    s = calculate_standard_deviation(mean, sum_fi_xi2, n)
    Lambda = calculate_lambda(mean, s)

    df = calculate_observed_poisson_cdf(df)
    df = calculate_poisson_cumulative_probability(Lambda, df)
    df = calculate_absolute_difference_poisson(df)
    Dmax = find_maximum_difference_poisson(df)

    # Imprimo la tabla
    headers = ["Class (i)", "Observed frequency", "Observed probability (i)", "(i) * Observed frequency^2", "Observed cumulative probability", "Poisson theoretical probability (i)", "Cumulative theoretical probability", "|D|"]
    print(df.to_string(index=False, header=headers))

    # Imprimo resultados
    print("\nSuma de frecuencias observadas (n):", n)
    print("Media (x):", mean)
    print("Desviación estándar (s):", s)
    print("λ:", Lambda)
    print(f"Dmax: ", Dmax)

# Ejecuto la función principal
if __name__ == "__main__":
    main()
