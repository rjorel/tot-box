#!/usr/bin/env python3

from pygame.locals import *

import pygame

pygame.init()

# Environnement de jeu

fenetre = pygame.display.set_mode((300, 300))

police = pygame.font.match_font('Arial')
texte = pygame.font.Font(police, 20)

# Création des surfaces utilisées

ligne_hztl = pygame.Surface((300, 5))
ligne_vtl = pygame.transform.rotate(ligne_hztl, 90)

ligne_hztl.fill((255, 255, 255))
ligne_vtl.fill((255, 255, 255))

# Création de la grille de jeu

grille = []
for i in range(0, 3):
    grille.append([])
    for j in range(0, 3):
        grille[i].append(0)


# Fonctions

def affichage():
    for i in [98, 199]:
        fenetre.blit(ligne_hztl, (0, i))
        fenetre.blit(ligne_vtl, (i, 0))

    pygame.display.flip()


def croix_gagnent():
    fenetre.blit(texte.render('Les croix gagnent', True, (0, 200, 0)), (75, 130))
    pygame.display.flip()
    pygame.time.delay(2000)

    return 0


def ronds_gagnent():
    fenetre.blit(texte.render('Les ronds gagnent', True, (200, 0, 0)), (75, 130))
    pygame.display.flip()
    pygame.time.delay(2000)

    return 0


# Début

affichage()

joueur = 1
continuer = 1

while continuer:
    event = pygame.event.wait()
    if event.type == QUIT:
        continuer = 0

    elif event.type == MOUSEBUTTONDOWN:
        i = event.pos[-1] // 100
        j = event.pos[0] // 100

        if grille[i][j] == 0:
            grille[i][j] = joueur

            if joueur == 1:
                pygame.draw.line(fenetre, (255, 255, 255), (j * 100 + 10, i * 100 + 10),
                                 (j * 100 + 90, i * 100 + 90), 5)
                pygame.draw.line(fenetre, (255, 255, 255), (j * 100 + 10, i * 100 + 90),
                                 (j * 100 + 90, i * 100 + 10), 5)
            else:
                pygame.draw.circle(fenetre, (255, 255, 255), (j * 100 + 50, i * 100 + 50), 40, 5)

            joueur = -joueur

        affichage()

        # On teste les lignes et les colonnes, pour savoir si un joueur a gagné ou non

        for i in range(0, 3):
            if (grille[i][0] + grille[i][1] + grille[i][2] == 3) or (
                grille[0][i] + grille[1][i] + grille[2][i] == 3):
                continuer = croix_gagnent()

            elif (grille[i][0] + grille[i][1] + grille[i][2] == -3) or (
                grille[0][i] + grille[1][i] + grille[2][i] == -3):
                continuer = ronds_gagnent()

        if (grille[0][0] + grille[1][1] + grille[2][2] == 3) or (
            grille[0][2] + grille[1][1] + grille[2][0] == 3):
            continuer = croix_gagnent()

        elif (grille[0][0] + grille[1][1] + grille[2][2] == -3) or (
            grille[0][2] + grille[1][1] + grille[2][0] == -3):
            continuer = ronds_gagnent()

        # On cherche à savoir si la grille est remplie, sans qu'aucun joueur ne gagne

        if continuer:
            grille_pleine = True

            for liste in grille:
                if 0 in liste:
                    grille_pleine = False

            if grille_pleine == True:
                fenetre.blit(texte.render('Match nul', True, (200, 200, 0)), (110, 130))
                pygame.display.flip()
                pygame.time.delay(2000)
                continuer = 0
