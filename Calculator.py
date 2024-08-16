from tkinter import *

#Create the main window

root = Tk()

root.title("My Calculator")

root.configure(bg="#BBDEFB") #Set background color

# Create entry field for user input

user_input = Entry(root, width=20, font=('Arial', 18), borderwidth=5)

user_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10) #ipady adds internal padding vertic

#Function to update the entry field 

def add_to_input(number): 
    current = user_input.get() 
    user_input.delete(0, END)
    user_input.insert(0, current + str(number))

#Function to clear the entry field 

def clear_input():
    user_input.delete(0, END)

#Function to perform calculations 

def do_math(): 
    try:
        calculation = user_input.get() 
        result = eval(calculation)
        user_input.delete(0,END)
        user_input.insert(0,result)
    except:
        user_input.delete(0,END)
        user_input.insert(0,"Invalid Division")
        

#Button configuration for a casual Look

button_style= {
    'font' : ('Arial', 14),
    'bg' : '#000000',#Black
    'fg' : 'white',
    'padx' : 30,
    'pady' : 20,
    'borderwidth': 2,
    'relief':'raised' # Border style
}

# Button Layout in a grid

buttons = [("7", "8","9", "/"),("4", "5", "6", "*"),("1","2","3","4"),("0", "Clear", "=", "+")]


#Create buttons in a grid Layout 

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text =="Clear":
            button = Button(root, text=text, command=clear_input, **button_style)

        elif text == "=":
            button = Button(root, text=text, command=do_math, bg='#000000', fg='white', padx= 89, pady=20, font=('Arial',14))
        else:
            button =Button(root, text=text, command=lambda t=text: add_to_input(t), **button_style)
        button.grid(row=i+1, column=j, padx=5, pady=5)

#Start the GUI

root.mainloop()
