import math
import pandas as pd
from multiplicativeCongruentMethod import modular_sequence

#EDITAR POR CANTIDAD DE NUM ALEATORIOS
cant = 100

def factorial(n):
    # Calcular el factorial de n
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def probabilidad_poisson(k, Lambda):
    # Calcular la probabilidad de Poisson
    e_elevado_a_menos_lambda = math.exp(-Lambda)
    lambda_elevado_a_k = Lambda ** k
    factorial_k = factorial(k)
    return (e_elevado_a_menos_lambda * lambda_elevado_a_k) / factorial_k

def generar_tabla_poisson(Lambda, max_k):
    # Generar los datos de la tabla de Poisson
    datos_tabla = []
    probabilidades_acumuladas = [0]
    suma_previa = 0
    for k in range(max_k + 1):
        probabilidad = probabilidad_poisson(k, Lambda)
        suma_probabilidad = probabilidad + suma_previa
        datos_tabla.append((k, probabilidad, suma_probabilidad))
        probabilidades_acumuladas.append(suma_probabilidad)
        suma_previa = suma_probabilidad
    return datos_tabla, probabilidades_acumuladas

def generar_datos_combinados(numeros_aleatorios, rangos):
    # Generar datos combinados
    datos_combinados = []
    for i, (inicio, fin) in enumerate(rangos, start=1):
        numeros_en_rango = [numero for numero in numeros_aleatorios[:cant] if inicio <= numero < fin]
        numeros_indexados = [(numeros_aleatorios.index(num) + 1, num) for num in numeros_en_rango]
        numeros_indexados_str = ' - '.join([f"{indice}) {valor:.4f}" for indice, valor in numeros_indexados])
        datos_combinados.append([f"{i}", f"{inicio:.4f} - {fin:.4f}", numeros_indexados_str])
    return datos_combinados

def resultado(numeros_aleatorios, rangos):
    # Generar datos de resultado
    datos_combinados = []
    numeros_indexados = [(numeros_aleatorios.index(num), num) for num in numeros_aleatorios[:cant]]
    numeros_indexados.sort()
    for indice, num in numeros_indexados:
        for i, (inicio, fin) in enumerate(rangos, start=1):
            if inicio <= num < fin:
                indice_tabla = numeros_aleatorios.index(num) + 1
                datos_combinados.append([f"Número Aleatorio: {num:.4f}", f"Índice: {indice + 1}", f"Índice Tabla: {indice_tabla}"])
                print(f"Se obtuvo R{indice + 1} = {num:.4f}, lo que implica un valor de x{indice + 1} = {i}, lo que significa que para la semana {indice + 1} será {i} piezas")
                break
    return datos_combinados

def main():
    # Valores dados
    a, m, X0 = 16807, 10007, 17
    rangos = [(0.0, 0.0067), (0.0067, 0.0404), (0.0404, 0.1247), (0.1247, 0.265), (0.265, 0.4405),
              (0.4405, 0.616), (0.616, 0.7622), (0.7622, 0.8666), (0.8666, 0.9319), (0.9319, 0.9682),
              (0.9682, 0.9863), (0.9863, 0.9945), (0.9945, 0.998), (0.998, 0.9993), (0.9993, 0.9998),
              (0.9998, 0.9999)]
    Lambda, max_k = 5, 15

    # Generador de números aleatorios
    numeros_aleatorios = modular_sequence(a, m, X0)[5][:modular_sequence(a, m, X0)[0]]

    # Generar la tabla de Poisson
    datos_tabla, probabilidades_acumuladas = generar_tabla_poisson(Lambda, max_k)

    # Imprimir la tabla de Poisson
    encabezados = ["k(x)", "f(x)", "Acumulativo de f(x)"]
    tabla_poisson = pd.DataFrame(datos_tabla, columns=encabezados)
    print(tabla_poisson.to_string(index=False))

    # Generar datos combinados
    datos_combinados = generar_datos_combinados(numeros_aleatorios, rangos)

    # Imprimir la tabla combinada
    print("\n-> Rangos y Números Aleatorios:\n")
    tabla_combinada = pd.DataFrame(datos_combinados, columns=["k(x)", "Rangos", "Números Aleatorios"])
    print(tabla_combinada.to_string(index=False))

    # Generar datos de resultado
    print("\n")
    resultado(numeros_aleatorios, rangos)

if __name__ == "__main__":
    main()