def pyramide():
    print("      *")
    print("     ***")
    print("    *****")
    print("   *******")
    print("  *********")
    print(" ***********")
    print("*************")

def pyramide_inversée():
    print("*************")
    print(" ***********")
    print("  *********")
    print("   *******")
    print("    *****")
    print("     ***")
    print("      *")

choix = input("Tu veux une pyramide normale (1) ou inversée (2) ? ")
if choix == "1":
    pyramide()
elif choix == "2":
    pyramide_inversée()
else:
    print("Choix invalide.")