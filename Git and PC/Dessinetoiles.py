from math import*

def menu():
    while True :
        choix = input("""tu veux quoi ? :
Pyramide normale --------------> (1)
Pyramide inversée -------------> (2)
Pyramide normale trou ---------> (3)
Pyramide inversée trou --------> (4)
Ou un carré -------------------> (5)
Ou un carré avec un trou ------> (6)
Ou un rectangle ---------------> (7)
Ou un rectangle avec un trou --> (8)
Ou un cercle ------------------> (9)
Ou un cercle avec un trou -----> (10)
Ou 'stop' pour fermer le programme? : """)
        if choix == "1":
            pyramide()
            break
        elif choix == "2":
            pyramide_inverser()
            break
        elif choix == "3":
            pyramide_trou()
            break
        elif choix == "4":
            pyramide_inverser_trou()
            break
        elif choix == "5":
            carré()
            break
        elif choix == "6":
            carré_trou()
            break
        elif choix == "7":
            rectangle()
            break
        elif choix == "8":
            rectangle_trou()
            break
        elif choix == "9":
            cercle()
            break
        elif choix == "10":
            cercle_trou()
            break
        elif choix == "stop":
            break
        else:
            print("Choix invalide !")
            
def pyramide():
    nbLignes = int(input(f"tu veux combien de lignes ? : "))
    nbetoiles = 1
    espaces = nbLignes
    for i in range(int(nbLignes)):
        print(" " * espaces, "*" * nbetoiles)
        espaces -= 1
        nbetoiles += 2
    menu()
    
def pyramide_trou():
    nbLignes = int(input(f"tu veux combien de lignes ? : "))
    nbetoiles = 1
    nbespaces = 1
    espaces = nbLignes+1
    debut = int(espaces)+1
    print(" " * debut, "*" * nbetoiles)
    for i in range(int(nbLignes)-2):
        print(" "*espaces,"*"+" "*nbespaces+"*")
        espaces -= 1
        nbespaces +=2
        nbetoiles += 2
    fin = int(nbetoiles)+2
    print(" " * espaces,"*" * fin)
    menu()
        
def pyramide_inverser():
    nbLignes = int(input(f"tu veux combien de lignes ? : "))
    nbetoiles = nbLignes * 2 - 1
    espaces = 0
    for i in range(int(nbLignes)):
        print(" " * espaces, "*" * nbetoiles)
        espaces += 1
        nbetoiles -= 2
    menu()
    
def pyramide_inverser_trou():
    nbLignes = int(input(f"tu veux combien de lignes ? : "))
    nbetoiles = nbLignes * 2 - 1
    espaces = 1
    nbespaces = nbetoiles - 4
    print("*"*nbetoiles)
    for i in range(int(nbLignes)-2):
        print(" "*espaces+"*"+" "*nbespaces+"*")
        espaces += 1
        nbetoiles -= 2
        nbespaces -= 2
    print(" "*espaces+"*")
    menu()
        
def carré():
    nbLignes = int(input(f"tu veux quelle longueur ? : "))
    nbetoiles = nbLignes
    for i in range(int(nbLignes)):
        print("*" * nbetoiles)
    menu()
        
def carré_trou():
    nbLignes = int(input(f"tu veux quelle longueur ? : "))
    print("*"*nbLignes)
    for i in range(int(nbLignes-2)):
        print("*"+" "* (int(nbLignes)-2)+"*")
    print("*"*nbLignes)
    menu()
    
def rectangle():
    Longueur = int(input(f"tu veux quelle longueur ? : "))
    Largeur = int(input(f"tu veux quelle largeur ? : "))
    for i in range(Longueur):
        print(f"*" * Largeur)
    menu()

def rectangle_trou():
    Longueur = int(input(f"tu veux quelle longueur ? : "))
    Largeur = int(input(f"tu veux quelle largeur ? : "))
    print("*"*Largeur)
    for i in range(int(Longueur) - 2):
        print("*"+" "* (int(Largeur)-2)+"*")
    print("*"*Largeur)
    menu()

def cercle():
    rayon = int(input("tu veux quel rayon ? : "))
    for y in range(-rayon, rayon + 1):
        ligne = ""
        for x in range(-rayon, rayon + 1):
            distance = (x**2 + y**2)**0.5
            if distance <= rayon:
                ligne += "*"
            else:
                ligne += " "
        print(ligne)
    menu()

def cercle_trou():
    rayon = int(input("tu veux quel rayon ? : "))
    epaisseur = float(input("tu veux quelle épaisseur ? : "))
    
    for y in range(-rayon, rayon + 1):
        ligne = ""
        for x in range(-rayon, rayon + 1):
            distance = (x**2 + y**2)**0.5
            if rayon - epaisseur <= distance <= rayon + epaisseur:
                ligne += "*"
            else:
                ligne += " "
        print(ligne)
    menu()
    
menu()
