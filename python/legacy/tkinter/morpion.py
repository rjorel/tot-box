#!/usr/bin/env python3

from tkinter import *


class Window(Tk):

    def __init__(self, size):
        Tk.__init__(self)

        self.__size = size
        self.__tile = size // 3
        self.__canvas = Canvas(self, width=self.__size, height=self.__size)
        self.__canvas.pack(side=TOP, padx=5, pady=5)

        self.geometry(str(self.__size) + "x" + str(self.__size))
        self.resizable(False, False)
        self.title("Morpion")

        self.init()
        self.mainloop()

    def init(self):
        self.__player = -1  # -1 -> cross, 1 -> circle.
        self.__turns = 0
        self.__board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        self.__canvas.delete(ALL)
        for i in range(0, 3):
            self.__canvas.create_line(0, i * self.__size / 3, self.__size, i * self.__size / 3,
                                      fill="black")
            self.__canvas.create_line(i * self.__size / 3, 0, i * self.__size / 3, self.__size,
                                      fill="black")

        self.__canvas.bind("<Button-1>", self.play)

    def play(self, event):
        posx = event.x // self.__tile
        posy = event.y // self.__tile

        if (self.__board[posy][posx] == 0):
            if (self.__player == -1):
                self.__canvas.create_line(posx * self.__tile + 10, posy * self.__tile + 10,
                                          (posx + 1) * self.__tile - 10,
                                          (posy + 1) * self.__tile - 10, fill="blue")
                self.__canvas.create_line(posx * self.__tile + 10, (posy + 1) * self.__tile - 10,
                                          (posx + 1) * self.__tile - 10, posy * self.__tile + 10,
                                          fill="blue")
            else:
                self.__canvas.create_oval(posx * self.__tile + 10, posy * self.__tile + 10,
                                          (posx + 1) * self.__tile - 10,
                                          (posy + 1) * self.__tile - 10, outline="green")

            self.__board[posy][posx] = self.__player

            if (self.check(posx, posy)):
                self.end(self.__player)
            else:
                self.__turns += 1
                if (self.__turns >= 9):
                    self.end(0)

            self.__player *= -1

    def check(self, x, y):
        i = 0
        while (i < 3 and self.__board[i][x] == self.__player): i += 1
        if (i == 3): return True

        i = 0
        while (i < 3 and self.__board[y][i] == self.__player): i += 1
        if (i == 3): return True

        if (x == y):
            i = 0
            while (i < 3 and self.__board[i][i] == self.__player): i += 1
            if (i == 3): return True

        if (x == 2 - y):
            i = 0
            while (i < 3 and self.__board[i][2 - i] == self.__player): i += 1
            if (i == 3): return True

        return False

    def end(self, player):
        text = ["Crosses won", "Draw", "Circles won"]
        self.__canvas.unbind("<Button-1>")
        self.__canvas.create_text(self.__size // 2, self.__size // 2, text=text[player + 1],
                                  fill="red")
        self.after(2000, self.init)


if (__name__ == "__main__"):
    Window(500)
