import scipy.stats as s

def valid(tab,obs):
  if obs < tab:
    return f"Como el valor OBSERVADO({obs:.4f}) es menor que el valor TABULADO({tab:.4f}) entonces RECHAZAMOS la representatividad del simualdor"
  else:
    return f"Como el valor OBSERVADO({obs:.4f}) es mayor que el valor TABULADO({tab:.4f}) entonces NO rechazamos la representatividad del simualdor"

def zTabNormal(a:float) -> float:
  return s.norm.ppf(a/2)

def tTabStudent(a:float, N:float) -> float:
  return s.t.ppf(a/2,N-1)

def desplegar(a:float, tabulada:float, observada:float):
  print(f"Valor TABULADO: {tabulada:.4f}")
  print(f"Valor OBSERVADO: {observada:.4f} \n")
  print(valid(tabulada,observada))