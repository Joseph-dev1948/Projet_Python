from turtle import*
from time import*
from keyboard import*
from PIL import ImageGrab

mode_lent = False
stylo = False
colormode(255)
pencolor(0,0,0)
red = 0
green = 0
blue = 0
fillcolor(0,0,0)
red1 = 0
green1 = 0
blue1 = 0
taille = 5
width(taille)

def basculer_mode_lent():
    global mode_lent
    mode_lent = not mode_lent
    print("Mode lent activé" if mode_lent else "Mode normal")
    
def basculer_le_stylo():
    global stylo
    stylo = not stylo
    print("Le stylo est lever" if stylo else "Le stylo est prêt a écrire")

def augmenter_taille():
    global taille
    taille += 1
    width(taille)
    print(f"Taille du stylo : {taille}")
    
def diminuer_taille():
    global taille
    if taille == 0:
        print("Mon gars tu cherche a faire une taille de stylo négative aller choisi autre chose")
    else :
        taille -= 1
    width(taille)
    print(f"Taille du stylo : {taille}")
def reset():
    global red
    global green
    global blue
    global red1
    global green1
    global blue1
    global pencolor
    global fillcolor
    global width
    home()
    red = 0
    green = 0
    blue = 0
    red1 = 0
    green1 = 0
    blue1 = 0
    pencolor(0,0,0)
    fillcolor(0,0,0)
    clear()
    width(5)

def avancer():
    penup() if stylo else pendown()
    fd(25 if mode_lent else 50)
def reculer():
    penup() if stylo else pendown()
    pencolor("white")
    back(25 if mode_lent else 50)
    pencolor((red, green, blue))
def gauche():
    penup() if stylo else pendown()
    lt(45)
def droite():
    penup() if stylo else pendown()
    rt(45)
def retourner():
    lt(180)
def gauche90():
    lt(90)
def droite90():
    rt(90)

def dessiner(x, y):
    if not stylo:
        goto(x, y)

def commencer_dessin(x, y):
    global stylo
    stylo = False
    dessiner(x, y)

def arreter_dessin(x, y):
    global stylo
    stylo = True

def polygone():
    côté = int(input("Tu veux combien de côté ? : "))
    print(f"Tu a choisi {côté} côté")
    speed(0)
    angle = 360/côté
    print(f"Ce qui fait un angle de {angle}°")
    width(taille)
    down()
    for i in range(côté):
        rt(angle)
        fd(50)
    
def color1():
    global pencolor
    global red
    global green
    global blue
    try :
        red = int(input("Quelle valeur RGB voulez vous pour le rouge (0-255) seulement ? : "))
        green = int(input("Quelle valeur RGB voulez vous pour le vert (0-255) seulement ? : "))
        blue = int(input("Quelle valeur RGB voulez vous pour le bleu (0-255) seulement ? : "))
        colormode(255)
        red = max(0, min(255, red))
        green = max(0, min(255, green))
        blue = max(0, min(255, blue))
        pencolor(red, green, blue)
    except ValueError:
        print("Erreur : entrez un nombre entre 0 et 255 !")
        
def fcolor():
    global fillcolor
    global red1
    global green1
    global blue1
    try :
        red1 = int(input("Quelle valeur RGB voulez vous pour le rouge (0-255) seulement ? : "))
        green1 = int(input("Quelle valeur RGB voulez vous pour le vert (0-255) seulement ? : "))
        blue1 = int(input("Quelle valeur RGB voulez vous pour le bleu (0-255) seulement ? : "))
        colormode(255)
        red1 = max(0, min(255, red1))
        green1 = max(0, min(255, green1))
        blue1 = max(0, min(255, blue1))
        fillcolor(red1, green1, blue1)
    except ValueError:
        print("Erreur : entrez un nombre entre 0 et 255 !")


def sauvegarder():
    # Capture l'écran de la tortue
    x0 = window_width() // -2
    y0 = window_height() // -2
    x1 = window_width() // 2
    y1 = window_height() // 2
    ImageGrab.grab(bbox=(x0, y0, x1, y1)).save("dessin.png")
    print("Dessin sauvegardé sous 'dessin.png' !")
        
def rouge():
    pencolor(255, 0, 0)
    fillcolor(255, 0, 0)
def bleu():
    pencolor(0, 0, 255)
    fillcolor(0, 0, 255)
def vert():
    pencolor(0, 255, 0)
    fillcolor(0, 255, 0)
def blanc():
    pencolor(255,255,255)
    fillcolor(255, 255, 255)
def noir():
    pencolor(0,0,0)
    fillcolor(0,0,0)

onkey(avancer, "Up")
onkey(reculer, "Down")
onkey(gauche, "Left")
onkey(droite, "Right")
onkey(basculer_mode_lent, "e")
onkey(basculer_le_stylo,"s")
onkey(diminuer_taille, "q")
onkey(augmenter_taille, "a")
onkey(color1, "c")
onkey(rouge, "r")
onkey(bleu, "b")
onkey(vert, "v")
onkey(noir, "n")
onkey(blanc, "w")
onkey(fcolor, "f")
onkey(retourner, "p")
onkey(gauche90, "l")
onkey(droite90, "m")
onkey(polygone, "o")
onkey(reset,"x")
onkey(sauvegarder, "z")
onscreenclick(commencer_dessin, 1)
onscreenclick(arreter_dessin, 3)
ondrag(dessiner)
listen()
done()