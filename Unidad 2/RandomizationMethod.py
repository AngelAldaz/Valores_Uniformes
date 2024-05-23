

import pandas as pd
import os
import multiplicativeCongruentMethod as multCM
from fractions import Fraction

def binarizacion(muestra):
    nuevaMuestra = []
    for elemento in muestra:
        if elemento > 0.5:
            nuevaMuestra.append(1)
        else:
            nuevaMuestra.append(0)
    return nuevaMuestra

def contarElementos(muestra,delimitante):
    #Inicializacion de variables
    valoresAContar = []
    cantLongitudes = 0
    longitudes = []
    
    #Determinar posiciones del elemento limitante (0 o 1), usanod el DELIMITANTE
    for i in range(len(muestra)):
        if muestra[i] == delimitante:
            valoresAContar.append(i)

    #print(valoresAContar)
    
    #Encontrar cuantas Longitudes se tienen
    for i in range(0,len(valoresAContar)):
        try:
            #print(len(muestra[valoresAContar[i]+1:valoresAContar[i+1]]))
            if cantLongitudes < len(muestra[valoresAContar[i]+1:valoresAContar[i+1]]):
                cantLongitudes = len(muestra[valoresAContar[i]+1:valoresAContar[i+1]])
        except:
            pass
    
    #Crear lista con la cantidad correspondiente de Longitudes, en ceros
    for i in range(cantLongitudes+1):
        longitudes.append(0)
    
    #Imprimir cantidad de longitudes
    print(f'Cantidad de Longitudes: {len(longitudes)}')
    
    #Hacer el conteo correspondiente
    for i in range(0,len(valoresAContar)):
        try:
            longitudes[len(muestra[valoresAContar[i]+1:valoresAContar[i+1]])] += 1
        except:
            pass
    
    #Resultados del conteo de Ceros
    return longitudes

def test_sequence(FE,longitudes, cantLongitudes):
  
  nueva_lista = longitudes[:]  # Copia de la lista original para no modificarla
  nueva_lista_FE = FE[:]  # Copia de la lista original para no modificarla
  cont = 0
  for i in range(len(longitudes)):
    if longitudes[i] < cantLongitudes and longitudes[i] != 0:
      cont += 1
      # Si el número es menor que la longitud de la lista, sumarlo con su vecino más cercano
      if i == 0:
        # Si es el primer número, sumar con el siguiente
        nueva_lista[i+1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i+1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif i == cantLongitudes - 1:
        # Si es el último número, sumar con el anterior
        nueva_lista[i-1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i-1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif abs(i - (cantLongitudes - 1)) < i:
        # Si es más cercano al final, sumar con el siguiente
        nueva_lista[i+1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i+1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      else:
        # Si es más cercano al inicio, sumar con el anterior
        nueva_lista[i-1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i-1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      
  if cont != 0:
    test_sequence(nueva_lista_FE,nueva_lista, cantLongitudes)
  
  nueva_lista = [elemento for elemento in nueva_lista if elemento != 0]
  nueva_lista_FE = [elemento for elemento in nueva_lista_FE if elemento != 0]
  
  
  return nueva_lista_FE, nueva_lista

def dataStructure(cantLongitudes, FE, FO):
    operacion = 0
    data = {
    'Longitud de Corrida i': [],
    'Frecuencia Esperada': [],
    'Frecuencia Observada': [],
    'X² = ((FE - FO)²) / FE': [],
    }
    for i in range(cantLongitudes):
        data['Longitud de Corrida i'].append(i)
        data['Frecuencia Esperada'].append(FE[i])
        data['Frecuencia Observada'].append(FO[i])
        data['X² = ((FE - FO)²) / FE'].append(((FE[i] - FO[i])**2) / FE[i])
        operacion += ((FE[i] - FO[i])**2) / FE[i]
    
    return data, operacion

def outDF(data):
  df = pd.DataFrame(data)
  print(df.to_string(index=False))

def main() -> None:
    os.system('clear')
    a = 16807
    m = 10007
    X0 = 17

    cont, n, Xn, rDR, XnMod, numAl = multCM.modular_sequence(a,m,X0)

    baseInterv = [
        0.0, 0.199,
        0.2, 0.399,
        0.4, 0.599,
        0.6, 0.799,
        0.8, 0.999
        ]
    
    
    muestraSinBin = [.411,.819,.191,.037,.894,.575,
                    .730,.281,.408,.541,.995,.233,
                    .553,.469,.392,.598,.434,.668,
                    .719,.791,.213,.770,.671,.156,
                    .383,.771,.914,.826,.018,.984]
    
    
    #muestra = [0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1]
    
    #muestraSinBin = numAl[:cont]
    muestra = binarizacion(muestraSinBin)
    
    #Contar unos
    print("------Unos------")
    longitudesUnos = contarElementos(muestra,0)
    for i in range(len(longitudesUnos)):
        print(f'Longitud({i}): {longitudesUnos[i]}')
        
    #Contar ceros
    print("\n------Ceros------")
    longitudesCeros = contarElementos(muestra,1)
    for i in range(len(longitudesCeros)):
        print(f'Longitud({i}): {longitudesCeros[i]}')
    
    #Longitudes totales
    longitudesTotales = []
    if len(longitudesUnos) >= len(longitudesCeros):
        for i in range(len(longitudesUnos)):
            try:
                longitudesTotales.append(longitudesUnos[i]+longitudesCeros[i])
            except:
                longitudesTotales.append(longitudesUnos[i])
    else:
        for i in range(len(longitudesCeros)):
            try:
                longitudesTotales.append(longitudesCeros[i]+longitudesUnos[i])
            except:
                longitudesTotales.append(longitudesCeros[i])
              
    #Calculo de frecuencias esperadas  
    frecuenciasEsperadas = []
    for i in range(len(longitudesTotales)):
        frecuenciasEsperadas.append((len(muestra)-i+3)/(2**(i+1)))
        
    
    print("\n------Longitudes totales------")
    data, operacion = dataStructure(len(longitudesTotales),frecuenciasEsperadas,longitudesTotales)
    outDF(data)
    
    print("\n------Longitudes totales Corregidos------")
    new_frecuenciasEsperadas, new_longitudesTotales = test_sequence(frecuenciasEsperadas,longitudesTotales,len(longitudesTotales))
        
    data, operacion = dataStructure(len(new_longitudesTotales),new_frecuenciasEsperadas,new_longitudesTotales)
    outDF(data)
    print(operacion)
    
    
    print(f'\nv = ({len(new_longitudesTotales)}-1) = {len(new_longitudesTotales)-1}')
    jiCuadrada = float(input(f'Asumiendo que \'a = 5%\', consulta la tabla de distribucion de Ji-Cuadrada para X²(5%,{len(new_longitudesTotales)-1}) e ingresalo: '))
    
    if operacion < jiCuadrada:
        print(f'\nComo la X² observada ({operacion}) es MENOR que la X²(5%,{len(new_longitudesTotales)-1}) tabulada ({jiCuadrada}), no se puede rechazar la hipótesis de que los números generados provienen de una distribución uniforme.\n\n')
    else:
        print(f'\nComo la X² observada ({operacion}) es MAYOR que la X²(5%,{len(new_longitudesTotales)-1}) tabulada ({jiCuadrada}), es posible rechazar la hipótesis de que los números generados provienen de una distribución uniforme.\n\n')
    

if __name__ == '__main__':
  main()