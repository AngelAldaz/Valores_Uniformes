import multiplicativeCongruentMethod as multCM
import os
import pandas as pd

def pokerizacion(muestra: list[int]) -> list[str]:
  return [format(int(element * 100000), '05d') for element in muestra]
  
def todos_diferentes(numero):
  return len(set(numero)) == 5

def contar_pares(numero):
  cuenta_pares = sum(numero.count(digito) // 2 for digito in set(numero))
  return cuenta_pares

def tercia(numero):
  for digito in set(numero):
    if numero.count(digito) == 3:
      return True
  return False

def full(numero):
  # Obtener la cuenta de ocurrencias de cada dígito en el número
  digit_counts = {digito: numero.count(digito) for digito in set(numero)}
  
  # Verificar si hay exactamente una tercia y exactamente un par
  tercia_present = False
  par_present = False

  for count in digit_counts.values():
    if count == 3:
      tercia_present = True
    elif count == 2:
      par_present = True
  
  return tercia_present and par_present

def poker(numero):
  for digito in set(numero):
    if numero.count(digito) == 4:
      return True
  return False

def quintilla(numero):
  for digito in set(numero):
    if numero.count(digito) == 5:
      return True
  return False

def contar_jugadas_poker(muestra):
  resultados = {
        'Todos diferentes': [],
        'Un par': [],
        'Dos pares': [],
        'Una tercia': [],
        'Full': [],
        'Poker': [],
        'Quintilla': []
    }
  
  for numero in muestra:  
    if quintilla(numero):
      resultados['Quintilla'].append(numero)
      #print(f"QUINTILLA: {numero}")
    
    elif poker(numero):
      resultados['Poker'].append(numero)
      #print(f"POKER: {numero}")
    
    elif full(numero):
      resultados['Full'].append(numero)
      #print(f"FULL: {numero}")
    
    elif tercia(numero):
      resultados['Una tercia'].append(numero)
      #print(f"TERCIA: {numero}")
    
    elif contar_pares(numero) == 2:
      resultados['Dos pares'].append(numero)
      #print(f"2 PARES: {numero}")
    
    elif contar_pares(numero) == 1:
      resultados['Un par'].append(numero)
      #print(f"1 PAR: {numero}")
    
    elif todos_diferentes(numero):
      resultados['Todos diferentes'].append(numero)
      #print(f"TODOS DIFERENTES: {numero}")
  
  return resultados

def dataStructure(cantLongitudes:int, resultados:dict, totalMuestra:int):
    data = {
    'Clase (i)': [],
    'Probabilidad Teorica de (i) P(i)': [],
    'Frecuencia esperada de (i) Fe(i)=P(i)*n': [],
    'Frecuencia observada de (i) Fo(i)': [],
    'X²(i)': [],
    }
    pTeorica = [0.3024,0.5040,0.1080,0.0720,0.0090,0.0045,0.0001]
    for i in range(cantLongitudes):
      data['Clase (i)'].append(list(resultados.keys())[i])
      data['Probabilidad Teorica de (i) P(i)'].append(pTeorica[i])
      data['Frecuencia esperada de (i) Fe(i)=P(i)*n'].append(pTeorica[i]*totalMuestra)
      data['Frecuencia observada de (i) Fo(i)'].append(len(resultados[list(resultados.keys())[i]]))
      data['X²(i)'].append(((data['Frecuencia esperada de (i) Fe(i)=P(i)*n'][i]-data['Frecuencia observada de (i) Fo(i)'][i])**2)/data['Frecuencia esperada de (i) Fe(i)=P(i)*n'][i])
    
    return data

def outDF(data):
  df = pd.DataFrame(data)
  print(df.to_string(index=False))

def test_sequence(FE,fo, cantFO):
  
  nueva_lista = fo[:]  # Copia de la lista original para no modificarla
  nueva_lista_FE = FE[:]  # Copia de la lista original para no modificarla
  cont = 0
  for i in range(len(fo)):
    if fo[i] < cantFO and fo[i] != 0:
      cont += 1
      # Si el número es menor que la longitud de la lista, sumarlo con su vecino más cercano
      if i == 0:
        # Si es el primer número, sumar con el siguiente
        nueva_lista[i+1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i+1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif i == cantFO - 1:
        # Si es el último número, sumar con el anterior
        nueva_lista[i-1] += nueva_lista[i]
        nueva_lista[i] = 0
        nueva_lista_FE[i-1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif abs(i - (cantFO - 1)) < i:
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
    test_sequence(nueva_lista_FE,nueva_lista, len(nueva_lista))
  
  nueva_lista = [elemento for elemento in nueva_lista if elemento != 0]
  nueva_lista_FE = [elemento for elemento in nueva_lista_FE if elemento != 0]
  
  
  return nueva_lista_FE, nueva_lista



def main() -> None:
  os.system('clear')
  a = 16807
  m = 10007
  X0 = 17

  cont = multCM.modular_sequence(a,m,X0)[0]
  numAl = multCM.modular_sequence(a,m,X0)[-1]
  
  numeros = [
    .72422, .45444, .34633, .77676, .13173, .62783, .24529, .27489, 
    .37149, .43923, .61394, .21569, .28490, .23439, .51505, .88888, 
    .24177, .94949, .59333, .77399, .92992, .67879, .55452, .34347, .45850
  ]
  
  #listPokerizada = pokerizacion(numAl[:cont])
  listPokerizada = pokerizacion(numeros)
  
  #Resultados
  resultados = contar_jugadas_poker(listPokerizada)
  
  data = dataStructure(len(resultados), resultados, len(listPokerizada))
  outDF(data)
  nueva_lista_FO, nueva_lista = test_sequence(data['Frecuencia esperada de (i) Fe(i)=P(i)*n'],data['Frecuencia observada de (i) Fo(i)'], len(data['Frecuencia observada de (i) Fo(i)']))
  
  print(nueva_lista_FO)
  print(nueva_lista)
  
  #n = list(resultados.keys())
  #print(list(resultados.keys()))
  """
  print("-----RESULTADOS-----")
    
  #Diferentes
  print("Diferentes")
  print(f"Cantidad: {len(resultados['Todos diferentes'])}")
  print(resultados['Todos diferentes'])
  
  #UnPar
  print("UnPar")
  print(f"Cantidad: {len(resultados['Un par'])}")
  print(resultados['Un par'])
  
  #DosPares
  print("DosPares")
  print(f"Cantidad: {len(resultados['Dos pares'])}")
  print(resultados['Dos pares'])
  
  #Tercia
  print("Tercia")
  print(f"Cantidad: {len(resultados['Una tercia'])}")
  print(resultados['Una tercia'])
  
  #Full
  print("Full")
  print(f"Cantidad: {len(resultados['Full'])}")
  print(resultados['Full'])
  
  #Poker
  print("Poker")
  print(f"Cantidad: {len(resultados['Poker'])}")
  print(resultados['Poker'])
  
  #Quintilla
  print("Quintilla")
  print(f"Cantidad: {len(resultados['Quintilla'])}")
  print(resultados['Quintilla'])
  
  """

if __name__ == "__main__":
  main()