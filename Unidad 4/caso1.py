"""
VAR -> TRUE
MIU -> TRUE
N > 30

ZOBS
"""

from math import sqrt
from validation_tabulation import zTab,desplegar

def zObs(x: int, miu: int, sVar: int, N: int) -> float:
  return (x-miu)/(sVar/sqrt(N))

def main():
  x = 456
  miu = 460
  sVar = 10
  N = 60
  a = 0.02
  
  desplegar(a,zTab(a),zObs(x,miu,sVar,N))
  
if __name__ == '__main__':
  main()