import multiplicativeCongruentMethod as multCM
import os

def pokerizacion(muestra: list[int],limit: int) -> list[str]:
  return [format(int(element * 100000), '05d') for element in muestra[:limit]]
  
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
  listDiferentes = []
  listUnPar = []
  listDosPares = []
  listTercia = []
  listFull = []
  listPoker = []
  listQuintilla = []
  
  for numero in muestra:  
    if quintilla(numero):
      listQuintilla.append(numero)
      #print(f"QUINTILLA: {numero}")
    
    elif poker(numero):
      listPoker.append(numero)
      #print(f"POKER: {numero}")
    
    elif full(numero):
      listFull.append(numero)
      #print(f"FULL: {numero}")
    
    elif tercia(numero):
      listTercia.append(numero)
      #print(f"TERCIA: {numero}")
    
    elif contar_pares(numero) == 2:
      listDosPares.append(numero)
      #print(f"2 PARES: {numero}")
    
    elif contar_pares(numero) == 1:
      listUnPar.append(numero)
      #print(f"1 PAR: {numero}")
    
    elif todos_diferentes(numero):
      listDiferentes.append(numero)
      #print(f"TODOS DIFERENTES: {numero}")
  
  return listDiferentes, listUnPar, listDosPares, listTercia, listFull, listPoker, listQuintilla


def main() -> None:
  os.system('clear')
  a = 16807
  m = 10007
  X0 = 17

  cont = multCM.modular_sequence(a,m,X0)[0]
  numAl = multCM.modular_sequence(a,m,X0)[-1]
  
  listPokerizada = pokerizacion(numAl,cont)
  
  #Resultados
  print("-----RESULTADOS-----")
  """
  for i in range(59,70):
    print(f"{i+1}: {contar_jugadas_poker(listPokerizada[i])}")
  """
  
  """
  numeros = [
    '72422', '45444', '34633', '77676', '13173', '62783', '24529', '27489', 
    '37149', '43923', '61394', '21569', '28490', '23439', '51505', '88888', 
    '24177', '94949', '59333', '77399', '92992', '67879', '55452', '34347', '45850'
  ]
  """
  
  listDiferentes, listUnPar, listDosPares, listTercia, listFull, listPoker, listQuintilla = contar_jugadas_poker(listPokerizada)
  
  #Diferentes
  print("Diferentes")
  print(f"Cantidad: {len(listDiferentes)}")
  print(listDiferentes)
  
  #UnPar
  print("UnPar")
  print(f"Cantidad: {len(listUnPar)}")
  print(listUnPar)
  
  #DosPares
  print("DosPares")
  print(f"Cantidad: {len(listDosPares)}")
  print(listDosPares)
  
  #Tercia
  print("Tercia")
  print(f"Cantidad: {len(listTercia)}")
  print(listTercia)
  
  #Full
  print("Full")
  print(f"Cantidad: {len(listFull)}")
  print(listFull)
  
  #Poker
  print("Poker")
  print(f"Cantidad: {len(listPoker)}")
  print(listPoker)
  
  #Quintilla
  print("Quintilla")
  print(f"Cantidad: {len(listQuintilla)}")
  print(listQuintilla)
  

if __name__ == "__main__":
  main()