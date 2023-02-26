import numpy 


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
            raiz_1 = float((-args[1]+numpy.sqrt(args[1]**2-(4*args[0]*args[2])))/(2*args[0]))
            raiz_2 = float((-args[1]-numpy.sqrt(args[1]**2-(4*args[0]*args[2])))/(2*args[0]))
            raices = [raiz_1,raiz_2]
        case 4:
            args = [args[0]/args[0],args[1]/args[0],args[2]/args[0],args[3]/args[1]]
            p = float(args[2]-(args[1]**2 / 3))
            q = float((2*args[1]**2)/27 - (args[1]*args[2])/3 + args[3])
            dsc = q**2 + (4 * p**3)/27
            if dsc > 0:
                u = numpy.cbrt((-1*p+numpy.sqrt(dsc))/2)
                v = numpy.cbrt((-1*q-numpy.sqrt(dsc))/2)
                raiz_1 = u+v
                raiz_2 = complex(-(raiz_1/2),(numpy.cbrt(3)*u-v)/2)
                raiz_3 = complex(-(raiz_1/2),-(numpy.sqrt(3)*u-v)/2)
                raices = [raiz_1,raiz_2,raiz_3]
                return raices
            elif dsc == 0:
                if p == 0 and q == 0:
                    raices = ["0","0","0"]
                    return raices
                else: 
                    raiz_1 = 3*q/p
                    raiz_2 = (-3*q)/(2*p)
                    raices = [raiz_1,raiz_2]
                    return raices
            else:
                dsc=-1*dsc 
                uc = (complex(-q,+numpy.sqrt(dsc)))/2
                vc = (complex(-q,-numpy.sqrt(dsc)))/2
                u = uc**(1/3)
                v = vc**(1/3)
                w_1=complex(-1/2,numpy.sqrt(3)/2)
                w_2=complex(-1/2,-numpy.sqrt(3)/2)
                raiz_1=u+v
                raiz_2=w_1*u + (w_1**2)*v
                raiz_3=w_2*u + (w_2**2)*v
                raices = [raiz_1,raiz_2,raiz_3]
                return raices
        case 5:
            args = [args[0]/args[0],args[1]/args[0],args[2]/args[0],args[3]/args[0],args[4]/args[0]]
            p = args[2] - (3/8)*(args[1]**2)
            q = args[3] - (1/2)*(args[1]*args[2]) + (1/8) * args[1]**3
            r = args[4] - (1/4)*(args[1]*args[3]) + (1/16) * (args[1]**3) * args[2] - (3/25) * (args[1]**4)
            b = 2*p
            c = (p**2 - 4*r) 
            d = (-1 * q**2)
            raices_3 = raices(b,c,d)
            y = raices_3[0]
            raiz_1 = (numpy.sqrt(y)+numpy.sqrt(-y-(2*p)-(2*q)/numpy.sqrt(y)))/2 - args[1]/4
            raiz_2 = (numpy.sqrt(y)-numpy.sqrt(-y-(2*p)-(2*q)/numpy.sqrt(y)))/2 - args[1]/4
            raiz_3 = (-1*numpy.sqrt(y)+numpy.sqrt(-y-(2*p)-(2*q)/numpy.sqrt(y)))/2 - args[1]/4
            raiz_4 = (-1*numpy.sqrt(y)-numpy.sqrt(-y-(2*p)-(2*q)/numpy.sqrt(y)))/2 - args[1]/4
            raices = [raiz_1, raiz_2, raiz_3, raiz_4]
            return raices 

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