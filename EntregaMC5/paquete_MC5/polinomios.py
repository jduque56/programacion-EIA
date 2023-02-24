from numpy import sqrt as sq
from numpy import cbrt as cb

def polyval(pol, x):
    y = 0
    orden = len(pol) - 1
    for i, coef in enumerate(pol):
        y += coef*x**(orden-i)
    return y


def polyder(pol):
    der = list(pol)
    der.pop()
    orden = len(der)
    for i, a in enumerate(der):
        der[i] *= orden - i
    return der


def polyconv(pol1, pol2):
    orden1, orden2 = len(pol1) - 1, len(pol2) - 1
    if orden1 < 0 or orden2 < 0:
        producto = None
    else:
        orden = orden1 + orden2
        producto = [0]*(orden + 1)
        for i, elem1 in enumerate(pol1):
            for j, elem2 in enumerate(pol2):
                producto[i + j] += elem1*elem2
    return producto

def raices(*args):
    """
    funcion para encontrar raices de polinomio de hasta grado 4
    raices(*args)

    parametros
    ----------
    args: lista con los coeficientes en orden descendiente

    retorna
    -------
    raices: lista con las raices del polinomio 

    ejemplos
    
    x=raices(2,3)
    print(x)
    """
    #estructura match case
    match len(args):
        case 2:
            raiz_1 = float((-1*args[0])/args[1])
            raices = [raiz_1]
            return raices
        case 3:
            raiz_1 = float((-args[1]+sq(args[1]**2-(4*args[0]*args[2])))/(2*args[0]))
            raiz_2 = float((-args[1]-sq(args[1]**2-(4*args[0]*args[2])))/(2*args[0]))
            raices = [raiz_1,raiz_2]
        case 4:
            args = [args[0]/args[0],args[1]/args[0],args[2]/args[0],args[3]/args[1]]
            p = float(args[2]-(args[1]**2 / 3))
            q = float(args[3]-((args[1]*args[2])/3)+((2 * args[1]**3)/27))
            dsc = (q**2 / 4.0) + (p**3 / 27.0)
            alp = cb((-1.0*q/2) + sq(dsc))
            bt = cb((-1.0*q/2) - sq(dsc))
            raiz_1 = 
            raiz_2 = 
            raiz_3 = 



if __name__ == '__main__':
    pol = [4, 3, 2, 1]
    assert polyder(pol) == [12, 6, 2]
    print('Test -> polyder(pol) == [12, 6, 2]\nOk')
    assert polyval(pol, 0.) == 1.
    print('Test -> polyval(pol, 0.) == 1.\nOk')
    assert polyval(pol, 1.) == 10.
    print('Test -> polyval(pol, 1.) == 10.\nOk')
    assert polyval(pol, 2.) == 49.
    print('Test -> polyval(pol, 2.) == 49.\nOk')
    assert polyconv(pol, pol) == [16, 24, 25, 20, 10, 4, 1]
    print('Test -> polyconv(pol, pol) == [16, 24, 25, 20, 10, 4, 1]\nOk')