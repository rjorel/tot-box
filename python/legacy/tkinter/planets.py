#!/usr/bin/env python3

from tkinter import *
import math


class Window(Tk):
    
    def __init__(self, w, h):
        Tk.__init__(self)
        
        self.__width = w
        self.__height = h
        
        self.__canvas = Canvas(self, width=w, height=h)
        self.__canvas.grid(columnspan=2)
        
        self.__distanceLabel = Label(self)
        self.__distanceLabel.grid(row=1, column=0)
        self.__forceLabel = Label(self)
        self.__forceLabel.grid(row=1, column=1)
        
        self.__weightLabel1 = Label(self)
        self.__weightLabel1.grid(row=2, column=0)
        self.__weightLabel2 = Label(self)
        self.__weightLabel2.grid(row=2, column=1)
                
        self.__scale1 = Scale(self, from_=10, orient=HORIZONTAL, command=self.changeSize)
        self.__scale1.grid(row=3, column=0)
        self.__scale2 = Scale(self, from_=10, orient=HORIZONTAL, command=self.changeSize)
        self.__scale2.grid(row=3, column=1)
        
        self.geometry(str(w) + "x" + str(h + 100))
        self.resizable(False, False)
        self.title("Planets")
        self.initPosition()
        
        self.__canvas.bind("<Button-1>", self.moveFirst)
        self.__canvas.bind("<Button-3>", self.moveSecond)
        self.mainloop()
        
    def initPosition(self):
        self.__canvas.create_rectangle(0, 0, self.__width, self.__height, width=0, fill="white")
        
        self.__x1 = self.__width // 4
        self.__y1 = self.__height // 4
        self.__r1 = 10
        
        self.__x2 = 3 * self.__width // 4
        self.__y2 = 2 * self.__height // 3
        self.__r2 = 10
        
        self.__first = self.__canvas.create_oval(self.__x1 - self.__r1, self.__y1 - self.__r1,
                                                 self.__x1 + self.__r1, self.__y1 + self.__r1)
        self.__second = self.__canvas.create_oval(self.__x2 - self.__r2, self.__y2 - self.__r2,
                                                  self.__x2 + self.__r2, self.__y2 + self.__r2)
        self.update()
        
    def update(self):
        self.__canvas.coords(self.__first, self.__x1 - self.__r1, self.__y1 - self.__r1, 
                                           self.__x1 + self.__r1, self.__y1 + self.__r1)
        self.__canvas.coords(self.__second, self.__x2 - self.__r2, self.__y2 - self.__r2,
                                            self.__x2 + self.__r2, self.__y2 + self.__r2)
        
        distance = math.sqrt((self.__x1 - self.__x2) ** 2 + (self.__y1 - self.__y2) ** 2)
        self.__weight1 = math.pi * self.__r1 ** 2
        self.__weight2 = math.pi * self.__r2 ** 2
        
        self.__distanceLabel.configure(text="Distance : " + str(distance) + "u")
        self.__forceLabel.configure(text="Force : " + str((self.__weight1 * self.__weight2 * 6.67e-11) / distance ** 2) + "SI")
        self.__weightLabel1.configure(text="Weight 1 : " + str((self.__weight1)))
        self.__weightLabel2.configure(text="Weight 2 : " + str((self.__weight2)))

    def moveFirst(self, event):
        self.__x1 = event.x
        self.__y1 = event.y
        self.update()
        
    def moveSecond(self, event):
        self.__x2 = event.x
        self.__y2 = event.y
        self.update()
        
    def changeSize(self, val):
        self.__r1 = self.__scale1.get()
        self.__r2 = self.__scale2.get()
        self.__weight1 = math.pi * self.__r1 ** 2
        self.__weight2 = math.pi * self.__r2 ** 2
        self.update()
        
        
if (__name__ == "__main__"):
    Window(640, 480)
