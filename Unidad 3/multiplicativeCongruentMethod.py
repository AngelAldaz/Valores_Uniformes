"""
Formula:
  (a * X_{n-1}) % m

  
  Where:
    a = Multiplicative constant.
    m = Modulus of m.
    X0 = Seed.

  Meeting the following requirements:
    Xn, a, m ≥ 0 --> integers 
    m ≥ a -->  m ≥ X0. 

The formula must be used until a repetition is found.
"""
import pandas as pd
import os

def modular_sequence(a,m,X0) -> tuple:
  n = []
  Xn = [X0]
  rDR = []
  XnMod = []
  numAl = []

  cont = 0
  while True:

    cont+=1
    n.append(cont)
    XnMod.append(((Xn[n[cont-1]-1]*a))%m)
    Xn.append(XnMod[cont-1])
    rDR.append(f"{((Xn[n[cont-1]-1]*a))}/{m} = {int(((Xn[n[cont-1]-1]*a))/m)} + {Xn[cont]}/{m}")
    numAl.append(Xn[cont]/m)

    #print(f"{n[cont-1]} | {Xn[cont-1]} | {rDR[cont-1]} | {XnMod[cont-1]} | {numAl[cont-1]}")

    if numAl.count(numAl[cont-1]) > 1:
      return cont-1, n, Xn, rDR, XnMod, numAl

def main() -> None:
  #Example used:
  a = 16807
  m = 10007
  X0 = 17

  cont, n, Xn, rDR, XnMod, numAl = modular_sequence(a,m,X0)

  data = {
    'n': n[:cont],
    'Xn': Xn[:cont],
    'Relacion de recurrencia': rDR[:cont],
    'Xn (mod)': XnMod[:cont],
    '# Aleatorio': numAl[:cont]
    }
  
  df = pd.DataFrame(data)
  print(df.head().to_string(index=False))
  print("--------------------------------------------------------------------------------")
  print(df.tail().to_string(index=False))
  print(f"\nTotal = {sum(numAl[:cont])}")




if __name__ == '__main__':
  os.system('clear')
  main()