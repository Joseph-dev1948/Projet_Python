import os
mydict = {
    "Agents Actifs",
    "Agents Dormant",
    "Agents Démissionner",
    "Agents Mort"
    }

mydict1 = {
    "Agents de terrain",
    "Tireur d'élite",
    "Démolition",
    "Neutralisation",
    "Infiltration",
    "Reconnaissance",
    "Cyber-attaque",
    }

mydict2 = {
    "Catégorie 0",
    "Catégorie 1",
    "Catégorie 2",
    "Catégorie 3",
    "Catégorie 4",
    "Catégorie 5",
    "Catégorie 6",
    "Catégorie 7",
    "Catégorie 8"
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