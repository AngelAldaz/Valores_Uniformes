import multiplicativeCongruentMethod as multCM

# Función para calcular y mostrar la distribución binomial
def binomial_dist(probability, random_numbers):
    # Contador para valores menores o iguales a p
    count = 0
    numbers_less_than_probability = []

    # Imprimir solo los primeros diez números aleatorios generados
    print("\nFirst ten random numbers generated:\n")
    for i, num in zip(range(1, 11), random_numbers[:10]):
        print(f"{chr(96 + i)}) {num}")  # Convertir a letra usando la tabla ASCII
        # Incrementar el contador
        count += 1

    # Restablecer el contador para números menores que la probabilidad
    count_less_than_probability = 0

    # Iterar a través de la lista y contar valores menores o iguales a p
    for i, value in enumerate(random_numbers[:10], start=1):
        if value <= probability:
            count_less_than_probability += 1
            # Guardar el número junto con su índice original
            numbers_less_than_probability.append((chr(96 + i), value))  # Convertir a letra usando la tabla ASCII

    # Determinar si se debe usar "is" o "are"
    verb = "is" if count_less_than_probability == 1 else "are"

    # Imprimir el número de valores menores o iguales a p
    print(f"\nThe number of values (x) less or equal than Probability {verb} {count_less_than_probability}:\n")

    # Imprimir cada número menor que la probabilidad con su índice original en una nueva línea
    for index, value in numbers_less_than_probability:
        print(f"{index}) {value}")


def main():
    # Parámetros para el generador de números pseudoaleatorios
    a = 16807
    m = 10007
    X0 = 17

    # Secuencia de números pseudoaleatorios
    cont = multCM.modular_sequence(a, m, X0)[0]
    random_numbers = multCM.modular_sequence(a, m, X0)[5]

    # Intentos
    attempts = 6

    # Calcular la probabilidad usando la fórmula p = 1/T
    probability = 1 / attempts

    print("Probability: ", probability)
    binomial_dist(probability, random_numbers[:cont])

if __name__ == '__main__':
    main()
