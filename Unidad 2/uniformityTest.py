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
  print("\t-------Tabulacion Principal------\n")
  data = dataStructure(frecEsp,frecObs,sampleLen)
  outDF(data)  
  nueva_lista_FE, nueva_lista_FO, numClas = test_sequence(frecObs, frecEsp, len(frecEsp))
  print("\n\t-------Tabulacion Principal (Ajuste de Clases)------\n")
  data = dataStructure(nueva_lista_FE,nueva_lista_FO,sampleLen)
  outDF(data)
  print("\n\t-------Calculo------\n")
  dataCal, jiCalculada= dataStructureCalculated(nueva_lista_FE,nueva_lista_FO,sampleLen)
  outDF(dataCal)    
  
  print(f'\nv = ({numClas}-1) = {numClas-1}')
  jiCuadrada = float(input(f'Asumiendo que \'a = 5%\', consulta la tabla de distribucion de Ji-Cuadrada para X²(5%,{numClas-1}) e ingresalo: '))
  
  if jiCalculada < jiCuadrada:
    print(f'\nComo la X² observada ({jiCalculada}) es MENOR que la X²(5%,{numClas-1}) tabulada ({jiCuadrada}), no se puede rechazar la hipótesis de que los números generados provienen de una distribución uniforme.\n\n')
  else:
    print(f'\nComo la X² observada ({jiCalculada}) es MAYOR que la X²(5%,{numClas-1}) tabulada ({jiCuadrada}), es posible rechazar la hipótesis de que los números generados provienen de una distribución uniforme.\n\n')
  
  
def dataStructure(frecEsp, frecObs, sampleLen):
    data = {
    'Clase': ['Frecuencia esperada','Frecuencia observada','(FE-FO)²/FE'],
    '0-.199': [f'{frecEsp[0]*len(frecEsp)}/{len(frecEsp)}',frecObs[0],''],
    '.2-.399': [frecEsp[1],frecObs[1],''],
    '.4-.599': [frecEsp[2],frecObs[2],''],
    '.6-.799': [frecEsp[3],frecObs[3],''],
    '.8-.999': [frecEsp[4],frecObs[4],''],
    'Total = 1': [f'Total = {sampleLen}',f'Total = {sampleLen}','']
    }
  
    return data
  
  
def dataStructureCalculated(frecEsp, frecObs, sampleLen):
  resultCal = []
  
  for i in range(len(frecEsp)):
    try:
      resultCal.append((((frecEsp[i]-frecObs[i])**2)/frecEsp[i]))
    except:
      resultCal.append(0)
    
  dataCal = {
    'Clase': ['Frecuencia esperada','Frecuencia observada','(FE-FO)²/FE'],
    '0-.199': [f'{frecEsp[0]*len(frecEsp)}/{len(frecEsp)}',frecObs[0],f'{resultCal[0]:.3f}'],
    '.2-.399': [frecEsp[1],frecObs[1],f'{resultCal[1]:.3f}'],
    '.4-.599': [frecEsp[2],frecObs[2],f'{resultCal[2]:.3f}'],
    '.6-.799': [frecEsp[3],frecObs[3],f'{resultCal[3]:.3f}'],
    '.8-.999': [frecEsp[4],frecObs[4],f'{resultCal[4]:.3f}'],
    'Total = 1': [f'Total = {sampleLen}',f'Total = {sampleLen}',f'Total = {sum(resultCal):.3f}']
    }
  
  return dataCal, sum(resultCal)


def test_sequence(frecObs, frecEsp, limite):
  
  nueva_lista_FO = frecObs[:]  # Copia de la lista original para no modificarla
  nueva_lista_FE = frecEsp[:]  # Copia de la lista original para no modificarla
  cont = 0
  numClas = 0
  for i in range(len(frecObs)):
    if frecObs[i] < limite and frecObs[i] != 0:
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
    else:
      numClas += 1
      
  if cont != 0:
    test_sequence(nueva_lista_FO, nueva_lista_FE, limite)
  
  return nueva_lista_FE, nueva_lista_FO, numClas
    
    
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
  
  """
  muestra = [.411,.819,.191,.037,.894,.575,
                 .730,.281,.408,.541,.995,.233,
                 .553,.469,.392,.598,.434,.668,
                 .719,.791,.213,.770,.671,.156,
                 .383,.771,.914,.826,.018,.984]
  """
  
  muestra = numAl[:cont]
  frecObs = []
  frecEsp = []

  for i in range(0,len(baseInterv)-1,2):
    frecObs.append(counter(muestra,baseInterv[i],baseInterv[i+1]))
  
  for i in range(0,len(baseInterv)-1,2):
    frecEsp.append(int(len(muestra)/(len(baseInterv)/2)))  
  
  test_sequencePlant(len(muestra),baseInterv, frecObs, frecEsp)



if __name__ == '__main__':
  main()