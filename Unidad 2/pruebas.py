import math
from collections import Counter
import pandas as pd
import multiplicativeCongruentMethod as multCM
import os

# Función para convertir una muestra de números en una lista de strings de 5 dígitos
def pokerizacion(muestra: list[int]) -> list[str]:
    return [format(int(element * 100000), '05d') for element in muestra]

# Función para detectar la categoría de un número basado en sus dígitos
def detect_category(number: int) -> str:
    digits = [int(d) for d in str(number)]
    digit_count = Counter(digits)
    
    if len(digit_count) == 5:
        return "Todos diferentes"
    elif 5 in digit_count.values():
        return "Quintilla"
    elif 4 in digit_count.values():
        return "Póker"
    elif 3 in digit_count.values() and 2 in digit_count.values():
        return "Full"
    elif 3 in digit_count.values():
        return "Una tercia"
    elif len(digit_count) == 4:
        return "Un par"
    elif len(digit_count) == 3:
        return "Dos pares"
    else:
        return "Otro"

# Función para calcular la probabilidad de una categoría dada en los datos
def calculate_probability(category: str, data: list[int]) -> float:
    if category == "Todos diferentes":
        return 0.3024
    elif category == "Un par":
        return 0.5040
    elif category == "Dos pares":
        return 0.1080
    elif category == "Una tercia":
        return 0.0720
    elif category == "Full":
        return 0.0090
    elif category == "Póker":
        return 0.0045
    elif category == "Quintilla":
        return 0.0001
    else:  # "Otro"
        return 0

# Función para construir y mostrar una tabla con las frecuencias observadas y esperadas y el cálculo de Chi-Cuadrado
def build_table(data: list[int]):
    observed_frequency = Counter()
    categories = set()
    total_chi_square = 0

    # Contar frecuencias observadas por categoría
    for number in data:
        category = detect_category(number)
        categories.add(category)
        observed_frequency[category] += 1

    rows = []
    grouped_obs = 0
    grouped_prob = 0

    # Construir la tabla con las frecuencias observadas y esperadas y el cálculo de Chi-Cuadrado
    for category in sorted(categories, key=lambda x: observed_frequency[x], reverse=True):
        probability = calculate_probability(category, data)
        expected_frequency = probability * len(data)
        chi_square = 0

        if observed_frequency[category] < 5:
            grouped_obs += observed_frequency[category]
            grouped_prob += probability
        else:
            if grouped_obs > 0:
                chi_square = (grouped_obs - (grouped_prob * len(data))) ** 2 / (grouped_prob * len(data))
                rows.append(["Agrupados", grouped_prob, grouped_prob * len(data), grouped_obs, chi_square])
                total_chi_square += chi_square
                grouped_obs = 0
                grouped_prob = 0

            chi_square = (observed_frequency[category] - expected_frequency) ** 2 / expected_frequency
            rows.append([category, probability, expected_frequency, observed_frequency[category], chi_square])
            total_chi_square += chi_square

    if grouped_obs > 0:
        chi_square = (grouped_obs - (grouped_prob * len(data))) ** 2 / (grouped_prob * len(data))
        rows.append(["Agrupados", grouped_prob, grouped_prob * len(data), grouped_obs, chi_square])
        total_chi_square += chi_square

    # Crear el DataFrame con pandas
    df = pd.DataFrame(rows, columns=[
        'Clase (i)', 
        'Probabilidad Teórica de (i) P(i)', 
        'Frecuencia esperada de (i) Fe(i)=P(i)*n', 
        'Frecuencia observada de (i) Fo(i)', 
        'X²(i)'
    ])
    outDF(df)

    print("\nChi Cuadrado Total:", total_chi_square)

    chi_square_tabulated = float(input(f"\nEscribe el valor tabulado de chi cuadrado para X²(5%,{len(rows)-1}): "))

    if total_chi_square < chi_square_tabulated:
        print("Se concluye que la independencia de los números de la muestra dada NO PUEDE ser rechazada.")
    else:
        print("Se concluye que la independencia de los números de la muestra dada PUEDE ser rechazada.")

# Función para imprimir el DataFrame sin el índice
def outDF(df: pd.DataFrame):
    print(df.to_string(index=False))


def main():
    # Limpiar la pantalla
    os.system('clear')

    # Generar la secuencia usando el método congruente multiplicativo
    a = 16807
    m = 10007
    X0 = 17
    cont = multCM.modular_sequence(a, m, X0)[0]
    numAl = multCM.modular_sequence(a, m, X0)[-1]

    lista = numAl[:cont]

    # Datos de muestra
    data = [
        43923, 61394, 21569, 28490, 23439, 51505, 67879, 55452, 72422, 45444, 34633, 77676, 13173,
        88888, 24177, 94949, 59333, 77399, 92992, 34347, 45850, 62783, 24529, 27489, 37149
    ]

    # Construir y mostrar la tabla
    build_table(data)
    #build_table(pokerizacion(lista))

if __name__ == '__main__':
    main()