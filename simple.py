from tkinter import *
from tkinter import filedialog as fd


# This function let us to check if a string is an integer
def isint(integer):
    try:
        int(integer)
        return True
    except ValueError:
        return False

def secondwindowfunction(first_window, function, constraints):
    first_window.destroy()
    
    second_window = Tk()
    second_window.geometry("500x200")
    

# This is the main function
def firstwindowfunction():
    first_window = Tk()
    first_window.geometry("500x200")


    # Array of variables

    # Data from the file
    file_variable = []
    # The function variables are store here
    function_array = []
    # The constraints data is store here
    constraints_array = []

    # Open the file directory
    filename = fd.askopenfilename()
    if filename:
        # Open the file
        with open(filename) as file:
            for i in file:
                # Loops the file and append it to the file_variable (file data)
                file_variable.append(i.rstrip())
    # The first position should be the function variables and we split it to save it in an array
    function_array = file_variable[0].split()
    
    # We loop the file data to store it in the constraints array
    for i in range(1,len(file_variable)):
        constraint = file_variable[i].split()
        constraints_array.append(constraint)

    
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
        print(file_variable[i])

    # The buttton
    button = Button(first_window, text="Next", command=lambda: secondwindowfunction(first_window, function_array, constraints_array))
    button.place(x=100, y=0)

    # This is necesary to open the window
    first_window.mainloop()


firstwindowfunction()
