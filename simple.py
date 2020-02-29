from tkinter import *
from tkinter import messagebox

master = Tk()
master.geometry("500x200")

def close_window():
    master.destroy()
    
# This is the main function
def main():

    # The labels to be use
    variableLabel = Label(master, text='How many variables does the problem has? ')
    constraintsLabel = Label(master, text='How many constraints?')

    # The buttton
    button = Button(master, text="Next", command=close_window)

    # The input of the user
    variableEntry = Entry(master, textvariable="variable")
    constraintsEntry = Entry(master, textvariable="constraint")

    # The position on the window
    variableLabel.place(x=0, y=0)
    constraintsLabel.place(x=0, y=20)
    button.place(x=50, y=50)
    variableEntry.place(x=300,y=0)
    constraintsEntry.place(x=300, y=20)
    master.mainloop()

main()