import numpy

def manhattan(ax,ay,bx,by):
    """
    funcion para calcular la distancia entre dos puntos mediante el metodo Manhattan
    manhattan(ax,ay,bx,by)

    parametros
    ----------
    ax: distancia en el eje x del primer punto
    ay: distancia en el eje y del primer punto
    bx: distancia en el eje x del segundo punto
    by: distancia en el eje y del segundo punto

    retorna
    -------
    distancia: distancia entre los dos puntos

    ejemplos
    
    x=manhattan(5,7,8,9)
    print(x)
    """
    cx = numpy.abs(ax-bx)
    cy = numpy.abs(ay-by)
    distancia = cx+cy
    return distancia 

def euclidiana(ax,ay,bx,by):
    """
    funcion para calcular la distancia entre dos puntos mediante el metodo Euclidiano 
    euclidiana(ax,ay,bx,by)

    parametros
    ----------
    ax: distancia en el eje x del primer punto
    ay: distancia en el eje y del primer punto
    bx: distancia en el eje x del segundo punto
    by: distancia en el eje y del segundo punto

    retorna
    -------
    distancia: distancia entre los dos puntos

    ejemplos
    
    x=euclidiana(5,7,8,9)
    print(x)
    """
    cx = ax-bx
    cy = ay-by
    distancia = float(numpy.sqrt(cx**2 + cy**2))
    return distancia

def chebyshev(ax,ay,bx,by):
    """
    funcion para calcular la distancia entre dos puntos mediante el metodo Chebyshev
    parametros
    ----------
    ax: distancia en el eje x del primer punto
    ay: distancia en el eje y del primer punto
    bx: distancia en el eje x del segundo punto
    by: distancia en el eje y del segundo punto

    retorna
    -------
    distancia: distancia entre los dos puntos

    ejemplos
    
    x=chebyshev(5,7,8,9)
    print(x)
    """
    cx = numpy.abs(ax-bx)
    cy = numpy.abs(ay-by)
    if cx >= cy:
        distancia = cx
        return distancia
    elif cx < cy:
        distancia = cy
        return distancia
    
if __name__=='__main__':
    assert manhattan(5,7,8,9) == 5
    print('test -> manhattan(uni) == 5\nOk')
    assert euclidiana(5,7,8,9) == 3.605551275463989
    print('test -> euclidiana(uni) == 3.605551275463989\nOk')
    assert chebyshev(5,7,8,9) == 3
    print('test -> chebyshev(uni) == 3\nOk')


