import os
mydict = {
    "Joseph",
    "Louis",
    "Édouard",
    }

mydict1 = {
    "Capacité",
    "Humanité",
    "Tempérament",
    "Intelligence",
    }

mydict2 = {
    "Physique",
    "Moral",
    "Social",
    "Culturel",
    "Connaissance",
    }

for x in mydict:
    for y in mydict1:
        for z in mydict2:
            chemin = f"./Base de données/{x}/{y}/{z}/"
            os.makedirs(chemin, exist_ok=True)
            
            for i in range(11):
                nom_fichier = os.path.join(chemin, f"fichier_{i}.txt")
                with open(nom_fichier, "w", encoding="utf-8") as fichier:
                    fichier.write(f"Fichier numéro {i}\n")
                    fichier.write("""
Ça a l'air très pratique.
selon Claude sonnet 4.5.
ça permettrait d'écrire.
plusieurs lignes à la fois sans le /n
""")
