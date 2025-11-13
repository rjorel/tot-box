#!/usr/bin/env python3

from pygame.locals import *

import pygame

pygame.init()

fenetre = pygame.display.set_mode((570, 570))

# Création des surfaces utilisées

carre_blanc = pygame.Surface((30, 30))
carre_noir = pygame.Surface((30, 30))

carre_blanc.fill((255, 255, 255))
carre_noir.fill((0, 0, 0))


# Fonctions

def affichage():
    for i in range(0, n):
        for j in range(0, n):
            if M[i][j] == 0:
                fenetre.blit(carre_blanc, (j * 30, i * 30))
            else:
                fenetre.blit(carre_noir, (j * 30, i * 30))


def etat_suivant():
    temp = []
    for i in range(0, n - 1):
        temp.append([])
        for j in range(0, n - 1):
            if M[i][j - 1] == M[i][j + 1] and M[i - 1][j] == M[i + 1][j]:
                temp[i].append(M[i][j])
            else:
                temp[i].append(1 - M[i][j])

        if M[i][0] == M[i][n - 2] and M[i - 1][n - 1] == M[i + 1][n - 1]:  # Dernière colonne
            temp[i].append(M[i][n - 1])
        else:
            temp[i].append(1 - M[i][n - 1])

    temp.append([])  # Dernière ligne
    for j in range(0, n - 1):
        if M[n - 1][j - 1] == M[n - 1][j + 1] and M[n - 2][j] == M[0][j]:
            temp[n - 1].append(M[n - 1][j])
        else:
            temp[n - 1].append(1 - M[n - 1][j])

    if M[n - 1][0] == M[n - 1][n - 2] and M[n - 2][n - 1] == M[0][
        n - 1]:  # Dernière case de la dernière colonne
        temp[n - 1].append(M[n - 1][n - 1])
    else:
        temp[n - 1].append(1 - M[n - 1][n - 1])

    return temp


# Début

n = 20
M = []

for i in range(0, n):  # Création, initialisation du tableau
    M.append([])
    for j in range(0, n):
        M[i].append(0)

M[n // 2 - 1][n // 2 - 1] = 1
M[n // 4 - 1][n // 4 - 1] = 1
M[3 * n // 4 - 1][3 * n // 4 - 1] = 1
M[n // 4 - 1][3 * n // 4 - 1] = 1
M[3 * n // 4 - 1][n // 4 - 1] = 1

continuer = 1

while continuer:
    pygame.time.Clock().tick(5)

    for event in pygame.event.get():
        if event.type == KEYDOWN or event.type == QUIT:
            continuer = 0
    affichage()
    M = etat_suivant()
    pygame.display.flip()
