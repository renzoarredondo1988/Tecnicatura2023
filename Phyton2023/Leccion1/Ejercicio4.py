#Etapas de la vida

etapas=int(input("Indique una edad "))

if 0<=etapas<10:
    print("La infancia es increible y bella")
elif 10<=etapas<20:
    print("Tienes muchos cambios, mucho que estudiar")
elif 20<=etapas<30:
    print("Amor y comienza el trabajo")
elif 30<=etapas<40:
    print("Formar familia, viajes, proyectos")
elif 40<=etapas<50:
    print("Plena madures")
elif 50<=etapas<60:
    print("Ultima etapa laboral")
elif 60<=etapas<70:
    print("La jubilacion...")
elif etapas >= 70:
    print("Cuidate el bobo...")
else:
    print("No ha elegido una edad correcta")