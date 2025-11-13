#!/usr/bin/env python3

from tkinter import *
from random import randrange
from random import choice


class Item:
    def __init__(self, x, y, w, h, id = 0):
        self.__id = id
        self.__x = x
        self.__y = y
        self._width = w
        self._height = h
        
    def getId(self): return self.__id
    def getCoords(self): return (self.__x, self.__y, self.__x + self._width, self.__y + self._height)
    def setCoords(self, x, y):
        self.__x = x
        self.__y = y

    def move(self, dx = 0, dy = 0, **limits):
        self.__x += dx
        self.__y += dy
        
        if (self.__x < 0): self.__x = 0
        if (self.__x + self._width > limits['width']): self.__x = limits['width'] - self._width
        if (self.__y < 0): self.__y = 0
        if (self.__y + self._height > limits['height']): self.__y = limits['height'] - self._height


class Ball(Item):
    __SPEED = 4
    
    def __init__(self, x, y, w, h, id = 0):
        Item.__init__(self, x, y, w, h, id)
        self.__dx = 0
        self.__dy = 0
        
    def setDeltax(self, dx): self.__dx = dx
    def setDeltay(self, dy): self.__dy = dy
    
    def evolve(self, **limits):
        self.move(self.__dx * Ball.__SPEED, self.__dy * Ball.__SPEED, width=limits['width'], height=limits['height'])
        
        (x1, y1, x2, y2) = self.getCoords()
        if (y1 <= 0 or y2 >= limits['height']): self.__dy = -self.__dy
        
        xmiddle = x1 + self._width / 2
        ymiddle = y1 + self._height / 2
        
        for player in limits['players'].values():
            xpmiddle = (player['xmax'] - player['xmin']) / 2 + player['xmin']
            ypmiddle = (player['ymax'] - player['ymin']) / 2 + player['ymin']
            pwidth = player['xmax'] - player['xmin']
            pheight = player['ymax'] - player['ymin']
            
            if ((abs(xmiddle - xpmiddle) <= (self._width + pwidth) / 2) and (abs(ymiddle - ypmiddle) <= (self._height + pheight) / 2)):
                self.__dx = -self.__dx
                if (self.__dy < 0):
                    if (ymiddle < ypmiddle): self.__dy *= 1.2
                    else: self.__dy *= 0.8
                else:
                    if (ymiddle < ypmiddle): self.__dy *= 0.8
                    else: self.__dy *= 1.2
                    
                if (player['xmin'] + 2 < xmiddle < player['xmax'] - 2): 
                    self.__dy = -self.__dy
                    self.__dy *= 2
                return True
        return False
        

class Game(Tk):
    __MOVE_WAIT = 1
    
    def __init__(self, w, h):
        Tk.__init__(self)
        
        self.__width = w
        self.__height = h
        self.__move = 0
        self.__dy = 0
        self.__scorePlayer = 0
        self.__scoreIA = 0
        self.__canvas = Canvas(self, width=w, height=h, bg="black", bd=0)
        self.__canvas.pack()
        self.__textPlayer = self.__canvas.create_text(50, 20, font="Courier", text="0", fill="white")
        self.__textIA = self.__canvas.create_text(w - 50, 20, font="Courier", text="0", fill="white")
        
        self.__player = Item(10, h // 2 - 20, 10, 40, self.__canvas.create_rectangle(0, 0, 0, 0, width=0, fill="white"))
        self.__ia = Item(w - 20, h // 2 - 20, 10, 40, self.__canvas.create_rectangle(0, 0, 0, 0, width=0, fill="white"))
        self.__ball = Ball(0, 0, 10, 10, self.__canvas.create_rectangle(0, 0, 0, 0, width=0, fill="white"))
        
        self.geometry(str(w) + "x" + str(h))
        self.resizable(False, False)
        self.title("Pong")
        
        self.bind("<KeyPress-z>", lambda event: self.playerMove(event, -10))   # For fluidity.
        self.bind("<KeyRelease-z>", self.playerStop)
        self.bind("<KeyPress-s>", lambda event: self.playerMove(event, 10))
        self.bind("<KeyRelease-s>", self.playerStop)
        self.newGame()
        self.evolve()
        self.mainloop()
        
    def playerMove(self, event, dy): self.__dy = dy
    def playerStop(self, event): self.__dy = 0
        
    def newGame(self):
        x = randrange(0, self.__width)
        self.__ball.setCoords(x, randrange(0, self.__height))
        
        if (x <= self.__width // 2): self.__ball.setDeltax(1)
        else: self.__ball.setDeltax(-1)
        self.__ball.setDeltay(choice([-1, 1]))
        
    def evolve(self):
        (x11, y11, x12, y12) = self.__player.getCoords()
        (x21, y21, x22, y22) = self.__ia.getCoords()
        
        self.__player.move(0, self.__dy, width=self.__width, height=self.__height)
        self.__canvas.coords(self.__player.getId(), x11, y11, x12, y12)
        
        self.__ball.evolve(width=self.__width, height=self.__height,
                           players={'first': {'xmin': x11, 'xmax': x12, 'ymin': y11, 'ymax': y12},
                                    'second': {'xmin': x21, 'xmax': x22, 'ymin': y21, 'ymax': y22}})
        (x1, y1, x2, y2) = self.__ball.getCoords()
        
        if (self.__move == Game.__MOVE_WAIT):
            if (y1 < y21): self.__ia.move(0, -10, width=self.__width, height=self.__height)
            if (y2 > y22): self.__ia.move(0, 10, width=self.__width, height=self.__height)
            self.__move = 0
        else: self.__move += 1
        self.__canvas.coords(self.__ia.getId(), x21, y21, x22, y22)
        
        if (x1 <= 0 or x2 >= self.__width): 
            self.newGame()
            if (x1 <= 0): 
                self.__scoreIA += 1
                self.__canvas.itemconfig(self.__textIA, text=str(self.__scoreIA))
            else:
                self.__scorePlayer += 1
                self.__canvas.itemconfig(self.__textPlayer, text=str(self.__scorePlayer))
        self.__canvas.coords(self.__ball.getId(), self.__ball.getCoords())

        self.after(10, self.evolve)
    
        
if (__name__ == "__main__"):
    Game(640, 480)
