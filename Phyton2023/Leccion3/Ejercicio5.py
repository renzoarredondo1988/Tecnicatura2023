
numero=int(input("Digite un numero al cual se le calculara el factorial "))

i=numero
factorial=1

if numero>0:
    while i>1:
        i=i-1
        factorialAnterior=1*i
        factorial=factorialAnterior*factorial

resultado=factorial*numero

print(resultado)

