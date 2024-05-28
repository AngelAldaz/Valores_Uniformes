import scipy.stats as s

def valid(tab,obs):
  if obs < tab:
    return f"Como ZObs({obs:.4f}) es menor que zTab({tab:.4f}) entonces RECHAZAMOS la representatividad del simualdor"
  else:
    return f"Como ZObs({obs:.4f}) es mayor que zTab({tab:.4f}) entonces NO rechazamos la representatividad del simualdor"

def zTab(a:float) -> float:
  return s.norm.ppf(a/2)

def desplegar(a:float, tabulada:float, observada:float):
  print(f"Z Tabulada: {tabulada:.4f}")
  print(f"Z observada: {observada:.4f} \n")
  print(valid(tabulada,observada))