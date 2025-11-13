#!/usr/bin/env python3

from tkinter import *
from math import sin, pi


class Oscillo(Canvas):
    def __init__(self, boss = None, w = 320, h = 240, grid = True):
        Canvas.__init__(self, boss)
        
        self.__width = w
        self.__height = h

        self.configure(width=w, height=h)

        self.grid(grid)
        self.create_line(10, h / 2, w, h / 2, arrow=LAST)
        self.create_line(10, h - 10, 10, 10, arrow=LAST)

    def grid(self, expand):
        step = (self.__width - 25) / 10       # a mark every 1/10s.
        
        if (expand):
            ymin = self.__height / 2 - (10 * self.__height / 25)       # min et max signal value for an amplitude of 10.
            ymax = self.__height / 2 + (10 * self.__height / 25)
            
            for i in range(1, 11):
                x = 10 + i * step
                self.create_line(x, int(ymin), x, int(ymax), fill="light grey")

            step = (ymax - ymin) / 10
            for i in range(0, 11):
                y = ymin + i * step
                self.create_line(10, int(y), self.__width - 15, int(y), fill="light grey")

        else:
            for i in range(1, 11):
                x = 10 + i * step
                self.create_line(x, self.__height / 2 - 5, x, self.__height / 2 + 5)
            
    def trace(self, frequency = 1, phase = 0, amplitude = 10, color = "blue"):
        step = (self.__width - 25) / 1000      # 1 secon divided in 1000ms
       
        points = []
        for t in range(1, 1001, 5):
            e = amplitude * sin(2 * pi * frequency * t / 1000 - phase)
            x = 10 + t * step
            y = self.__height / 2 - e * self.__height / 25
            points.append((x, y))

        return self.create_line(points, fill=color, smooth=True)


class ValueSignal(Frame):
    def __init__(self, boss = None):
        Frame.__init__(self, boss)

        self.__frequency = 0
        self.__phase = 0
        self.__amplitude = 0

        self.configure(bd=2, relief=GROOVE)

        self.__displayButton = IntVar()
        Checkbutton(self, text="Display", variable=self.__displayButton, command=self.check).pack(side=LEFT)
        
        Scale(self, length=200, orient=HORIZONTAL, sliderlength=25, label="Frequency (Hz)", from_=0, to=20,
              tickinterval=5, resolution=0.2, command=lambda value: self.setValue("frequency", value)).pack(side=LEFT)
        Scale(self, length=200, orient=HORIZONTAL, sliderlength=15, label="Phase (Degrees)", from_=-180, to=180,
              tickinterval=90, resolution=1, command=lambda value: self.setValue("phase", value)).pack(side=LEFT)
        Scale(self, length=200, orient=HORIZONTAL, sliderlength=25, label="Amplitude", from_=0, to=10,
              tickinterval=2, resolution=0.2, command=lambda value: self.setValue("amplitude", value)).pack(side=LEFT)
        
    def check(self):
        self.event_generate("<Control-Z>")

    def setValue(self, scale, value):
        if (scale == "frequency"):   self.__frequency = float(value)
        elif (scale == "phase"):     self.__phase = float(value)
        elif (scale == "amplitude"): self.__amplitude = float(value)

        self.event_generate("<Control-Z>")

    def getValues(self):
        return (self.__displayButton.get(), self.__frequency, self.__phase, self.__amplitude)


class Application:
    def __init__(self, numCurves = 3, w = 320, h = 240, **args):
        self.__root = Tk()
        
        self.__oscillo = Oscillo(self.__root, w, h)
        self.__oscillo.pack(side=TOP, padx=10, pady=10)

        self.__numCurves = numCurves
        self.__oscillo.configure(bg="white", bd=2, relief=SOLID)
        
        self.__colors = args.get('colors', ["blue"] * numCurves)
        self.__signals = [0] * numCurves
        self.__curves = [0] * numCurves

        for i in range(0, numCurves):
            self.__signals[i] = ValueSignal(self.__root)
            self.__signals[i].pack(side=BOTTOM, padx=10, pady=5)

        self.__root.resizable(False, False)
        self.__root.title("Oscilloscope")

        self.__root.bind("<Control-Z>", self.show)
        self.__root.mainloop()

    def show(self, event):
        for i in range(0, self.__numCurves):
            self.__oscillo.delete(self.__curves[i])

            (display, freq, phase, amp) = self.__signals[i].getValues()
            if (display):
                self.__curves[i] = self.__oscillo.trace(freq, phase, amp, self.__colors[i])


if (__name__ == "__main__"):
    Application(4, 600, 200, colors = ["blue", "red", "green", "purple"])
