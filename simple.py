from tkinter import *
from tkinter import filedialog as fd
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import sys
from fractions import Fraction 
import copy 

# This function does everything with the graphing
def showfunction(functions):

    # This gets the max point to show the linear function
    max_number = 0
    length_of_matrix = len(functions)
    for i in functions:
        max_number = max(i[len(i)-1],max_number)

    # Adds the range of the X dimension
    x = np.array(range(0, max_number))

    array_of_functions = []

    # Adds the linear function to the graph
    for i in range(length_of_matrix-1):
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


def calculatepivots(matrix_function):
    
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
    
    res = [row_pivot, column_pivot]
    return res

def hasnegatives(matrix_function):
    
    for x in range(len(matrix_function[0])-1):
        if matrix_function[len(matrix_function)-1][x] < 0:
            return True    
    
    return False

def makechanges(matrix_function, matrices, changes):
    
    tmp_changes = []
       
    #primera linea 
    pivots = calculatepivots(matrix_function)
    pivot_number = matrix_function[pivots[0]][pivots[1]]

    string = '1/' + str(pivot_number) + ' en toda la fila ' + str(pivots[0]+1) + '.'
    tmp_changes.append(string)
    
    for x in range(len(matrix_function[0])):
        matrix_function[pivots[0]][x] = matrix_function[pivots[0]][x] / pivot_number
        
    #segunda linea
    
    for x in range(len(matrix_function)):
        
        if x == pivots[0]:
            continue

        tmp_number = matrix_function[x][pivots[1]]
        string = 'Fila ' + str(pivots[0]+1) + ' multiplicado por ' + str(-tmp_number) + ' sumado a la fila ' + str(x+1) + '.'
        tmp_changes.append(string)
        
        for y in range(len(matrix_function[0])):
            
            matrix_function[x][y] = matrix_function[x][y] + (-tmp_number * matrix_function[pivots[0]][y])
    
    changes.append(tmp_changes)

def thirdwindowfunction(third_window, matrices, changes):
    
    if matrices == []:
        function_label = Label(third_window, text='FIN.')
        function_label.place(x=700, y=350)
    
    else:
    
        # This is only the label
        function_label = Label(third_window, text='Matrix: ')
        function_label.place(x=20, y=10)

        function_label = Label(third_window, text="X")
        function_label.place(x=80, y=20)

        function_label = Label(third_window, text="Y")
        function_label.place(x=80*2, y=20)

        for i in range(2,len(matrices[0])+2):
            function_label = Label(third_window, text="Z" + str(i-1))
            function_label.place(x=80 * (i+1), y=20)

        function_label = Label(third_window, text="Result")
        function_label.place(x=80 * (len(matrices[0])+3), y=20)

        # We print the matrix on the screen
        for i in range(len(matrices[0])):
            for j in range(len((matrices[0])[i])):
                function_label = Label(third_window, text=str(Fraction((matrices[0])[i][j]).limit_denominator()))
                # The position depends on the i position
                function_label.place(x=80*(j+1), y=40*(i+1))
        
        for x in range(len(changes[0])):
            function_label = Label(third_window, text=str(changes[0][x]))
            # The position depends on the i position
            function_label.place(x=120, y=100*(x+2))
    
        # The buttton
        button = Button(third_window, text="Next", command=lambda: thirdwindowfunction(third_window, matrices[1:], changes[1:]))
        button.place(x=700, y=300)

        third_window.mainloop()
    
def calculate(second_window, matrices, changes, matrix_function):

    second_window.destroy()
    
    # Create a second window
    third_window = Tk()
    third_window.geometry("900x600")

    var = hasnegatives(matrix_function)

    while var:

        matrix_tmp = copy.deepcopy(matrix_function)
        matrices.append(matrix_tmp)
        makechanges(matrix_function, matrices, changes)
        var = hasnegatives(matrix_function)
    
    matrix_tmp = copy.deepcopy(matrix_function)
    matrices.append(matrix_tmp)
    
    thirdwindowfunction(third_window, matrices, changes)
    

def secondwindowfunction(first_window, matrix_function):

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

    function_label = Label(second_window, text="X")
    function_label.place(x=80, y=20)

    function_label = Label(second_window, text="Y")
    function_label.place(x=80*2, y=20)

    for i in range(2,len(matrix_function)+2):
        function_label = Label(second_window, text="Z" + str(i-1))
        function_label.place(x=80 * (i+1), y=20)

    function_label = Label(second_window, text="Result")
    function_label.place(x=80 * (len(matrix_function)+3), y=20)

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
    panel.place(x=80, y=250)
    # This is necesary to open the window
    
    # The buttton
    button = Button(second_window, text="Next", command=lambda: calculate(second_window, matrices, changes, matrix_function))
    button.place(x=800, y=450)
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
