import math
import pandas as pd
from multiplicativeCongruentMethod import modular_sequence 

def calculate_and_print_result(R, miu, sigma):
    # Calculate the sum of the first 10 values in R
    random_numbers_sum = sum(R)

    # Print the sum of the first 10 values with three decimal places
    print(f"The sum of the first 16 values (ΣR) is: {random_numbers_sum:.3f}")

    # Calculate the result of the expression
    result = miu + sigma * (random_numbers_sum - 6)

    # Print the result with three decimal places
    print(f"{miu} + {sigma} * ({random_numbers_sum:.3f} - 6) = {result:.3f}")

def main():
  # Valores dados
  a, m, X0 = 16807, 10007, 17

  # Random number generator
  random_numbers = modular_sequence(a, m, X0)[5][:modular_sequence(a, m, X0)[0]]

  # Array of random values
  R = random_numbers[:16]

  # Mean and standard deviation
  miu = 2.5
  sigma = 0.4

  # Call the function to calculate and print the result
  calculate_and_print_result(R, miu, sigma)

if __name__ == '__main__':
  main()