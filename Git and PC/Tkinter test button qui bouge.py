from tkinter import *
from math import *
from time import *
root = Tk()
root.title("Bouton qui se barre")
WIDTH = 1200
HEIGHT = 900
root.geometry(f"{WIDTH}x{HEIGHT}")
def Merci():
    label.config(text="Merci beaucoup le virement est fait")
    btn_reste.place_forget()
    btn_cours.place_forget()
    btn_quitter.pack()
def Quitter():
    root.destroy()
def suivre_souris(event):
    Courir(event)
root.bind("<Motion>", suivre_souris)
def Courir(event):
    x1 = btn_cours.winfo_x()
    y1 = btn_cours.winfo_y()
    width = btn_cours.winfo_width()
    height = btn_cours.winfo_height()
    distance_x = abs(event.x - x1)
    distance_y = abs(event.y - y1)
    if distance_x < 100 and distance_y < 100:
        distance_haut = y1
        distance_bas = HEIGHT - (y1 + height)
        distance_gauche = x1
        distance_droite = WIDTH - (x1 + width)
        vient_de_gauche = event.x < x1
        vient_de_droite = event.x > x1 + width
        vient_du_haut = event.y < y1
        vient_du_bas = event.y > y1 + height
        nouveau_x = x1
        nouveau_y = y1
        if vient_de_gauche:
            if distance_droite > 100:
                nouveau_x = x1 + 50
            elif distance_gauche > 50:
                nouveau_x = x1 - 100
        elif vient_de_droite:
            if distance_gauche > 50:
                nouveau_x = x1 - 100
            elif distance_droite > 50:
                nouveau_x = x1 + 100
        if vient_du_haut:
            if distance_bas > 50:
                nouveau_y = y1 + 100
            elif distance_haut > 50:
                nouveau_y = y1 - 100
        elif vient_du_bas:
            if distance_haut > 50:
                nouveau_y = y1 - 100
            elif distance_bas > 50:
                nouveau_y = y1 + 100
        nouveau_x = max(0, min(nouveau_x, WIDTH - width))
        nouveau_y = max(0, min(nouveau_y, HEIGHT - height))
        btn_cours.place(x=nouveau_x, y=nouveau_y)
def BRUH():
    label.config(text="Bravo t'a réussi a esquiver")
    btn_reste.place_forget()
    btn_cours.place_forget()
    btn_quitter.pack()
label = Label(root, text="Veux tu me donner 10 000€", font=("Arial",30))
label.pack()
btn_reste = Button(root, text="Oui", width=10, height=5, bg="green", font=("Liberation Serif", 10), command=Merci)
btn_reste.place(x=320, y=109)
btn_cours = Button(root, text="Non", width=10, height=5, bg="red", font=("Liberation Serif", 10), command=BRUH)
btn_cours.place(x=410, y=109)
btn_quitter = Button(root, text="Merci tu peux quitter", width=20, height=10, bg="Orange", font=("Liberation Serif",20), command=Quitter)
btn_quitter.pack_forget()
root.mainloop()