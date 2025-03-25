"""from tkinter import Tk, Label, Button
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()
        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    def greet(self):
        print("Greetings!")
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop() """

"""from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
mainloop()"""

"""from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()"""

"""from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()"""

"""from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()"""

"""from tkinter import *
root = Tk()
w = Label(root, text='I am lable this is my place!')
w.pack()
root.mainloop()
"""
#Listbox
"""from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(4, 'Python')
Lb.insert(3, 'Java')
Lb.insert(1, 'C++')
Lb.insert(2, 'Any other')
Lb.pack()
top.mainloop()"""

"""from tkinter import *
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainloop()"""

"""from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='yellow')
messageVar.pack( )
main.mainloop( )"""

"""from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
mainloop()"""


"""from tkinter import *
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
    mylist.insert(END, 'This is line number' + str(line))
mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )
mainloop()"""

"""from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'I am writing\nsomething\n')
mainloop()"""

"""from tkinter import *
master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()"""

"""import tkinter
# Creating the GUI window.
root = tkinter.Tk()
root.title("Welcome to GeekForGeeks")
#this is not'*' but 'x'
root.geometry("10x10")
# Creating our text widget.
sample_text = tkinter.Text( root, height = 10)
sample_text.pack()
# Creating a tuple containing
# the specifications of the font.
Font_tuple = ("Comic Sans MS", 20, "bold")
# Parsed the specifications to the
# Text widget using .configure( ) method.
sample_text.configure(font = Font_tuple)
root.mainloop()"""

"""import tkinter.font
# Creating the GUI window.
root = tkinter.Tk()
root.title("Welcome to GeekForGeeks")
root.geometry("918x450")
# Creating our text widget.
sample_text=tkinter.Text( root, height = 10)
sample_text.pack()
# Create an object of type Font from tkinter.
Desired_font = tkinter.font.Font( family = "Comic Sans MS",
                                  size = 20,
                                  weight = "bold")
# Parsed the Font object
# to the Text widget using .configure( ) method.
sample_text.configure(font = Desired_font)
root.mainloop()"""

"""from tkinter import *
class Table:
    def __init__(self,root):
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
# create root window
root = Tk()
t = Table(root)
root.mainloop()"""

"""from tkinter import *
master = Tk()
pane = Frame(master)
pane.pack(fill = BOTH, expand = True)
b1 = Button(pane, text = "Click me !",
            background = "red", fg = "white")
b1.pack(side = TOP, expand = True, fill = BOTH)
b2 = Button(pane, text = "Click me too",
            background = "blue", fg = "white")
b2.pack(side = TOP, expand = True, fill = BOTH)
b3 = Button(pane, text = "I'm also button",
            background = "green", fg = "white")
b3.pack(side = TOP, expand = True, fill = BOTH)
master.mainloop()"""

"""from tkinter import *
class GFG:
    def __init__(self, master = None):
        self.master = master
        # Calls create method of class GFG
        self.create()
    def create(self):
        self.canvas = Canvas(self.master)
        # This creates a line of length 200 (straight horizontal line)
        #position wrt x and y axises,length and width
        self.canvas.create_line(250, 55, 200, 25)
        # This creates a lines of 300 (straight vertical dashed line)
        self.canvas.create_line(300, 35, 300, 200, dash = (5, 2))
        # This creates a triangle (triangle can be created by other methods also)
        self.canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        self.canvas.pack(fill = BOTH, expand = True)
if __name__ == "__main__":
    master = Tk()
    geeks = GFG(master)
    master.title("Lines")
    # This sets the geometry and position of window
    # on the screen
    master.geometry("400x250")
    master.mainloop()"""

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0
        self.total_label_text.set(self.total)
        self.entry.delete(0, END)
root = Tk()
my_gui = Calculator(root)
root.mainloop()