from pygame import *
from math import *

WIDTH = 1000
HEIGHT = 600
x, y = (int(WIDTH)/2), (int(HEIGHT)/2) 
gravite = 0.5
vitesse_y = 0
vitesse_x = 5
rayon = 50

init()
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Jeux tiktok")
clock = time.Clock()

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:  
            running = False
    
    vitesse_y += gravite
    y += vitesse_y
    
    if y > HEIGHT - rayon:
        y = HEIGHT - rayon
        vitesse_y = -vitesse_y
    if y < rayon:
        y = rayon
        vitesse_y = -vitesse_y
        
        
    x += vitesse_x
    
    if x > WIDTH - rayon:
        x = WIDTH - rayon
        vitesse_x = -vitesse_x
    
    if x < rayon:
        x = rayon
        vitesse_x = -vitesse_x
        
    screen.fill((0, 0, 0))
    
    draw.circle(screen, (255, 255, 255), [int(x), int(y)], rayon, 0)
    draw.circle(screen, (100, 0, 100), [int(x), int(y)], rayon-3, 0)
    
    display.update()
    clock.tick(60)

quit()