from math import sqrt
from validation_tabulation import zTabNormal,desplegar,tTabStudent
from typing import Optional
import scipy.stats as s

class Cases:
  
  def __init__(self,x: Optional[int] = None, miu: Optional[int] = None, sVar: Optional[int] = None, N: Optional[int] = None, a:Optional[float] = None, x1: Optional[int] = None, x2: Optional[int] = None, N1: Optional[int] = None, N2: Optional[int] = None, desvEstandar: Optional[float] = None, s1: Optional[float] = None, s2: Optional[float] = None) -> None:
    self.x = x
    self.miu = miu
    self.sVar = sVar
    self.N = N
    self.a = a
    self.x1 = x1
    self.x2 = x2
    self.N1 = N1
    self.N2 = N2
    self.desvEstandar = desvEstandar
    self.s1 = s1
    self.s2 = s2
      
  def accion(self):
    cases = [self.caseOne, self.caseTwo, self.caseThree, self.eval]
    
    for case in cases:
      try:
        case()
        break  # Si se ejecuta correctamente, salimos del bucle
      except Exception as e:
        #print(e)
        continue
      
  def eval(self):
    if self.s1 == self.s2:
      if (self.N1 + self.N2) > 30:
        self.caseFour()
      else:
        self.caseFive()
    else:
      if (self.N1 > 30 and self.N1 == self.N2) or (self.N2 > 30 and self.N1 != self.N2):
        self.caseSix()
      else:
        print("nada")
          
  def caseOne(self):
    """
    VAR -> TRUE
    MIU -> TRUE
    N > 30

    ZOBS
    """
    r = (self.x-self.miu)/(self.sVar/sqrt(self.N))
    print("Caso 1\n")
    desplegar(self.a,zTabNormal(self.a),r)
    
  def caseTwo(self):
    """
    VAR -> TRUE
    MIU -> FALSE
    (N1N2) >= 30

    ZOBS
    """
    r = ((self.x1-self.x2)/((self.sVar/self.N1)+(self.sVar/self.N2)))
    print("Caso 2\n")
    desplegar(self.a,zTabNormal(self.a),r)

  def caseThree(self):
    r = (self.x-self.miu)/(self.desvEstandar/sqrt(self.N))
    print("Caso 3\n")
    if self.N < 30:
      desplegar(self.a,tTabStudent(self.a,self.N),r)
    else:
      desplegar(self.a,zTabNormal(self.a),r)
  
  def caseFour(self):
    r = (self.x1-self.x2)/((self.s1/self.N1)+(self.s2/self.N2))
    print("Caso 4\n")
    desplegar(self.a,zTabNormal(self.a),r)
  
  def caseFive(self):
    r = ( self.x1 - self.x2 ) / ( ( sqrt(((self.s1*self.N1)+ (self.s2*self.N2))/((self.N1+self.N2)/2)) ) * ( sqrt( ( 1 / self.N1 ) + ( 1 / self.N2 ) )  ) )
    print("Caso 5\n")
    desplegar(self.a,tTabStudent(self.a, (self.N1 + self.N2 - 1)),r)
  
  def caseSix(self):
    r = (self.x1 - self.x2) / sqrt( ( self.s1 / ( self.N1 - 1 ) ) + ( self.s2 / ( self.N2 - 1 ) ) )
    print("Caso 6\n")
    desplegar(self.a,zTabNormal(self.a),r)
    
def main():
  """
  #CASO 1
  x = 249.7
  miu = 245
  sVar = 10
  N = 31
  a = 0.05
  c = Cases(x=x,miu=miu,sVar=sVar,N=N,a=a)
  """
  """
  #CASO 2
  x1 = 23
  x2 = 25
  N1 = 30
  N2 = 40
  sVar = 3.1
  a = 0.05
  c = Cases(x= None, miu= None, sVar = sVar, N = None, a = a, x1 = x1, x2 = x2, N1 = N1, N2 = N2)
  """
  
  """
  #CASO 3 CUANDO N < 30
  x = 80
  desvEstandar = 10
  N = 20
  a = 0.05
  miu =  75
  """
  """
  #CASO 3 CUANDO N >= 30
  x = 21
  desvEstandar = 2
  N = 50
  a = 0.05
  miu =  21
  c = Cases(x = x, miu = miu, sVar = None, N = N, a = a, x1 = None, x2 = None, N1 = None, N2 = None, desvEstandar = desvEstandar)
  """
  """
  #CASO 4
  N1 = 40
  N2 = 50
  s1 = 3.5
  s2 = 3.5
  x1 =  48.5
  x2 = 34.7
  a = 0.05
  c = Cases(N1 = N1, N2 = N2, s1 = s1, s2 = s2, x1 = x1, x2 = x2, a = a)
  """
  """
  #CASO 4
  N1 = 13
  N2 = 11
  s1 = 49.0769
  s2 = 49.0769
  x1 =  91.9231
  x2 = 94.37
  a = 0.05
  c = Cases(N1 = N1, N2 = N2, s1 = s1, s2 = s2, x1 = x1, x2 = x2, a = a)
  """
  
  
  #CASO 6
  N1 = 12
  N2 = 32
  s1 = 2396.0071
  s2 = 1440.0606
  x1 =  147.8437
  x2 = 182.6666
  a = 0.05
  c = Cases(N1 = N1, N2 = N2, s1 = s1, s2 = s2, x1 = x1, x2 = x2, a = a)
  
  c.accion()

if __name__ == '__main__':
  main()