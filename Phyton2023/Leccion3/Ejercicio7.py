i=0
horasTrabajadas=[]
tarifaPorHora=[]
salario=[]
salarioTotal=0

for i in range(0,5,1):
    hora=int(input("Indique la cantidad de horas trabajadas por el empleado "))
    horasTrabajadas.append(hora)
    tarifa=int(input("Indique la tarifa por hora del trabajador "))
    tarifaPorHora.append(tarifa)
    salario.append(tarifaPorHora[i]*horasTrabajadas[i])
    print("El salario del trabajador es ",salario[i])
    salarioTotal=salarioTotal+salario[i]

print(salario)

print("La suma de todos los salarios es ",salarioTotal)
