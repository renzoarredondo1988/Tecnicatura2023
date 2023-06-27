#Predecir una estacion del año

eligeEstacion=int(input("Indique una estacion del año, por favor, del 1 al 12"))

if eligeEstacion>0 and eligeEstacion<=3:
    print("La estacion escogida es Verano")
elif eligeEstacion>3 and eligeEstacion<=6:
    print("La estacion escogida es Otoño")
elif eligeEstacion>6 and eligeEstacion<=9:
    print("La estacion escogida es Invierno")
elif eligeEstacion>9 and eligeEstacion<=12:
    print("La estacion escogida es Primavera")
else:
    print("Se equivoco de opcion")