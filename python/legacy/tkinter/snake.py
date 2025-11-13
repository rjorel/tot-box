#!/usr/bin/env python3


from tkinter import *
from random import randrange


class Snake:
    def __init__(self, d):
        self.__body = []
        self.__dir = d

    def addHead(self, coords):
        self.__body.append(coords)
    
    def delTail(self):
        del(self.__body[0])
    
    def next(self, **limits):
        x = self.__body[-1][0]
        y = self.__body[-1][1]
        xlimit = limits.get("xlimit", 100)
        ylimit = limits.get("ylimit", 100)

        if (self.__dir == "left"):    x, y = x - 1, y     # Add moves according direction.
        elif (self.__dir == "right"): x, y = x + 1, y
        elif (self.__dir == "up"):    x, y = x, y - 1
        elif (self.__dir == "down"):  x, y = x, y + 1

        if (x < 0):       x = xlimit - 1                   # Bounds check.
        if (x >= xlimit): x = 0
        if (y < 0):       y = ylimit - 1
        if (y >= ylimit): y = 0

        return (x, y)

    def belongs(self, coords): return coords in self.__body
    def setDir(self, d): self.__dir = d
    def getDir(self): return self.__dir
    def getHead(self): return self.__body[-1]
    def getTail(self): return self.__body[0]


class Window(Tk):
    def __init__(self, cols, rows, size, fg, bg, gc):
        Tk.__init__(self)
        
        self.__cols = cols
        self.__rows = rows
        self.__size = size
        self.__fgcolor = fg
        self.__bgcolor = bg
        self.__goalcolor = gc

        self.__time = 100
        self.__snake = Snake("left")
        
        for i in range(1, -2, -1):             # Set up the snake (3 boxes at beginning).
            self.__snake.addHead((cols // 2 + i, rows // 2))

        self.__canvas = Canvas(self, width=cols * size, height=rows * size)
        self.__canvas.pack(side=TOP)
        self.__id = []
        self.__cursor = 0
        self.__sizeSnake = 3
 
        self.geometry(str(cols * size) + "x" + str(rows * size))
        self.resizable(False, False)
        self.title("Snake")
         
        self.bind("<KeyPress-z>", self.changeDirUp)        # Key bindings.
        self.bind("<KeyPress-s>", self.changeDirDown)
        self.bind("<KeyPress-q>", self.changeDirLeft)
        self.bind("<KeyPress-d>", self.changeDirRight)

        self.__canvas.create_rectangle(0, 0, cols * size, rows * size, width=0, fill=bg)

        for i in range(1, -2, -1):                          # Draw the boxes.
            self.__id.append(self.__canvas.create_rectangle((cols // 2 + i) * size, (rows // 2) * size,
                                                            (cols // 2 + (i + 1)) * size, (rows // 2 + 1) * size,
                                                            width=0, fill=fg))
        col = randrange(0, cols)
        row = randrange(0, rows)
        self.__goal = (col, row)                           # Goal and score.
        self.__goalId = self.__canvas.create_rectangle(col * size, row * size, (col + 1) * size, (row + 1) * size,
                                                       width=0, fill=gc)
        self.__scoreId = self.__canvas.create_text(20, rows * size - 10, text="0")

        self.evolve()
        self.mainloop()
         
    def changeDirUp(self, event):
        if (self.__snake.getDir() != "down"):
            self.__snake.setDir("up")
    
    def changeDirDown(self, event):
        if (self.__snake.getDir() != "up"):
            self.__snake.setDir("down")
    
    def changeDirLeft(self, event):
        if (self.__snake.getDir() != "right"):
            self.__snake.setDir("left")
    
    def changeDirRight(self, event):
        if (self.__snake.getDir() != "left"):
            self.__snake.setDir("right")

    def evolve(self):
        col, row = self.__snake.next(xlimit=self.__rows, ylimit=self.__cols)   # Get the next head.
        
        if (self.__snake.belongs((col, row))):      # The head touchs the body.
            self.__canvas.create_text(self.__cols // 2 * self.__size, self.__rows // 2 * self.__size,
                                      text="You lose !", fill=self.__fgcolor)
            self.after(1000, self.quit)
        
        else:
            if (col == self.__goal[0] and row == self.__goal[1]):   # Goal is reached.
                gcol = randrange(0, self.__cols)                    # New goal position.
                grow = randrange(0, self.__rows)
                self.__goal = (gcol, grow)
                self.__canvas.coords(self.__goalId, gcol * self.__size, grow * self.__size,
                                                   (gcol + 1) * self.__size, (grow + 1) * self.__size)
                # Add a canvas id, for the new box.
                self.__id.insert(self.__cursor, self.__canvas.create_rectangle(
                                                            -1, -1, -1, -1,
                                                            width=0, fill=self.__fgcolor))

                self.__sizeSnake += 1
                self.__canvas.itemconfig(self.__scoreId, text=str((self.__sizeSnake - 3) * 100))   # Edit score.
                self.__time -= 2

            else:
                self.__snake.delTail()
            
            self.__snake.addHead((col, row))
            self.__canvas.coords(self.__id[self.__cursor], col * self.__size, row * self.__size,
                                                           (col + 1) * self.__size, (row + 1) * self.__size)
        
            self.__cursor += 1                     # Canvas id used to move tail to head.
            self.__cursor %= self.__sizeSnake
            
            self.after(self.__time, self.evolve)


if  (__name__ == "__main__"):
    Window(40, 40, 10, "black", "white", "red")
