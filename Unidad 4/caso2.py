"""
VAR -> TRUE
MIU -> FALSE
(N1N2) >= 30

ZOBS
"""

from validation_tabulation import zTabNormal,desplegar

def zObs(x1: int, x2: int, varianza: int, N1: int, N2: int) -> float:
  return ((x1-x2)/((varianza/N1)+(varianza/N2)))

def main():
  N1 = 30
  N2 = 40
  X1 = 23
  X2 = 25
  varianza = 3.1
  a = 0.05
  
  desplegar(a,zTabNormal(a),zObs(X1,X2,varianza,N1,N2))
  
  
if __name__ == '__main__':
  main()