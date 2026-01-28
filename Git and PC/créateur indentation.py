alphabet = ["b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
voiture = 4
bip = 8
print(f'for a in range({int(bip)}):')
for x in alphabet[:26]:
    print(" "*int(voiture),f'for {x} in range({int(bip)}):')
    voiture +=4
print(" "*int(voiture),f'print("caca")')