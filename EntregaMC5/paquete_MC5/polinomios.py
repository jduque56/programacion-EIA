import cmath
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
    funcion para encontrar raices de polinomio de hasta grado 3
    raices(*args)

    parametros
    ----------
    args: lista con los coeficientes en orden descendiente, del coficiente de la mayor variable a la menor

    retorna
    -------
    respuesta: lista con las raices del polinomio 

    ejemplos
    
    print(raices(2,3))
    """
    #estructura match case
    match len(args):
        case 2:
            raiz_1 = float((-1*args[1])/args[0])
            respuesta = [raiz_1]
            return respuesta
        case 3:
            a = args[1]**2-(4*args[0]*args[2])
            b = args[1]**2-(4*args[0]*args[2])
            raiz_1 = (-args[1]+a**(1/2)/(2*args[0]))
            raiz_2 = (-args[1]-b**(1/2))/(2*args[0])
            respuesta = [raiz_1,raiz_2]
            return respuesta
        case 4:
            args = [args[0]/args[0],args[1]/args[0],args[2]/args[0],args[3]/args[1]]
            p = float(args[2]-(args[1]**2 / 3))
            q = float((2*args[1]**2)/27 - (args[1]*args[2])/3 + args[3])
            dsc = q**2 + (4 * p**3)/27
            if dsc > 0:
                aux_1 = float((-1*p+dsc**(1/2))/2)
                aux_2 = float((-1*q-dsc**(1/2))/2)
                u = aux_1**(1/3)
                v = aux_2**(1/3)
                raiz_1 = u+v
                raiz_2 = complex(-(raiz_1/2),(3**(1/2)*(u-v))/2)
                raiz_3 = complex(-(raiz_1/2),-(3**(1/2)*(u-v))/2)
                respuesta = [raiz_1,raiz_2,raiz_3]
                return respuesta
            elif dsc == 0:
                if p == 0 and q == 0:
                    respuesta = ["0","0","0"]
                    return respuesta
                else: 
                    raiz_1 = 3*q/p
                    raiz_2 = (-3*q)/(2*p)
                    respuesta = [raiz_1,raiz_2]
                    return respuesta
            else:
                dsc=-1*dsc 
                uc = (complex(-q,dsc**(1/2)))/2
                vc = (complex(-q,-dsc**(1/2)))/2
                u = uc**(1/3)
                v = vc**(1/3)
                w_1=complex(-1/2,3**(1/2)/2)
                w_2=complex(-1/2,-3**(1/2)/2)
                raiz_1=u+v
                raiz_2=w_1*u + (w_1**2)*v
                raiz_3=w_2*u + (w_2**2)*v
                respuesta = [raiz_1,raiz_2,raiz_3]
                return respuesta
            
def raices_4 (*args):
    """
    funcion para calcular las raices de un polinomio de grado 4
    raices_4(*args)

    parametros
    ---------
    args: lista con los coeficientes en orden descendiente, del coficiente de la mayor variable a la menor

    retorna
    -------
    respuesta: lista con con las raices del polinomio
    """
    args = [args[0]/args[0],args[1]/args[0],args[2]/args[0],args[3]/args[0],args[4]/args[0]]
    f = float(args[2] - ((3*(args[1]**2))/8))
    g = float(args[3] + (args[1]**3 / 8) - (args[1]*args[2] / 2))
    h = float(args[4] - (3 * (args[1]**4)) / 256 + ((args[1]**2)*args[2]) / 16 - (args[1]*args[3]) / 4)
    a = 1
    b = f/2
    c = ((f**2 - 4*h)/16)
    d = -g**2 / 64
    r_3 = []
    r_3.append(raices(a,b,c,d))
    sq = []
    print(r_3[0][1])
    for i in range(0,3,1):
        if r_3[0][i] != complex(0.0,0.0):
            sq.append(r_3[0][i])
        print (i)
    print (sq)
    e = sq[0][0]
    k = sq[0][1]
    sq_1 = a.real
    sq_2 = a.imag * 1j
    sq_3 = k.real
    sq_4 = k.imag * 1j
    q = cmath.sqrt(complex(sq_3,sq_4))
    r = -g/(8*p*q)
    s = float(args[1]/(4*args[0]))
    raiz_1 = p+q+r-s
    raiz_2 = p-q-r-s
    raiz_3 = -p+q-r-s
    raiz_4 = -p-q+r-s
    respuesta = [raiz_1,raiz_2,raiz_3,raiz_4]
    return respuesta 

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
    assert raices(1,2) == [-2.0]
    print("Test -> raices(1,2) == [-2.0].\nOk")
    assert raices(3,5,7) == [-5+1.2801909579781012j, -0.8333333333333335-1.2801909579781012j]
    print("Test -> raices(3,5,7) == [-5+1.2801909579781012j, -0.8333333333333335-1.2801909579781012j].\nOk")
    assert raices(3,5,7,9) == [0.7746668555916785+1.3417623528244094j, -0.13776329695122339-0.8149705586370338j, -0.6369035586404551-0.5267917941873755j]
    print("Test -> raices(3,5,7,9) == [0.7746668555916785+1.3417623528244094j, -0.13776329695122339-0.8149705586370338j, -0.6369035586404551-0.5267917941873755j].\nOk")
