import math
from tabulate import tabulate
import multiplicativeCongruentMethod as multCM


# Parámetros para el generador de números pseudoaleatorios
a = 16807
m = 10007
X0 = 17
# Secuencia de números pseudoaleatorios
cont = multCM.modular_sequence(a, m, X0)[0]
random_numbers = multCM.modular_sequence(a, m, X0)[5]

# Random number generator
random_numbers = multCM.modular_sequence(a, m, X0)

# Given values
Lambda = 5
max_k = 15

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def poisson_probability(k, Lambda):
    e_to_the_minus_lambda = math.exp(-Lambda)
    lambda_to_the_k = Lambda ** k
    factorial_k = factorial(k)
    return (e_to_the_minus_lambda * lambda_to_the_k) / factorial_k

def generate_poisson_table(Lambda, max_k):
    table_data = []
    cumulative_probabilities = [0]  # Initialize the cumulative probabilities list with 0 as the first element
    prev_sum = 0  # Initialize the sum of probabilities of the previous row
    for k in range(max_k + 1):
        probability = poisson_probability(k, Lambda)
        sum_probability = probability + prev_sum  # Calculate the sum of current and previous probabilities
        table_data.append((k, probability, sum_probability))
        cumulative_probabilities.append(sum_probability)  # Add the sum to the cumulative probabilities list
        prev_sum = sum_probability  # Update the sum for the next iteration
    return table_data, cumulative_probabilities

# Function to generate combined data
def generate_combined_data(random_numbers, ranges):
    combined_data = []

    for i, (start, end) in enumerate(ranges, start=1):
        numbers_in_range = [number for number in random_numbers[:10] if start <= number < end]
        indexed_numbers = [(random_numbers.index(num) + 1, num) for num in numbers_in_range]
        indexed_numbers_str = ' - '.join([f"{index}) {value:.4f}" for index, value in indexed_numbers])
        combined_data.append([f"{i}", f"{start:.4f} - {end:.4f}", indexed_numbers_str])

    return combined_data

# Funtion to print the final result
def result(random_numbers, ranges):
    combined_data = []

    # Create a list of tuples (index, random number)
    indexed_numbers = [(random_numbers.index(num), num) for num in random_numbers[:10]]
    # Sort the list of tuples by the index of the random number
    indexed_numbers.sort()

    for index, num in indexed_numbers:
        for i, (start, end) in enumerate(ranges, start=1):
            if start <= num < end:
                table_index = random_numbers.index(num) + 1
                combined_data.append([f"Random Number: {num:.4f}", f"Index: {index + 1}", f"Table Index: {table_index}"])
                print(f"Obtained R{index + 1} = {num:.4f}, implies a value of x{index + 1} = {i}, that means, for the week {index + 1} will be {i} pieces")
                break

    return combined_data

# Generate the table data and cumulative probabilities
table_data, cumulative_probabilities = generate_poisson_table(Lambda, max_k)

# Print the table using tabulate
headers = ["k(x)", "f(x)", "Cumulative of f(x)"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Generate combined data
combined_data = generate_combined_data(random_numbers, ranges)

# Print the combined table
print("\nRanges and Random Numbers:")
print(tabulate(combined_data, headers=["k(x)", "Ranges", "Random Numbers"], tablefmt="grid"))


# Generate combined data
print("\n")
result = result(random_numbers, ranges)