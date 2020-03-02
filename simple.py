from tkinter import *
from tkinter import filedialog as fd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import sys

# This function does everything with the graphing
def showfunction(functions):

    # This gets the max point to show the linear function
    max_number = 0
    length_of_matrix = len(functions)
    for i in functions:
        max_number = max(i[len(i)-1],max_number)

    # Adds the range of the X dimension
    x = np.array(range(0, max_number))

    # Adds the linear function to the graph
    for i in range(length_of_matrix-1):
        y = eval("(" + str(functions[i][-1]) + "-" + str(functions[i][0]) + "*x)/" + str(functions[i][1]))
        plt.plot(x, y)

    # Saves the image, this is necesary because we need to open it later
    plt.savefig('graph.png')


def calculate(second_window, matrices, matrix_function):

    # First we need to destroy the previous window, we do not need it anymore
    second_window.destroy()

    third_window = Tk()
    third_window.geometry("1500x800")
    
    
    column_pivot = 0
    column_number = 0
    row_pivot = 0
    row_number = sys.maxsize
    
    for x in range(len(matrix_function)):
        if matrix_function[len(matrix_function)-1][x] < column_number:
            column_number = matrix_function[len(matrix_function)-1][x]
            column_pivot = x
    
    for y in range(len(matrix_function)-1):
        if matrix_function[y][len(matrix_function[0])-1] / matrix_function[y][column_pivot] < row_number:
            row_number = matrix_function[y][len(matrix_function[0])-1] / matrix_function[y][column_pivot]
            row_pivot = y
    
    print(row_pivot, column_pivot)
    
    
    
    
    third_window.mainloop()

def secondwindowfunction(first_window, matrix_function):

    # First we need to destroy the first window, we do not need it anymore
    first_window.destroy()

    # All matrix stages
    matrices= []

    # Create a second window
    second_window = Tk()
    second_window.geometry("1500x800")

    # This is only the label
    function_label = Label(second_window, text='Matrix: ')
    function_label.place(x=20, y=10)

    # We print the matrix on the screen
    for i in range(len(matrix_function)):
        for j in range(len(matrix_function[i])):
            function_label = Label(second_window, text=str(matrix_function[i][j]))
            # The position depends on the i position
            function_label.place(x=80*(j+1), y=40*(i+1))

    # Calls the function
    showfunction(matrix_function)

    # Open the image
    img = ImageTk.PhotoImage(Image.open("graph.png"))
    # Saves it on a label
    panel = Label(second_window, image=img)
    # Place it
    panel.place(x=600, y=10)
    # This is necesary to open the window
    
    # The buttton
    button = Button(second_window, text="Next", command=lambda: calculate(second_window, matrices, matrix_function))
    button.place(x=100, y=0)
    second_window.mainloop()


# This is the main function
def firstwindowfunction():
    first_window = Tk()
    first_window.geometry("500x200")

    # Data from the file
    file_variable = []
    # The function variables are store here
    function_array = []
    # The constraints data is store here
    constraints_array = []
    # The identity matrix
    identity = []
    # The matrix use to do all the operations
    matrix_functions = []

    # Open the file directory
    filename = fd.askopenfilename()
    if filename:
        # Open the file
        with open(filename) as file:
            for i in file:
                # Loops the file and append it to the file_variable (file data)
                file_variable.append(i.rstrip())

    # Identity matriz, it is use to complete the process of maximaze
    for i in range(0, len(file_variable)):
        # We create a list with zero
        list = [0]*len(file_variable)
        # Then we add the add in the position to be identity matrix
        list[i] = 1
        # We append it
        identity.append(list)

    # The first position should be the function variables and we split it to save it in an array
    function_array = file_variable[0].split()

    # We loop the file data to store it in the constraints array
    for i in range(1, len(file_variable)):
        constraint = file_variable[i].split()
        constraints_array.append(constraint)

    # Now we have to add the constraints to the function array that we are gonna we to do all the magic
    for i in range(0, len(file_variable)-1):
        # We create a new list, the we append the first two values
        list = []
        list.append(int(constraints_array[i][0]))
        list.append(int(constraints_array[i][1]))

        # We need to loop through the identity matrix because we need to append every item
        for j in identity[i]:
            list.append(int(j))
        list.append(int(constraints_array[i][2]))
        matrix_functions.append(list)

    # Finally we do the same thing with the function list
    list = []
    list.append(-int(function_array[0]))
    list.append(-int(function_array[1]))
    for i in identity[len(identity)-1]:
        list.append(int(i))
    list.append(0)
    matrix_functions.append(list)


    # The labels to be use
    function_label = Label(first_window, text='Function: ' + file_variable[0])
    constraints_label = Label(first_window, text='Constraints: ')
    # The labels position
    function_label.place(x=0, y=0)
    constraints_label.place(x=0, y=20)

    # Prints the constraints on the window
    for i in range(1,len(file_variable)):
        constraints = Label(first_window, text=file_variable[i])
        constraints.place(x=100, y=i*30)

    # The buttton
    button = Button(first_window, text="Next", command=lambda: secondwindowfunction(first_window, matrix_functions))
    button.place(x=100, y=0)

    # This is necesary to open the window
    first_window.mainloop()


firstwindowfunction()
