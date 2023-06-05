'''#DB
import socket
import time
start=time.time()
s = socket


result = input ('\n DOyou like to continue(y,n):')
if (    .lower)=('y'):
    continue
else:
    break

from tkinter import*
root = Tk()
root.geometry=("700x300")
root.minsize(1000,200)
root.maxsize(1000,300)
root.title("ALish")
a=Label(text="hello ",background="yellow",foreground="red", font="arial 50 italic")
a.pack()
b=Label(text="champion",bg="pink",fg="blue")
b.pack()
root.mainloop()

a = 0

while a<10:

   print('you are learning python')

   pass'''

from tkinter import *
from tkinter import messagebox 
root=Tk()
def exitwc():
    root.destroy()
def wc():
    messagebox.showinfo("hello","welcome to Nepal")
root.geometry("600x400")
Button(text="on").pack()
Button(text="off" ,command=exitwc).pack(anchor="center")
Button(root,text="welcome",command=wc).pack()
root.mainloop()