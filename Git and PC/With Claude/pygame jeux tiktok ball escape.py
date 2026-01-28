from pygame import *
from math import *

WIDTH = 1000
HEIGHT = 600
x, y = (int(WIDTH)/2), (int(HEIGHT)/2) 
vitesse_y = 5
vitesse_x = 10
rayon = 50
init()
screen = display.set_mode((int(WIDTH), int(HEIGHT)))
display.set_caption("Jeux tiktok")
clock = time.Clock()

running = True
while running:
    for ev in event.get():
        if ev.type == QUIT:  
            running = False
    

    y += vitesse_y
    x += vitesse_x
    
    if y > int(HEIGHT) - rayon:
        y = int(HEIGHT) - rayon
        vitesse_y = -vitesse_y
    if y < rayon:
        y = rayon
        vitesse_y = -vitesse_y
    if x > int(WIDTH) - rayon:
        x = int(WIDTH) - rayon
        vitesse_x = -vitesse_x
    if x < rayon:
        x = rayon
        vitesse_x = -vitesse_x
    """
    distance = sqrt((x - obstacle_x)**2 + (y - obstacle_y)**2)
    
    if distance < rayon + obstacle_rayon:
        angle = atan2(y - obstacle_y, x - obstacle_x)
        x = obstacle_x + (rayon + obstacle_rayon) * cos(angle)
        y = obstacle_y + (rayon + obstacle_rayon) * sin(angle)
        
        nx = cos(angle)
        ny = sin(angle)
        dot = vitesse_x * nx + vitesse_y * ny
        vitesse_x = vitesse_x - 2 * dot * nx
        vitesse_y = vitesse_y - 2 * dot * ny
    
    
    draw.circle(screen, (255, 0, 255), [int(obstacle_x), int(obstacle_y)], obstacle_rayon)"""
    screen.fill((0, 0, 0))
    draw.circle(screen, (255, 255, 255), [int(x), int(y)], rayon, 0)
    draw.circle(screen, (126, 0, 126), [int(x), int(y)], rayon - 3, 0)
    
    display.update()
    clock.tick(60)

quit()