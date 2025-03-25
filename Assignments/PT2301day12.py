# # flask, exception handling, tkinter
# from pywin.framework.interact import valueFormatOutputError
#
# try:
#     a = 5
#     b = 0
#     print(a / b)
#     a1 = 1
#     b1 = 's'
#     print(a1 + b1)
#
#
#
# except TypeError:
#     print("Verror")
# except ZeroDivisionError:
#     print("Zerror")
#
#
# else:
#     print("over")
# finally:
#     print("finally block")
# class errrro(Exception):
#     pass
#
# a=3
# b=5
# try:
#     if a > b:
#         print("a")
#     else:
#         print("entered")
#         raise errrro("eoccured")
# except:
#     print("ook")

import tkinter
from tkinter.ttk import Radiobutton,Button


window=tkinter.Tk()

Radiobutton(window, value='python',text='python').grid(row=0, column=1)
Button(window,text='java').grid(row=1,column=1)
window.mainloop()


