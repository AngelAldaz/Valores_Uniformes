from math import sqrt
from validation_tabulation import zTab,desplegar
from typing import Optional
class Cases:
  
  def __init__(self,x: Optional[int] = None, miu: Optional[int] = None, sVar: Optional[int] = None, N: Optional[int] = None, a:Optional[float] = None, x1: Optional[int] = None, x2: Optional[int] = None, N1: Optional[int] = None, N2: Optional[int] = None) -> None:
    self.x = x
    self.miu = miu
    self.sVar = sVar
    self.N = N
    self.a = a
    self.x1 = x1
    self.x2 = x2
    self.N1 = N1
    self.N2 = N2
    
    print(self.x,self.miu,self.sVar,self.N,self.a,self.x1,self.x2,self.N1,self.N2)
  
  def accion(self):
    try:
      self.caseOne()
    except:
      self.caseTwo()
    
  def caseOne(self):
    """
    VAR -> TRUE
    MIU -> TRUE
    N > 30

    ZOBS
    """
    r = (self.x-self.miu)/(self.sVar/sqrt(self.N))
    print("Caso 1\n")
    desplegar(self.a,zTab(self.a),r)
    
  def caseTwo(self):
    """
    VAR -> TRUE
    MIU -> FALSE
    (N1N2) >= 30

    ZOBS
    """
    r = ((self.x1-self.x2)/((self.sVar/self.N1)+(self.sVar/self.N2)))
    print("Caso 2\n")
    desplegar(self.a,zTab(self.a),r)
    

def main():
  """
  #CASO 1
  x = 90
  miu = 85
  sVar = 7
  N = 100
  a = 0.03
  c = Cases(x=x,miu=miu,sVar=sVar,N=N,a=a)
  c.accion()
  """
  ""
  #CASO 2
  x1 = 23
  x2 = 25
  N1 = 30
  N2 = 40
  sVar = 3.1
  a = 0.05
  #c = Cases(x1=x1,x2=x2,N1=N1,N2=N2,sVar=sVar, a=a)
  c = Cases(x= None, miu= None, sVar = sVar, N = None, a = a, x1 = x1, x2 = x2, N1 = N1, N2 = N2)
  c.accion()
  
  
  ""
  
  

if __name__ == '__main__':
  main()