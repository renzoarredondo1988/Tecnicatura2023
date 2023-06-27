#Sistema calificaciones

calificacion=float(input("Indique la calificacion obtenida "))#Ingresamos un float por si tiene coma

if 9<=calificacion<=10:
    print("A")
elif 8<=calificacion<9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif calificacion < 6:
    print("F")
else:
    print("Ingrese una calificacion valida")