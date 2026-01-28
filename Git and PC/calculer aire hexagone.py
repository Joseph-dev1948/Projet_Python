from turtle import *
from math import *
côté = 30

for i in range(6):
    fd(côté)
    lt(60)
    
aire = (3*sqrt(3)/2)*côté**2
print(f"l'aire est de : {aire}cm²")
done()