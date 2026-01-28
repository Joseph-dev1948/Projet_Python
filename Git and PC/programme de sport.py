from random import*

exercice = ["pompes","tractions","squats","gainage","dips","relever de jambes sur barre","handstand hold"]

for exercice in exercice:
    nombre = randint(1,20)
    print(f"{exercice} : {nombre}")