

import pandas as pd
import os
import multiplicativeCongruentMethod as multCM
from fractions import Fraction

def binarizacion(muestra):
    nuevaMuestra = []
    for elemento in muestra:
        if elemento > 0.5:
            nuevaMuestra.append(1)
        else:
            nuevaMuestra.append(0)
    
    return nuevaMuestra

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
    muestra = [0,1,0,0,1,1,1,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1]
    
    """
    print(len(muestra))
    for i in range(0,len(muestra),6):
        print(f'{muestra[i]}\t{muestra[i+1]}\t{muestra[i+2]}\t{muestra[i+3]}\t{muestra[i+4]}\t{muestra[i+5]}')
    """
    
    """
    for i in range(len(muestra)):
        print(f'{muestra[i]},{binarizacion(muestra)[i]}')
    """
    
    #CONTAR UNOS
    
    
    

    
    """
    #muestra = numAl[:cont]
    frecObs = []
    frecEsp = []

    for i in range(0,len(baseInterv)-1,2):
        frecObs.append(counter(muestra,baseInterv[i],baseInterv[i+1]))
    
    for i in range(0,len(baseInterv)-1,2):
        frecEsp.append(int(len(muestra)/(len(baseInterv)/2)))  
    
    test_sequencePlant(len(muestra),baseInterv, frecObs, frecEsp)
    """


if __name__ == '__main__':
  main()