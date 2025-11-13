#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog


class SelectionTable(Frame):
    """ Table to display value, and select columns """

    def __init__(self, parent = None, rows = 0, columns = 0, values = []):
        Frame.__init__(self, parent, background="white", borderwidth=2, relief=SUNKEN)
      
        self.__rows = rows
        self.__columns = columns
        self.__widget_ids = []
        self.__selectedColumns = [False] * columns     # No column is selected at beginning.

        # Columns name.
        col_ids = []
        for col in range(0, columns):
            label = Label(self, text=values[0][col], background="#BBBBBB",
                                font=("", 9, "bold"), borderwidth=1, width=8, anchor=W)
            label.grid(row=0, column=col, padx=1, pady=1)

            # Each column name can be clickable, to select the entire column.
            label.bind("<Button-1>", lambda event, column=col: self.select(column))
            col_ids.append(label)

        self.__widget_ids.append(col_ids)

        # Columns values.
        for row in range(1, rows):
            col_ids = []
            for col in range(0, columns):
                label = Label(self, text=values[row][col], background="#DDDDDD",
                                    font=("", 9), borderwidth=1, width=8, anchor=W)
                label.grid(row=row, column=col, padx=1, pady=1)
                col_ids.append(label)

            self.__widget_ids.append(col_ids)


    def set(self, row, column, value):
        self.__widget_ids[row][column].configure(text=value)

    def select(self, index):
        self.__selectedColumns[index] = not self.__selectedColumns[index]

        if (self.__selectedColumns[index]):
            for row in range(1, self.__rows):
                self.__widget_ids[row][index].configure(background="green")

        else:
            for row in range(1, self.__rows):
                self.__widget_ids[row][index].configure(background="#DDDDDD")

    def get_selected_columns(self):
        return list(self.__selectedColumns)
        

class Window:
    def __init__(self):
        self.__root = Tk()

        # Window configuration.
        self.__list_fields = []
        self.__table = SelectionTable()

        self.__buttons_frame = Frame(self.__root)
        Button(self.__buttons_frame, text="Import CSV file", command=self.import_file).pack(side=LEFT)
        Button(self.__buttons_frame, text="Merge", command=self.merge).pack(side=LEFT)
        Button(self.__buttons_frame, text="Save", command=self.save).pack(side=RIGHT)
        self.__buttons_frame.pack(side=BOTTOM)

        self.__root.title("CSV Handler")
        self.__root.geometry("300x500")
        self.__root.resizable(False, False)
        self.__root.mainloop()


    def load_table(self):
        # New table.
        self.__table.destroy()
        self.__table = SelectionTable(self.__root, len(self.__list_fields), len(self.__list_fields[0]),
                                      self.__list_fields)
        self.__table.pack(side=TOP, pady=2)

        if (len(self.__list_fields[0]) * 80 < 300):      # The window must not be too little.
            self.__root.geometry("300x500")
        else:
            self.__root.geometry(str(len(self.__list_fields[0]) * 80) + "x500") # Fit the window to the columns number.

    def import_file(self):
        # Import file from user selection.
        filename = filedialog.askopenfilename()
        if (not filename.endswith('csv')): return

        fd = open(filename, "r")
        lines = [line for line in fd.read().split('\n') if (line != '')]
        lines = lines[:22]         # Keep just the 21 first lines, to avoid useless processings.
        fd.close()

        self.__list_fields = []
        for line in lines:
            self.__list_fields.append(line.split(','))

        self.load_table()

    def merge(self):
        selected_fields = self.__table.get_selected_columns()
        indexes = [index for (index, value) in enumerate(selected_fields) if (value == True)]
        if (len(indexes) != 2): return      # If the user didn't select exactly 2 fields, no action.

        for line in self.__list_fields:
            line[indexes[0]] += line[indexes[1]]
            del(line[indexes[1]])

        self.load_table()

    def save(self):
        filename = filedialog.asksaveasfilename()
        fd = open(filename, "w")

        for line in self.__list_fields:
            fd.write(",".join(line) + '\n')

        fd.close()


if (__name__ == "__main__"):
    Window()