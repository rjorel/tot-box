#!/usr/bin/env python3

from math import cos, sin, radians
from tkinter import *


class Clock:
    def __init__(self, h = 0, m = 0, s = 0):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def evolve(self, s = 1):
        self.__seconds += s

        self.__minutes += self.__seconds // 60
        self.__seconds %= 60

        self.__hours += self.__minutes // 60
        self.__minutes %= 60

        self.__hours %= 12

    def get_time(self):
        return (self.__hours, self.__minutes, self.__seconds)


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def rotation(self, center, radius = 0):
        xres = (self.x - center.x) * cos(radians(radius)) \
                    + (self.y - center.y) * sin(radians(radius))

        yres = (self.y - center.y) * cos(radians(radius)) \
                    - (self.x - center.x) * sin(radians(radius))

        return Point((xres + center.x), (yres + center.y))

    
class Window(Tk):

    def __init__(self, size):
        Tk.__init__(self)

        self.__clock = Clock()
        self.__size = size

        # Origin points for center and clock hands.
        self.__porigin = Point(size / 2, size / 2)
        self.__phours = Point(size / 2, 120)
        self.__pmins = Point(size / 2, 60)
        self.__psecs = Point(size / 2, 15)

        # Canvas ids.
        self.__hourId = 0
        self.__minId = 0
        self.__secId = 0
        
        self.__canvas = Canvas(self, width=self.__size, height=self.__size)
        self.__canvas.pack(side=TOP, padx=5, pady=5)
        
        self.geometry(str(self.__size) + "x" + str(self.__size))
        self.resizable(False, False)
        self.title("Clock")
        
        self.draw()
        self.advance()
        self.mainloop()
        
    def draw(self):
        # Initial clock drawing.
        self.__canvas.create_oval(15, 15, self.__size - 15, self.__size - 15, fill="white", width=5)

        # Hands.
        phours = self.__phours.rotation(self.__porigin)
        pmins = self.__pmins.rotation(self.__porigin)
        psecs = self.__psecs.rotation(self.__porigin)

        self.__hourId = self.__canvas.create_line(self.__porigin.x, self.__porigin.y,
                                                  phours.x, phours.y, fill="green")
        self.__minId = self.__canvas.create_line(self.__porigin.x, self.__porigin.y,
                                                 pmins.x, pmins.y, fill="red")
        self.__secId = self.__canvas.create_line(self.__porigin.x, self.__porigin.y,
                                                 psecs.x, psecs.y, fill="blue")

        # Graduations.
        # Minutes / seconds.
        opsup = Point(self.__size / 2, 15)     # Origin superior point.
        opinf = Point(self.__size / 2, 30)     # Origin inferior point.

        for i in range(0, 60):
            psup = opsup.rotation(self.__porigin, -i * 6)
            pinf = opinf.rotation(self.__porigin, -i * 6)

            self.__canvas.create_line(psup.x, psup.y, pinf.x, pinf.y)

        # Hours.
        opinf = Point(self.__size / 2, 50)     # Origin inferior point.

        for i in range(0, 12):
            psup = opsup.rotation(self.__porigin, -i * 30)
            pinf = opinf.rotation(self.__porigin, -i * 30)

            self.__canvas.create_line(psup.x, psup.y, pinf.x, pinf.y)
        
    def advance(self):
        # Next second.
        self.__clock.evolve()
        (hours, mins, secs) = self.__clock.get_time()

        phours = self.__phours.rotation(self.__porigin, -hours * 30 - mins / 2)
        pmins = self.__pmins.rotation(self.__porigin, -mins * 6 - secs / 10)
        psecs = self.__psecs.rotation(self.__porigin, -secs * 6)

        # Hand movement.
        self.__canvas.coords(self.__hourId, self.__porigin.x, self.__porigin.y,
                             phours.x, phours.y)
        self.__canvas.coords(self.__minId, self.__porigin.x, self.__porigin.y,
                             pmins.x, pmins.y)
        self.__canvas.coords(self.__secId, self.__porigin.x, self.__porigin.y,
                             psecs.x, psecs.y)

        self.after(100, self.advance)

        
if (__name__ == "__main__"):
    Window(500)
