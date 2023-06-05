'''from tkinter import *

def getdata():
    print("First name is :%s"%(fname.get()))
    print("last name is :%s"%(lname.get()))
root=Tk()
root.geometry("700x400")
Label(text="FIRST NAME:",font="comissansms 20 bold italic").grid(row=0,column=0)
Label(text="LAST NAME: ",font="comissansms 20 bold italic").grid(row=1,column=0)

#Variable: StringVar,IntVar,DoubleVar,BollenVar
fname=StringVar()
lname=StringVar()
Entry(root,textvariable=fname).grid(row=0,column=1)
Entry(root,textvariable=lname).grid(row=1,column=1)

Label (text="Hobbies: ",font="comicsansms 20 bold").grid(row=2,column=0)
Checkbutton(text="playing").grid(row=2,column=1)
Checkbutton(text="eating").grid(row=2,column=2)
Checkbutton(text="football").grid(row=2,column=3)

var=IntVar()
Label(text="gender: ",font="arial 20 bold ",bg="gray").grid(row=3,column=0)
Radiobutton(text="Male",variable=var,value=1).grid(row=3,column=1)
Radiobutton(text="Female",variable=var,value=2).grid(row=3,column=2)
Radiobutton(text="others",variable=var,value=3).grid(row=3,column=3)

Button(text="submit",command=getdata).grid(row=4,column=0)
Button(text="quit",command=exit).grid (row=4,column=2)

root.mainloop()
'''
'''
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font

def submit_order():
    first_name = entry_first_name.get()
    middle_name = entry_middle_name.get()
    last_name = entry_last_name.get() 
    gender = entry_gender.get()
    order_item = entry_order_item.get()
    total_amount = entry_total_amount.get()
    contact = entry_contact.get()
    email = entry_email.get()
    address = entry_address.get()
    delivered_date = entry_delivered_date.get()
    received_date = entry_received_date.get()

    messagebox.showinfo("Order Confirmation", f"Order details:\n\n"
                        f"Name: {first_name} {middle_name} {last_name}\n"
                        f"Gender: {gender}\n"
                        f"Order Item: {order_item}\n"
                        f"Total Amount: {total_amount}\n"
                        f"Contact: {contact}\n"
                        f"Email: {email}\n"
                        f"Address: {address}\n"
                        f"Delivered Date: {delivered_date}\n"
                        f"Received Date: {received_date}")

    entry_first_name.delete(0, tk.END)
    entry_middle_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_order_item.delete(0, tk.END)
    entry_total_amount.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_delivered_date.delete(0, tk.END)
    entry_received_date.delete(0, tk.END)

window = tk.Tk()
window.title("Online Order Form")

label_font = Font(family="Helvetica", size=12, weight="bold")
entry_font = Font(family="Helvetica", size=12)

label_first_name = tk.Label(window, text="First Name:", font=label_font)
label_first_name.pack()
entry_first_name = tk.Entry(window, font=entry_font)
entry_first_name.pack()

label_middle_name = tk.Label(window, text="Middle Name:", font=label_font)
label_middle_name.pack()
entry_middle_name = tk.Entry(window, font=entry_font)
entry_middle_name.pack()

label_last_name = tk.Label(window, text="Last Name:", font=label_font)
label_last_name.pack()
entry_last_name = tk.Entry(window, font=entry_font)
entry_last_name.pack()

label_gender = tk.Label(window, text="Gender:", font=label_font)
label_gender.pack()
entry_gender = tk.Entry(window, font=entry_font)
entry_gender.pack()

label_order_item = tk.Label(window, text="Order Item:", font=label_font)
label_order_item.pack()
entry_order_item = tk.Entry(window, font=entry_font)
entry_order_item.pack()

label_total_amount = tk.Label(window, text="Total Amount:", font=label_font)
label_total_amount.pack()
entry_total_amount = tk.Entry(window, font=entry_font)
entry_total_amount.pack()

label_contact = tk.Label(window, text="Contact:", font=label_font)
label_contact.pack()
entry_contact = tk.Entry(window, font=entry_font)
entry_contact.pack()

label_email = tk.Label(window, text="Email Address:", font=label_font)
label_email.pack()
entry_email = tk.Entry(window, font=entry_font)
entry_email.pack()

label_address = tk.Label(window, text="Receiving Address:", font=label_font)
label_address.pack()
entry_address = tk.Entry(window, font=entry_font)
entry_address.pack()

label_delivered_date = tk.Label(window, text="Delivered Date:", font=label_font)
label_delivered_date.pack()
entry_delivered_date = tk.Entry(window, font=entry_font)
entry_delivered_date.pack()

label_received_date = tk.Label(window, text="Received Date:", font=label_font)
label_received_date.pack()
entry_received_date = tk.Entry(window, font=entry_font)
entry_received_date.pack()

submit_button = tk.Button(window, text="Submit Order", command=submit_order, font=label_font, bg="green", fg="white")
submit_button.pack()

window.mainloop()
'''
from tkinter import *

root=Tk()
root.minsize(700,500)
root.title("Online Order Form")

#Labels

Label(text="ONLINE ORDER FORM", font=("Sans Serif", 16, "bold")).grid(row=0, column=1)
Label(text="First Name: ", font=("Sans Serif", 12)).grid(row=1, column=0)
Label(text="Middle Name: ", font=("Sans Serif", 12)).grid(row=2, column=0)
Label(text="Last Name: ", font=("Sans Serif", 12)).grid(row=3, column=0)
Label(text="First Name: ", font=("Sans Serif", 12)).grid(row=4, column=0)
Label(text="Gender: ", font=("Sans Serif", 12)).grid(row=5, column=0)
Label(text="Order Item: ", font=("Sans Serif", 12)).grid(row=6, column=0)
Label(text="Total Amount: ", font=("Sans Serif", 12)).grid(row=7, column=0)
Label(text="Contact number: ", font=("Sans Serif", 12)).grid(row=8, column=0)
Label(text="Email Address: ", font=("Sans Serif", 12)).grid(row=9, column=0)
Label(text="Receiving Address: ", font=("Sans Serif", 12)).grid(row=10, column=0)
Label(text="Delivery Date: ", font=("Sans Serif", 12)).grid(row=11, column=0)
Label(text="Received Date: ", font=("Sans Serif", 12)).grid(row=12, column=0)

#Entry Buttons
Entry(root).grid(row=1, column=1)
Entry(root).grid(row=2, column=1)
Entry(root).grid(row=3, column=1)
Entry(root).grid(row=4, column=1)
Entry(root).grid(row=6, column=1)
Entry(root).grid(row=7, column=1)
Entry(root).grid(row=8, column=1)
Entry(root).grid(row=9, column=1)
Entry(root).grid(row=10, column=1)
Entry(root).grid(row=11, column=1)
Entry(root).grid(row=12, column=1)


#Radio Button
war=IntVar()
Radiobutton(text="Male", variable=war, value=1).grid(row=5, column=1)
Radiobutton(text="Female", variable=war, value=2).grid(row=5, column=2)
Radiobutton(text="Others", variable=war, value=3).grid(row=5, column=3)

Button(text="submit").grid(row=13,column=1)
Button(text="quit",command=exit).grid (row=13,column=2)


root.mainloop()