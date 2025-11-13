#!/usr/bin/env python3

from tkinter import *
from random import choice
from math import sqrt


class Ball:
    
    __radius = 10
    __diameter = 2 * __radius
    __gravity = 0.2
    __impact = 0.6
    __balls = []
    __collisions = []

    def getBalls(): return Ball.__balls
    def emptyBalls(): Ball.__balls = []

    def nextState():
        Ball.__collisions = []
        
        for i in range(0, len(Ball.__balls)):
            for j in range(i + 1, len(Ball.__balls)):
                if ((Ball.__balls[i].__x - Ball.__balls[j].__x) ** 2 + (Ball.__balls[i].__y - Ball.__balls[j].__y) ** 2 < (Ball.__radius * 2) ** 2):
                    Ball.__collisions.append((Ball.__balls[i], Ball.__balls[j]))
        
        for (first, second) in Ball.__collisions: Ball.collisions(first, second)
            
    def collisions(first, second):
        distance = sqrt((first.__x - second.__x) ** 2 + (first.__y - second.__y) ** 2)
        rate = Ball.__diameter / distance
        deltax = (rate - 1) * abs(first.__x - second.__x) + 2
        deltay = (rate - 1) * abs(first.__y - second.__y)
        
        dx = first.__x - second.__x
        dy = first.__y - second.__y
        
        if (dx < 0):
            first.__x -= deltax / 2
            second.__x += deltax / 2
        else:
            first.__x += deltax / 2
            second.__x -= deltax / 2
            
        if (dy < 0):
            first.__y -= deltay / 2
            second.__y += deltay / 2
        else:
            first.__y += deltay / 2
            second.__y -= deltay / 2
            
        if ((dx < 0 and first.__dx >= 0) or (dx >= 0 and first.__dx < 0)):
            first.__dx = -first.__dx * Ball.__impact
            first.__dy = -first.__dy * Ball.__impact
            
        if ((dx < 0 and second.__dx < 0) or (dx >= 0 and second.__dx >= 0)):
            second.__dx = -second.__dx * Ball.__impact
            second.__dy = -second.__dy * Ball.__impact

        if (abs(first.__dx) > abs(second.__dx)): second.__dx -= first.__dx
        elif (abs(first.__dx) < abs(second.__dx)): first.__dx -= second.__dx
        else:
            a = first.__dx
            first.__dx -= second.__dx
            second.__dx -= a
            
    def __init__(self, x, y, dx, dy, id = 0):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__dx = dx
        self.__dy = dy
        self.__lasty = 1 - y
        
        Ball.__balls.append(self)
        
    def getId(self): return self.__id
    def deriv(self): return abs(self.__y - self.__lasty)
        
    def evolve(self, **limits):
        (x0, y0, x1, y1) = self.getCoords()
        if (y1 >= limits['height']):
            self.__dy *= -Ball.__impact
            self.__y = limits['height'] - Ball.__radius
            
        if (x1 >= limits['width'] or x0 <= 0): 
            self.__dx = -self.__dx
            if (x0 <= 0): self.__x = Ball.__radius
            else: self.__x = limits['width'] - Ball.__radius
            
        if (self.deriv() < 1.0e-8): self.__dx *= 0.98
        
        self.__lasty = self.__y
        self.__dy += Ball.__gravity
        
        self.__x += self.__dx
        self.__y += self.__dy
        
    def getCoords(self):
        return (self.__x - Ball.__radius, self.__y - Ball.__radius, self.__x + Ball.__radius, self.__y + Ball.__radius)
        
        
class Window(Tk):

    def __init__(self, w, h, r):
        Tk.__init__(self)
        
        self.__width = w
        self.__height = h
        self.__radius = r
        self.__colors = ["black", "yellow", "red", "green", "brown", "gray", "purple", "blue"]
        
        self.__canvas = Canvas(self, width=w, height=h)
        self.__canvas.pack(side=TOP)
        Button(self, text="Clear", command=self.clear).pack(side=BOTTOM)

        self.geometry(str(w) + "x" + str(h + 30))
        self.resizable(False, False)
        self.title("Physic")
        
        self.__canvas.bind("<Button-1>", lambda event: self.addBall(event, -1))
        self.__canvas.bind("<Button-3>", lambda event: self.addBall(event, 1))
        
        self.clear()
        self.evolve()
        
        self.mainloop()
        
    def clear(self):
        self.__canvas.delete(ALL)
        self.__canvas.create_rectangle(0, 0, self.__width, self.__height, width=0, fill="white")
        Ball.emptyBalls()
        
    def evolve(self):
        Ball.nextState()
        for ball in Ball.getBalls():
            ball.evolve(width=self.__width, height=self.__height)
            self.__canvas.coords(ball.getId(), ball.getCoords())
        self.after(10, self.evolve)
        
    def addBall(self, event, dy):
        color = choice(self.__colors)
        id = self.__canvas.create_oval(0, 0, 0, 0, outline=color, fill=color)
        Ball(event.x, event.y, dy, 0, id)

        
if (__name__ == "__main__"):
    Window(640, 480, 20)
