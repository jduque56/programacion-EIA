import numpy

def metro_pie(b,u):
    """
    funcion para convertir de metro a pie o de pie a metro
    metro_pie(b,u)

    parametros
    ----------
    u: int o float a convertir
    b: string que indica si estan en ft o m

    retorna
    -------
    u: float convertido

    ejemplos

    print(metro_pie("ft",25.5))
    """
    b = b.lower().strip()
    if b != "ft" and b != "m":
        print("error, ingrese tal cual 'ft' o 'm'")
    elif b == "m":
        u=float(u*3.28084)
        return u
    elif b == "ft":
        u=float(u/3.28084)
        return u

def hectarea_metro_cuadrado(b,u):
    """
    funcion para convertir de hectarea a metro cuadrado o viceversa
    hectarrea_metro_cuadrado(b,u)

    parametros
    ----------
    u: int o float a convertir
    b: string que indica si estan en ha o m2

    retorna
    -------
    u: float convertido 

    ejemplos
    
    print(hectarrea_metro_cuadrado("ha", 25.5))
    """
    b = b.lower().strip()
    if b != "ha" and b != "m2":
        print("error, ingrese tal cual 'ha' o 'm2'")
    elif b == "ha":
        u=float(u*10000)
        return u
    elif b == "m2":
        u=float(u/10000)
        return u
    
def bar_psi(b,u):
    """
    funcion para convertir de bar a psi o viceversa
    bar_psi(b,u)

    parametros
    ----------
    u: int o float a convertir
    b: string que indica si estan en bar o psi

    retorna
    -------
    u: float convertido

    ejemplos
    print(bar_psi("bar", 25.5))
    """
    b = b.lower().strip()
    if b != "bar" and b != "psi":
        print("error, ingrese tal cual 'bar' o 'psi'")
    elif b == "bar":
        u=float(u*14.5038)
        return u
    elif b == "psi":
        u=float(u/14.5038)
        return u
    
def celsius_fahrenheit(b,u):
    """
    funcion para convertir de celsius a farehnheit o viceversa
    celsius_fahrenheit(b,u)

    parametros
    ----------
    u: int o float a convertir
    b: string que indica si estan en C o F

    retorna
    -------
    u: float convertido 

    ejemplos
    
    print(celcius_farehnheit("C", 25.5))
    """
    b = b.upper().strip()
    if b != "C" and b != "F":
        print("error, ingrese tal cual 'C' o 'F'")
    elif b == "C":
        u=float((u*(9/5)) + 32)
        return u
    elif b == "F":
        u=float((u-32)*(5/9))
        return u

def newton_kilopondio(b,u):
    """
    funcion para convertir de Newton a Kilopondio o viceversa
    newton_kilopondio(b,u)

    parametros
    ----------
    u: int o float a convertir
    b: string que indica si estan en N o kp

    retorna
    -------
    u: float convertido

    ejemplos
    
    print(newton_kilopondio("N", 25.5))
    """
    b = b.upper().strip()
    if b != "N" and b != "KP":
        print("error, ingrese tal cual 'N' o 'kp'")
    elif b == "N":
        u=float(u*0.101972)
        return u
    elif b == "KP":
        u=float(u/0.101972)
        return u

def rads_rpm(b,u):
    """
    funcion para convertir de rad/s a rpm o viceversa
    tads_rpm(b,u)

    parametros
    ----------
    u: int o float a convertir 
    b: string que indica si estan en rad/s o rpm

    retorna
    -------
    u: float convertido

    ejemplos
    
    print(rads_rpm("rad/s",25.5))
    """
    pi = numpy.pi
    b = b.lower().strip()
    if b != "rad/s" and b != "rpm":
        print("error, ingrese tal cual 'rad/s' o 'rpm'")
    elif b == "rad/s":
        u=float(u/((2*pi)/60))
        return u
    elif b == "rpm":
        
        u=float(u*((2*pi)/60))
        return u

if __name__ == '__main__':
    assert metro_pie("ft",25.5) == 7.772399751283208
    print('Test -> metro_pie("ft",25.5) == 7.772399751283208\nOk')
    assert metro_pie("m",25.5) == 83.66141999999999
    print('Test -> metro_pie("m",25.5) == 83.66141999999999\nOk')
    assert hectarea_metro_cuadrado("ha",25.5) == 255000.0
    print('Test -> metro_pie("ha",25.5) == 255000.0\nOk')
    assert hectarea_metro_cuadrado("m2",25.5) == 0.00255
    print('Test -> metro_pie("m2",25.5) == 0.00255\nOk')
    assert bar_psi("bar",25.5) == 369.8469
    print('Test -> metro_pie("bar",25.5) == 369.8469\nOk')
    assert bar_psi("psi",25.5) == 1.758159930500972
    print('Test -> metro_pie("psi",25.5) == 1.758159930500972\nOk')
    assert celsius_fahrenheit("C",25.5) == 77.9
    print('Test -> metro_pie("C",25.5) == 77.9\nOk')
    assert celsius_fahrenheit("F",25.5) == -3.611111111111111
    print('Test -> metro_pie("F",25.5) == -3.611111111111111\nOk')
    assert newton_kilopondio("N",25.5) == 2.6002859999999997
    print('Test -> newton_kilopondio("N",25.5) == 2.6002859999999997\nOk')
    assert newton_kilopondio("kp",25.5) == 250.0686462950614
    print('Test -> newton_kilopondio("kp",25.5) == 250.0686462950614\nOk')
    assert rads_rpm("rad/s",25.5) == 243.5070629305999
    print('Test -> rads_rpm("rad/s",25.5) == 243.5070629305999\nOk')
    assert rads_rpm("rpm",25.5) == 2.670353755551324
    print('Test -> rads_rpm("rpm",25.5) == 2.670353755551324\nOk')