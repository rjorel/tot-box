#!/usr/bin/env python3

#################################################################
#                  PROGRAMMEUR : Raphael Jorel                  #
#                                                               #
# DESCRIPTION :                                                 #
#   Le classique snake, téxélisé, la vitesse du snake augmente  #
#   à chaque boule recoltée.                                    #        
#                                                               #
#################################################################


from random import randint

from pygame.locals import *

import pygame

pygame.init()

# Création de l'environnement du jeu

fenetre = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Snake')

police = pygame.font.match_font('Comic Sans MS')
texte = pygame.font.Font(police, 20)

# Création des surfaces utilisées

carre_fond = pygame.Surface((10, 10))
carre_snake = pygame.Surface((10, 10))
carre_boule = pygame.Surface((10, 10))

carre_fond.fill((0, 220, 30))
carre_snake.fill((112, 67, 0))
carre_boule.fill((0, 40, 200))

# Création de la map

niv = []
for i in range(0, 40):
    niv.append([])
    for j in range(0, 40):
        niv[i].append(0)

for j in range(19, 23):
    niv[20][j] = 1

# Début

continuer = 1
direction = 1
vitesse = 10
a = 20  # Position de la tête du snake
b = 22
pos = [[20, 19], [20, 20], [20, 21], [20, 22]]
c = randint(0, 39)  # Position du point rouge
d = randint(0, 39)
niv[c][d] = 2 - niv[c][d]
score = 0

while continuer:
    pygame.time.Clock().tick(vitesse)

    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0

        elif event.type == KEYDOWN:
            if (event.key == K_d or event.key == K_RIGHT) and direction != 3:
                direction = 1
            elif (event.key == K_s or event.key == K_DOWN) and direction != 4:
                direction = 2
            elif (event.key == K_q or event.key == K_LEFT) and direction != 1:
                direction = 3
            elif (event.key == K_z or event.key == K_UP) and direction != 2:
                direction = 4
            elif event.key == K_p:
                fenetre.blit(texte.render('Pause', True, (0, 0, 0)), (170, 180))
                pygame.display.flip()
                continuer = 2
                while continuer == 2:
                    event = pygame.event.wait()
                    if event.type == QUIT:
                        continuer = 0
                    elif event.type == KEYDOWN and event.key == K_p:
                        continuer = 1

    if direction == 1:
        b = (b + 1) % 40
    elif direction == 2:
        a = (a + 1) % 40
    elif direction == 3:
        b = (b - 1) % 40
    elif direction == 4:
        a = (a - 1) % 40

    if niv[a][b] == 1:
        fenetre.blit(texte.render('Perdu', True, (0, 0, 0)), (170, 180))
        pygame.display.flip()
        pygame.time.delay(2000)
        break

    if niv[c][d] != 2:
        vitesse += 1
        score += 100
        c = randint(0, 39)
        d = randint(0, 39)
        niv[c][d] = 2 - niv[c][d]
    else:
        niv[pos[0][0]][pos[0][1]] = 0
        del (pos[0])

    pos.append([a, b])
    niv[a][b] = 1

    for i in range(0, 40):
        for j in range(0, 40):
            if niv[i][j] == 0:
                fenetre.blit(carre_fond, (j * 10, i * 10))
            if niv[i][j] == 1:
                fenetre.blit(carre_snake, (j * 10, i * 10))
            if niv[i][j] == 2:
                fenetre.blit(carre_boule, (j * 10, i * 10))

    fenetre.blit(texte.render('{}'.format(score), True, (0, 0, 0)), (10, 370))

    pygame.display.flip()
