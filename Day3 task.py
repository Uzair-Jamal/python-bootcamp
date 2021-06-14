from tkinter import *
import tkinter as tk
window = Tk()

window.title("Registration Screen")
window.geometry('800x800')
window.configure(background = "blue");

Label(window ,text = "Registration Form",font=("bold", 18)).grid(row = 0,column = 2)

Firstname = Label(window ,text = "First Name ").grid(row = 1,column = 0)
LastName = Label(window ,text = "Last Name " ).grid(row = 2,column = 0)
Email = Label(window ,text = "Email Id ").grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number ").grid(row = 4,column = 0)
Employeename = Label(window, text = "Employee Name").grid(row = 5,column = 0)
Employeeid = Label(window, text = "Employee ID").grid(row = 6,column = 0)
Landline = Label(window, text = "Landline").grid(row = 7,column = 0)
Address = Label(window, text = "Address").grid(row = 8,column = 0)
Postalcode = Label(window, text = "Postal Code").grid(row = 9,column = 0)
Nationality = Label(window, text = "Nationality").grid(row = 10,column = 0)


Firstname1 = Entry(window).grid(row = 1,column = 1)
Lastname1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 4,column = 1)
Employeename1 = Entry(window).grid(row = 5,column = 1)
Employeeid1 = Entry(window).grid(row = 6,column = 1)
Landline1 = Entry(window).grid(row = 7,column = 1)
Address1 = Entry(window).grid(row = 8,column = 1)
Postalcode1 = Entry(window).grid(row = 9,column = 1)
Nationality1 = Entry(window).grid(row = 10,column = 1)

var1 = IntVar()
var2 = IntVar()

"""
Radiobutton(window, text= "Male", variable=var1, value=1 ).grid(row=10,coulumn = 1)
Radiobutton(window, text= "Female", variable=var1, value=2).grid(row=11,coulumn = 2)
"""

Checkbutton(window,text= "Male", variable=var1).grid(row = 12)
Checkbutton(window,text= "Female", variable=var2).grid(row = 13)

Birthday_Months=['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','December']
b=StringVar()
dropdown = OptionMenu(window,b,*Birthday_Months)
dropdown.config(width=20)
b.set('Select Month')
dropdown.grid(row = 12,column = 1)




def clicked():
    res = "Welcome to " + text.get()
    lbl.configure(text= res)
btn = tk.Button(window ,text="Submit").grid(row=15,column=1)

window.mainloop()
