#Ingresar N enteros, de alli ver ctos son pares y sacar la suma. A los impares sacar el promedio

N=int(input("Ingrese la cantidad de numeros a ingresar por el usuario "))#Defino la cantidad de valores a ingresar x el usuario
i=0
valores=[]#Dichos valores los guardare en una lista
suma=0#defino condiciones iniciales a las variables que utilizare luego
cantidadPar=0
cantidadImpar=0
sumaImpar=0

if N>0:#El valor ingresado por el usuario debe ser positivo entero
    for i in range(N):#con range le doy el rango a mi ciclo for
        valor=int(input("Ingrese un valor "))
        valores.append(valor)#con el append agrego un valor a la lista, que tendra justamente la variable de arriba

else:
    print("La cantidad a ingresar debe ser mayor que 0")

print(valores)#imprimo la lista formada

for i in range(0,N,1):#Recorro la lista desde 0 a N-1 con paso 1 (eso significa los valores dentro del range)
    if valores[i]%2==0:#Si el resto es 0 es porque es par
        sumaPares = suma+valores[i]
        suma=sumaPares
        cantidadPar=cantidadPar+1

    else:
        cantidadImpar=cantidadImpar+1
        sumaImpar=sumaImpar+valores[i]

print("Hay un total de ",cantidadPar," valores pares y su suma da un total de ",sumaPares)

if cantidadImpar>0:#Uso esta condicion xq si ningun valor es impar me queda un numero dividido cero y da error
    promedioImpar=sumaImpar/cantidadImpar
    print("El promedio de los valores impares es ",promedioImpar)
else:
    print("Usted no ingreso ningun valor impar")

