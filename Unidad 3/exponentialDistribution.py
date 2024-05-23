import math
import multiplicativeCongruentMethod as multCM

# Función para generar una distribución exponencial
def exponential_dist(random_numbers, Lambda):
    for i, r in enumerate(random_numbers[:10]):  # Solo los primeros 10 elementos
        # Fórmula para generar números distribuidos exponencialmente
        x = - (1 / Lambda) * math.log(r)
        print(f"x{i+1}: {x}")

def main():
    # Parámetros para el generador de números pseudoaleatorios
    a = 16807
    m = 10007
    X0 = 17

    # Secuencia de números pseudoaleatorios
    cont = multCM.modular_sequence(a, m, X0)[0]
    random_numbers = multCM.modular_sequence(a, m, X0)[5]

    # Tiempo promedio entre llegadas
    average_time_between_arrivals = 2

    # Calcular lambda usando la fórmula lambda = 1/T
    Lambda = 1 / average_time_between_arrivals

    # Ahora Lambda representa una tasa de llegada más realista
    print("λ:", Lambda, "\n")
    
    # Generar y mostrar la distribución exponencial
    exponential_dist(random_numbers[:cont], Lambda)
  
if __name__ == '__main__':
    main()
