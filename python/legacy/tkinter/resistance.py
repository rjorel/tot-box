#!/usr/bin/env python3

from tkinter import *
from math import log10, floor


class Resistance:
    # Possible colors for resistor rings.
    __COLORS = ["black", "brown", "red", "orange", "yellow",
                "green", "blue", "purple", "grey", "white",
                "silver", "gold"]

    def __init__(self):
        self.__root = Tk()
        self.__init_interface()
        
        self.__root.geometry("300x200")
        self.__root.resizable(False, False)
        self.__root.title("Resistance")

        self.__root.mainloop()

    def __init_interface(self):
        # Canvas initialization: white background, placement at the window top.
        self.__canvas = Canvas(self.__root, width=300, height=150, bg="white")
        self.__canvas.grid(row=1, column=1, columnspan=3)

        # Label for giving resistance value.
        Label(self.__root, text="Value :").grid(row=2, column=1)
        self.__value = Entry(self.__root, width=14)
        self.__value.grid(row=2, column=2)

        # Button to display a resistance value.
        Button(self.__root, text="Display", command=self.change_color).grid(row=2, column=3)

        # Color rings.
        self.__ringsId = []
        self.__canvas.create_line(10, 75, 290, 75, width=5)
        self.__canvas.create_rectangle(40, 30, 260, 120, fill="light grey")
        
        for i in range(60, 240, 60):
            self.__ringsId.append(self.__canvas.create_rectangle(i, 30, i + 15, 120, fill="black"))
       

    def change_color(self):
        # Gets the value from entry widget.
        try:
            value = float(self.__value.get())
            vlog = floor(log10(value)) - 1
        except:
            self.error()
            return

        # If the order is not handle, it's an error.
        if (vlog < -2 or vlog > 7):
            self.error()
            return

        # Ring values are computed..
        index = [0, 0, 0]
        vscaled = int(value / (10 ** (vlog)))

        index[0] = vscaled // 10
        index[1] = vscaled % 10
        index[2] = vlog

        # .. and displayed.
        for i in range(0, 3):
            self.__canvas.itemconfigure(self.__ringsId[i], fill=Resistance.__COLORS[index[i]])
       
    def error(self):
        self.__value.configure(bg="red")
        self.__root.after(1000, self.reset)

    def reset(self):
        self.__value.configure(bg="white")
        self.__value.delete(0, END)
        

if (__name__ == "__main__"):
    Resistance()