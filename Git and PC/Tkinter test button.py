from tkinter import *
from math import *
from time import *
root = Tk()
root.title("Bouton qui grossit")
root.geometry("800x600")
tailleoui = 20
taillenon = 20
tailleoui1 = 5
taillenon1 = 5
tailleoui2 = 10
taillenon2 = 10
def augmentertaille():
    global tailleoui
    global taillenon
    global tailleoui1
    global taillenon1
    global tailleoui2
    global taillenon2
    tailleoui = int(tailleoui*1.5)
    taillenon = int(taillenon/1.5)
    tailleoui1 = int(tailleoui1*1.5)
    taillenon1 = int(taillenon1/1.5)
    tailleoui2 = int(tailleoui2*1.5)
    taillenon2 = int(taillenon2/1.5)
    
    btn_reste.config(width=tailleoui, height=tailleoui1, font=("Liberation Serif", tailleoui2))
    btn_cours.config(width=taillenon, height=taillenon1, font=("Liberation Serif", taillenon2))

def Merci():
    label.config(text="Merci beaucoup le virement est fait")
    btn_reste.config(width=20, height=20, font=("Liberation Serif", 10))
    btn_cours.config(width=20, height=20, font=("Liberation Serif", 10))
    btn_reste.pack_forget()
    btn_cours.pack_forget()
    btn_quitter.pack()

def Quitter():
    root.destroy()
label = Label(root, text="Veux tu me donner 10 000€", font=("Arial",30))
label.pack()
btn_reste = Button(root, text="Oui", width=tailleoui, height=tailleoui1, bg="green", font=("Liberation Serif", tailleoui2), command=Merci)
btn_reste.pack()
btn_cours = Button(root, text="Non", width=taillenon, height=taillenon1, bg="red", font=("Liberation Serif", taillenon2), command=augmentertaille)
btn_cours.pack()
btn_quitter = Button(root, text="Merci pour ton geste", width=20, height=10, bg="Orange", font=("Liberation Serif",20), command=Quitter)
btn_quitter.pack_forget()

root.mainloop()