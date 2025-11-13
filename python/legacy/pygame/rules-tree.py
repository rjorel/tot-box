#!/usr/bin/env python3

from math import cos, radians, sin
from random import choice, randint

from pygame.locals import *

import pygame

"""
	Fonctions régissant l'ensemble du programme :
		- génération de règles,
		- dérivation,
		- trace d'une régle,
		- création d'une tortue à partir des fonctions précédentes,
		- fonction principale.
"""


# Génération d'une règle composée de A, B, C, D, E, (, {, ), }.

def generateRule(n):
    rule = []
    par = 0
    croc = 0

    for i in range(0, n):
        carac = choice(['A', 'B', 'C', 'D', 'E', '(', '{'])

        if (carac == '('):
            if (randint(0, 5) and par):
                rule.append(')')
                par -= 1

            else:
                rule.append('(')
                par += 1

        elif (carac == '{'):
            if (randint(0, 5) and croc):
                rule.append('}')
                croc -= 1

            else:
                rule.append('{')
                croc += 1

        else:
            rule.append(carac)

    while (par or croc):

        if (par and croc):
            if (randint(0, 1)):
                rule.append(')')
                par -= 1

            else:
                rule.append('}')
                croc -= 1

        elif (par):
            rule.append(')')
            par -= 1

        elif (croc):
            rule.append('}')
            croc -= 1

    return rule


# Dérivation à partir de régles générées. La première règle est prise comme base de dérivation.

def derivation(dicRules):
    deriv = []

    for i in range(0, len(dicRules['A'])):

        if (dicRules['A'][i] in ['A', '(', ')', '{', '}']):
            deriv.append(dicRules['A'][i])

        else:
            for j in range(0, len(dicRules[dicRules['A'][i]])):
                deriv.append(dicRules[dicRules['A'][i]][j])

    return deriv


# Trace d'une règle à l'écran.

def trace(screen, rule):
    stackPar = []
    stackCroc = []
    radius = 90
    x1 = randint(0, 640)
    y1 = randint(0, 480)
    x2 = x1
    y2 = y1

    for i in range(0, len(rule)):

        if (rule[i] in ['A', 'B', 'C', 'D', 'E']):
            x2 += 5 * cos(radians(radius))
            y2 += 5 * sin(radians(radius))

            pygame.draw.line(screen, (0, 0, 0), (x1, y1), (x2, y2))

            x1 = x2
            y1 = y2

        elif (rule[i] == '('):
            radius += 30
            stackPar.append([x1, y1, radius])

        elif (rule[i] == '{'):
            radius -= 30
            stackCroc.append([x1, y1, radius])

        elif (rule[i] == ')'):
            x1 = stackPar[len(stackPar) - 1][0]
            y1 = stackPar[len(stackPar) - 1][1]
            radius = stackPar[len(stackPar) - 1][2]
            del (stackPar[len(stackPar) - 1])

            x2 = x1
            y2 = y1

        elif (rule[i] == '}'):
            x1 = stackCroc[len(stackCroc) - 1][0]
            y1 = stackCroc[len(stackCroc) - 1][1]
            radius = stackCroc[len(stackCroc) - 1][2]
            del (stackCroc[len(stackCroc) - 1])

            x2 = x1
            y2 = y1


# Création d'une tortue, à partir des fonctions précédentes.

def createTurtle(screen, n):
    A = generateRule(n)
    B = generateRule(n)
    C = generateRule(n)
    D = generateRule(n)
    E = generateRule(n)

    dicRules = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}
    deriv = derivation(dicRules)

    screen.fill((255, 255, 255))
    trace(screen, deriv)
    pygame.display.flip()


# Fonction principale, gérant les événements.

def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Turtle')

    loop = 1

    createTurtle(screen, 50)

    while (loop):
        event = pygame.event.wait()

        if (event.type == QUIT):
            loop = 0

        elif (event.type == KEYDOWN):
            if (event.key == K_r):
                createTurtle(screen, 50)

            elif (event.key == K_ESCAPE):
                loop = 0


# Lancement du programme

if (__name__ == "__main__"):
    main()
