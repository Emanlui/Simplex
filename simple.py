from tkinter import *
from tkinter import filedialog as fd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import sys
from fractions import Fraction
import copy

# This function does everything with the graphing
def show3Dfunction(functions):
    return functions

# This function does everything with the graphing
def show2Dfunction(functions):
    # This gets the max point to show the linear function
    max_number = 0
    length_of_matrix = len(functions)
    for i in functions:
        max_number = max(i[len(i) - 1], max_number)

    # Adds the range of the X dimension
    x = np.array(range(0, max_number))

    array_of_functions = []

    # Adds the linear function to the graph
    for i in range(length_of_matrix - 1):
        y = eval("(" + str(functions[i][-1]) + "-" + str(functions[i][0]) + "*x)/" + str(functions[i][1]))
        plt.plot(x, y)
        array_of_functions.append(y)
    # Saves the image, this is necesary because we need to open it later
    plt.grid()
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('The graph of the constraints')

    plt.fill(5, 5, "b")

    # Adds the linear function to the graph
    for i in range(length_of_matrix - 1):
        y = eval("(" + str(functions[i][-1]) + "-" + str(functions[i][0]) + "*x)/" + str(functions[i][1]))
        plt.plot(x, y)
        array_of_functions.append(y)
    # Saves the image, this is necesary because we need to open it later
    plt.grid()
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('The graph of the constraints')

    for i in range(0, len(array_of_functions)):
        for j in range(0, len(array_of_functions)):
            if i != j:
                plt.fill_between(x, array_of_functions[i], array_of_functions[j],
                                 where=((array_of_functions[i] >= 0) & (array_of_functions[j] >= 0)), facecolor='blue',
                                 alpha=0.5)
    plt.savefig('graph.png')
    return plt


def calculatepivots(matrix_function):

    column_pivot = 0
    column_number = 0
    row_pivot = 0
    row_number = sys.maxsize

    # Travel alonmg the matrix to find the lowest column number
    for x in range(len(matrix_function[len(matrix_function)-1])):
        if matrix_function[len(matrix_function) - 1][x] < column_number:
            column_number = matrix_function[len(matrix_function) - 1][x]
            column_pivot = x

    for y in range(len(matrix_function) - 1):

        # Verify that the divisor is greater than zero
        if matrix_function[y][column_pivot] == 0 :
            continue

        # Travel alonmg the matrix to find the lowest row number
        elif matrix_function[y][len(matrix_function[0]) - 1] / matrix_function[y][column_pivot] < row_number:
        
            if matrix_function[y][len(matrix_function[0]) - 1] / matrix_function[y][column_pivot] > 0:
                row_number = matrix_function[y][len(matrix_function[0]) - 1] / matrix_function[y][column_pivot]
                row_pivot = y
            
            else:
                continue

    # Return the position of the pivot.
    res = [row_pivot, column_pivot]
    return res

def hasnegatives(matrix_function):
    # Function to verify if are negatives left on the matrix.
    for x in range(len(matrix_function[0]) - 1):
        if matrix_function[len(matrix_function) - 1][x] < 0:
            return True

    return False

def imp(matriz):
    
    print('\n')
    for x in range(len(matriz)):
        print(matriz[x])

def errorfunction(msj):
    
    error_window = Tk()
    error_window.geometry("500x200")
    
    function_label = Label(error_window, text="ATENCION: ")
    function_label.place(x=80, y=20)
    
    function_label = Label(error_window, text=msj)
    function_label.place(x=80, y=50)
    
    # This is necesary to open the window
    error_window.mainloop()

def makechanges(matrix_function, matrices, changes):

    # Function to modifiy the matrix after the pivot is found.
    tmp_changes = []

    pivots = calculatepivots(matrix_function)
    pivot_number = matrix_function[pivots[0]][pivots[1]]

    #print(pivot_number, pivots)
    #imp(matrix_function)

    flag = False
    
    for x in range(len(matrix_function)):
        if matrix_function[x][pivots[1]] > 0:
            flag = True

    if flag == False:
        errorfunction("Solucion no encontrada")

    string = '1/' + str(pivot_number) + ' en toda la fila ' + str(pivots[0] + 1) + '.'
    tmp_changes.append(string)

    # Changes the column pivot.
    for x in range(len(matrix_function[0])):
        matrix_function[pivots[0]][x] = matrix_function[pivots[0]][x] / pivot_number

    # Changes all the rows left on the matrix.
    for x in range(len(matrix_function)):

        if x == pivots[0]:
            continue

        tmp_number = matrix_function[x][pivots[1]]
        string = 'Fila ' + str(pivots[0] + 1) + ' multiplicado por ' + str(-tmp_number) + ' sumado a la fila ' + str(
            x + 1) + '.'
        tmp_changes.append(string)

        for y in range(len(matrix_function[0])):
            matrix_function[x][y] = matrix_function[x][y] + (-tmp_number * matrix_function[pivots[0]][y])

    changes.append(tmp_changes)


