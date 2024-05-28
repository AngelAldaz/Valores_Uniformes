import scipy.stats as s

def valid(tab,obs):
  if obs < tab:
    return f"Como ZObs({obs}) es menor que zTab({tab}) entonces RECHAZAMOS la representatividad del simualdor"
  else:
    return f"Como ZObs({obs}) es mayor que zTab({tab}) entonces NO rechazamos la representatividad del simualdor"

def zTab(a:float) -> float:
  return s.norm.ppf(a/2)

def desplegar(a:float, tabulada:float, observada:float):
  print(f"Z Tabulada: {tabulada}")
  print(f"Z observada: {observada} \n")
  print(valid(tabulada,observada))