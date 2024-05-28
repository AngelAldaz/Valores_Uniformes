import pandas as pd
from math import sqrt, erf

# Define una función para calcular la función de densidad de probabilidad observada (f(x)obs)
def calculate_observed_pdf(data):
    total_observations = data['fi'].sum()
    data['Class * x'] = (data['fi'] / total_observations).round(4)
    return data

# Define una función para calcular la función de distribución acumulativa observada (F(x)obs)
def calculate_observed_cdf(data):
    data['f(x) cumulative observed'] = data['Class * x'].cumsum().round(4)
    return data

# Define una función para calcular la media (x̄)
def calculate_mean(data):
    data['x * fi'] = (data['x'] * data['fi']).round(4)
    mean = round(data['x * fi'].sum() / data['fi'].sum(), 4)
    return mean

# Define una función para calcular la desviación estándar (s)
def calculate_standard_deviation(data, mean):
    total_observations = data['fi'].sum()
    sum_fi_xi2 = round((data['fi'] * data['x'] ** 2).sum(), 4)
    s = round(sqrt((sum_fi_xi2 - (mean ** 2) * total_observations) / (total_observations - 1)), 4)
    return s

# Define una función para calcular los puntajes Z para los límites inferior y superior
def calculate_z_scores(data, mean, std_dev):
    lower_limits = data['class'].str.split('-', expand=True)[0].astype(int)
    upper_limits = data['class'].str.split('-', expand=True)[1].astype(int)
    data['Z lower limit'] = ((lower_limits - mean) / std_dev).round(4)
    data['Z upper limit'] = ((upper_limits - mean) / std_dev).round(4)
    return data

# Define una función para calcular las probabilidades para los límites
def norm_cdf(z):
    return (1 + erf(z / sqrt(2))) / 2

def calculate_probabilities(data):
    data['P lower limit'] = data['Z lower limit'].apply(lambda z: round(norm_cdf(z), 4))
    data['P upper limit'] = data['Z upper limit'].apply(lambda z: round(norm_cdf(z), 4))
    data['P theoretical (normal)'] = (data['P upper limit'] - data['P lower limit']).round(4)
    return data

# Define una función para calcular la probabilidad acumulativa teórica
def calculate_theoretical_cumulative_probability(data):
    data['P theoretical (cumulative)'] = data['P theoretical (normal)'].cumsum().round(4)
    return data

# Define una función para calcular la diferencia absoluta (|D|)
def calculate_absolute_difference(data):
    data['|D|'] = (abs(data['f(x) cumulative observed'] - data['P theoretical (normal)'])).round(4)
    return data

# Define una función para encontrar la diferencia máxima (Dmax)
def find_maximum_difference(data):
    Dmax = data['|D|'].max()
    return Dmax

# Define una función para devolver los resultados en un DataFrame
def get_results_df(data):
    headers = ["class", "x", "fi", "Class * x", "f(x) cumulative observed", "Z lower limit", "P lower limit", "P theoretical (normal)", "P theoretical (cumulative)", "|D|"]
    result_df = data[headers].copy()
    return result_df

# Datos de la tabla proporcionada
data = {
    "class": ["20-30", "30-40", "40-50", "50-60", "60-70", "70-80"],
    "x": [25, 35, 45, 55, 65, 75],
    "fi": [5, 12, 26, 23, 10, 3],
}

def main():
    # Crear un DataFrame de pandas con los datos
    df = pd.DataFrame(data)

    # Calcular estadísticas
    df = calculate_observed_pdf(df)
    df = calculate_observed_cdf(df)
    mean = calculate_mean(df)
    std_dev = calculate_standard_deviation(df, mean)
    df = calculate_z_scores(df, mean, std_dev)
    df = calculate_probabilities(df)
    df = calculate_theoretical_cumulative_probability(df)
    df = calculate_absolute_difference(df)
    Dmax = find_maximum_difference(df)
    
    # Obtener resultados en un DataFrame
    result_df = get_results_df(df)
    
    # Imprimir resultados
    print("\nResult DataFrame:\n")
    print(result_df)
    print(f"\nMean (x): {mean:.4f}")
    print(f"Standard Deviation (s): {std_dev:.4f}")
    print(f"Dmax: {Dmax:.4f}")

if __name__ == '__main__':
    main()
