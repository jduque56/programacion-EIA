
#codigo para volver x segundos en horas, segundo y minutos

sec = float(input("Ingrese la cantidad de segundos que quiere convertir: "))
horas = sec//3600
minutos = (sec%3600)//60
segundos = sec%60
print(horas)
print(minutos)
print(segundos)

#if else

a = int(input("ingrese 1 o 0: "))
if a==True:
    print("Efectivamente es verdadero")
elif a==False: 
    print("Efectivamente es falso")
else:
    print("Error, ingrese solo 1 o 0")

#match case
error = input('Introduzca un código de error:\n')

match error:
    case "200":
        print('Todo ok.')
    case "301":
        print('Movimiento permanente de la página.')
    case "302":
        print('Movimiento temporal de la página.')
    case "404":
        print('Página no encontrada.')
    case "500":
        print('Error interno del servidor.')
    case "503":
        print('Servicio no disponible.')
    case _:#tambien se puede poner default o defecto
        print('Error no disponible.')


 