def destroywindow(third_window, matrices, changes, plt, matrix_function):
    third_window.destroy()
    thirdwindowfunction(matrices, changes, plt, matrix_function)


def thirdwindowfunction(matrices, changes, plt, matrix_function):
    # Create a third window.
    third_window = Tk()

    third_window.update_idletasks()

    width = third_window.winfo_width()
    height = third_window.winfo_height()

    x = (third_window.winfo_screenwidth() // 2) - (width // 2)
    y = (third_window.winfo_screenheight() // 2) - (height // 2)

    third_window.geometry('{}x{}+{}+{}'.format(width + 800, height + 800, x - 300, y - 300))
    if matrices == []:
        
        for i in range(len(matrix_function)):

            function_label = Label(third_window, text="X"+str(i))
            function_label.place(x=300, y=50*(i+1))

            if matrix_function[i][len(matrix_function[0])-1] < 0:
                function_label = Label(third_window, text="0")
                function_label.place(x=400, y=50*(i+1))
            else:
                function_label = Label(third_window, text=str(Fraction(matrix_function[i][len(matrix_function[0])-1]).limit_denominator()))
                function_label.place(x=400, y=50 * (i + 1))

    else:

        # This is only the label
        function_label = Label(third_window, text='Matrix: ')
        function_label.place(x=20, y=10)

        function_label = Label(third_window, text="X")
        function_label.place(x=80, y=20)

        function_label = Label(third_window, text="Y")
        function_label.place(x=80 * 2, y=20)

        for i in range(2, len(matrix_function[0])-1):
            function_label = Label(third_window, text="Z" + str(i - 1))
            function_label.place(x=80 * (i + 1), y=20)
            if(i+1 == len(matrix_function[0])-1):
                function_label = Label(third_window, text="Result")
                function_label.place(x=80 * (i + 2), y=20)

        # We print the matrix on the screen
        for i in range(len(matrices[0])):
            for j in range(len((matrices[0])[i])):
                function_label = Label(third_window, text=str(Fraction((matrices[0])[i][j]).limit_denominator()))
                # The position depends on the i position
                function_label.place(x=80 * (j + 1), y=40 * (i + 1))

        for x in range(len(changes[0])):
            function_label = Label(third_window, text=str(changes[0][x]))
            # The position depends on the i position
            function_label.place(x=120, y=100 * (x + 2))

        # The buttton
        button = Button(third_window, text="Next",
                        command=lambda: destroywindow(third_window, matrices[1:], changes[1:], plt, matrix_function))
        button.place(x=700, y=300)

        third_window.mainloop()


def calculate(second_window, matrices, changes, matrix_function, plt):
    second_window.destroy()

    var = hasnegatives(matrix_function)

    while var:
        matrix_tmp = copy.deepcopy(matrix_function)
        matrices.append(matrix_tmp)
        makechanges(matrix_function, matrices, changes)
        var = hasnegatives(matrix_function)

    matrix_tmp = copy.deepcopy(matrix_function)
    matrices.append(matrix_tmp)

    thirdwindowfunction(matrices, changes, plt, matrix_function)


def secondwindowfunction(first_window, matrix_function,dim):
    # First we need to destroy the first window, we do not need it anymore
    first_window.destroy()

    # All matrix stages
    matrices = []

    # All changes
    changes = []
    changes.append(["Matriz incial"])

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
            function_label.place(x=80 * (j + 1), y=40 * (i + 1))

    plt = []
    # Calls the function
    if dim-1 == 2:
        plt = show2Dfunction(matrix_function)

        # Open the image
        img = ImageTk.PhotoImage(Image.open("graph.png"))
        # Saves it on a label
        panel = Label(second_window, image=img)
        # Place it
        panel.place(x=80, y=250)
        # This is necesary to open the window


    elif dim-1 == 3:
        plt = show3Dfunction(matrix_function)

        # Open the image
        img = ImageTk.PhotoImage(Image.open("graph.png"))
        # Saves it on a label
        panel = Label(second_window, image=img)
        # Place it
        panel.place(x=80, y=250)
        # This is necesary to open the window

    # The buttton
    button = Button(second_window, text="Next", command=lambda: calculate(
        second_window, matrices, changes, matrix_function, plt))

    button.place(x=800, y=450)
    second_window.mainloop()


# This is the main function
def firstwindowfunction():
    first_window = Tk()
    first_window.geometry("500x200")

    # Data from the file
    file_function = []

    # The file with ints
    file_function_int = []

    # Open the file directory
    filename = fd.askopenfilename()
    if filename:
        # Open the file
        with open(filename) as file:
            for i in file:
                # Loops the file and append it to the file_variable (file data)
                file_function.append(i.rstrip())

    for i in file_function:
        a = i.split()
        new_list = []
        for j in a:
            new_list.append(int(j))
        file_function_int.append(new_list)

    dim = 0

    for i in file_function_int[len(file_function_int) - 1]:

        if i != 0:
            dim = dim + 1

    secondwindowfunction(first_window, file_function_int,dim)

    # This is necesary to open the window
    first_window.mainloop()


firstwindowfunction()
