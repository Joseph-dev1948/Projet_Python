for i in range(11):
    nom_fichier = f"fichier_{i}.txt"
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(f"Fichier numéro {i}\n")
        fichier.write("""
Ça a l'air très pratique.
selon Claude sonnet 4,5.
ça permetrait d'écrire.
plusieurs ligne a la fois sans le /n
""")