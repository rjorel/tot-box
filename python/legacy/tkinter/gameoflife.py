#!/usr/bin/env python3

from random import randint
from tkinter import *


class Game:
    """
        Gestion du jeu de la vie.
    """

    def __init__(self, cols, rows, generate=False):
        self.__tab = []
        self.__cols = cols
        self.__rows = rows

        for i in range(self.__rows):
            self.__tab.append([])
            for j in range(self.__cols):
                if (generate):
                    self.__tab[i].append(randint(0, 1))
                else:
                    self.__tab[i].append(0)

    def nextState(self):
        tmp = []

        for i in range(self.__rows):
            tmp.append([])

            for j in range(self.__cols):
                nbNeighbours = self.countNeighbours(i, j)

                if (nbNeighbours == 2):
                    tmp[i].append(self.__tab[i][j])
                elif (nbNeighbours == 3):
                    tmp[i].append(1)
                else:
                    tmp[i].append(0)

        self.__tab = tmp

    def countNeighbours(self, i, j):
        nb = 0
        top = (i == 0)
        bottom = (i == self.__rows - 1)
        left = (j == 0)
        right = (j == self.__cols - 1)

        if (not top): nb += self.__tab[i - 1][j]
        if (not bottom): nb += self.__tab[i + 1][j]
        if (not left): nb += self.__tab[i][j - 1]
        if (not right): nb += self.__tab[i][j + 1]
        if (not top and not left): nb += self.__tab[i - 1][j - 1]
        if (not top and not right): nb += self.__tab[i - 1][j + 1]
        if (not bottom and not left): nb += self.__tab[i + 1][j - 1]
        if (not bottom and not right): nb += self.__tab[i + 1][j + 1]

        return nb

    def getVal(self, i, j):
        return self.__tab[i][j]

    def getValues(self):
        return list(self.__tab)

    def getCols(self):
        return self.__cols

    def getRows(self):
        return self.__rows


class Window(Tk):
    """
        Fenêtre d'affichage
    """

    def __init__(self, cols, rows, size):
        Tk.__init__(self)

        self.__game = Game(cols, rows, True)
        self.__cols = cols
        self.__rows = rows
        self.__size = size
        self.__canvas = Canvas(self, width=cols * size, height=rows * size)
        self.__canvas.pack()

        self.geometry(str(cols * size) + "x" + str(rows * size))
        self.resizable(False, False)
        self.title("Game of life")

        self.evolve()
        self.mainloop()

    def display(self):
        colors = ["white", "black"]

        self.__canvas.delete(ALL)
        for i in range(0, self.__game.getRows()):
            for j in range(0, self.__game.getCols()):
                self.__canvas.create_rectangle(j * self.__size, i * self.__size,
                                               (j + 1) * self.__size, (i + 1) * self.__size,
                                               width=0, fill=colors[self.__game.getVal(i, j)])

    def evolve(self):
        self.__game.nextState()
        self.display()
        self.after(10, self.evolve)  # Rappel de la fonction toutes les 10ms.


if (__name__ == "__main__"):
    Window(40, 40, 10)
