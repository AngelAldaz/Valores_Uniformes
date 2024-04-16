"""
Formula:
  
  X² = sum(FOi - FEi)² / FEi
  
  WHERE:
  
    FOi: observed frequency of subinterval i (how many values were observed in the respective interval).

    FEi: expected frequency of subinterval i.

  N: sample size.

  n: number of subintervals or classes.

  The actual or observed chi-square statistic X² is compared with the tabulated or theoretical chi-square statistic X² for a significance level "a" and with n-1 degrees of freedom.

  If the observed X² is less than or equal to the theoretical X²__(a, n-1), the hypothesis that the sample comes from a uniform distribution cannot be rejected.
"""

import pandas as pd
import os
import multiplicativeCongruentMethod as multCM
from fractions import Fraction



def test_sequencePlant(sampleLen, baseInterv, frecObs, frecEsp):
  
  data = {
    'Clase': ['Frecuencia esperada','Frecuencia observada','(FE-FO)²/FE'],
    '0-.199': [f'{frecEsp[0]*len(frecEsp)}/{len(frecEsp)}',frecObs[0],''],
    '.2-.399': [frecEsp[1],frecObs[1],''],
    '.4-.599': [frecEsp[2],frecObs[2],''],
    '.6-.799': [frecEsp[3],frecObs[3],''],
    '.8-.999': [frecEsp[4],frecObs[4],''],
    'Total = 1': [f'Total = {sampleLen}',f'Total = {sampleLen}','']
    }

  outDF(data)  
  test_sequence([8, 4, 8, 4, 4], frecEsp, len(frecEsp))

def test_sequence(frecObs, frecEsp, limite):
  print("-------inicio------")
  print(frecEsp)
  print(frecObs)
  nueva_lista_FO = frecObs[:]  # Copia de la lista original para no modificarla
  nueva_lista_FE = frecEsp[:]  # Copia de la lista original para no modificarla
  cont = 0
  for i in range(len(frecObs)):
    if frecObs[i] < limite:
      cont += 1
      # Si el número es menor que la longitud de la lista, sumarlo con su vecino más cercano
      if i == 0:
        # Si es el primer número, sumar con el siguiente
        nueva_lista_FO[i+1] += nueva_lista_FO[i]
        nueva_lista_FO[i] = 0
        nueva_lista_FE[i+1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif i == limite - 1:
        # Si es el último número, sumar con el anterior
        nueva_lista_FO[i-1] += nueva_lista_FO[i]
        nueva_lista_FO[i] = 0
        nueva_lista_FE[i-1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      elif abs(i - (limite - 1)) < i:
        # Si es más cercano al final, sumar con el siguiente
        nueva_lista_FO[i+1] += nueva_lista_FO[i]
        nueva_lista_FO[i] = 0
        nueva_lista_FE[i+1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0
      else:
        # Si es más cercano al inicio, sumar con el anterior
        nueva_lista_FO[i-1] += nueva_lista_FO[i]
        nueva_lista_FO[i] = 0
        nueva_lista_FE[i-1] += nueva_lista_FE[i]
        nueva_lista_FE[i] = 0


    # Limpia los elementos cero de las listas
  nueva_lista_FO = [elemento for elemento in nueva_lista_FO if elemento != 0]
  nueva_lista_FE = [elemento for elemento in nueva_lista_FE if elemento != 0]
  
  if cont != 0:
    test_sequence(nueva_lista_FO, nueva_lista_FE, limite)
  else:
    print("-------------")
    print(nueva_lista_FE)
    print(nueva_lista_FO)


    


  
   

def outDF(data):
  df = pd.DataFrame(data)
  print(df.to_string(index=False))

def counter(samp,base,top):
  cont = 0
  for s in samp:
    if s >= base and s <= top:
      cont += 1
  return cont

def FoValidation(cantClass,foValue):
  results = []
  for i in foValue:
    results.append(i>=cantClass)
  return results

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
  
  muestra = [.411,.819,.191,.037,.894,.575,
                 .730,.281,.408,.541,.995,.233,
                 .553,.469,.392,.598,.434,.668,
                 .719,.791,.213,.770,.671,.156,
                 .383,.771,.914,.826,.018,.984]
  frecObs = []
  frecEsp = []

  for i in range(0,len(baseInterv)-1,2):
    frecObs.append(counter(muestra,baseInterv[i],baseInterv[i+1]))
  
  for i in range(0,len(baseInterv)-1,2):
    frecEsp.append(int(len(muestra)/(len(baseInterv)/2)))
  
  
  
  test_sequencePlant(len(muestra),baseInterv, frecObs, frecEsp)
  #test_sequence(numAl[:cont])

if __name__ == '__main__':
  main()