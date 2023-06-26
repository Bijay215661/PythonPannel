import tkinter

win = tkinter.Tk()
win.geometry("500x300")
win.configure(bg ="")

def getvals():
    print("Accepted")
#this is it
tkinter.Label(win,text = "Python Registration form", font = "ar 15 bold").grid(row=0, column=3)
name = tkinter.Label(win, text ="Name")
lastName = tkinter.Label(win, text ="Last_Name")
gender = tkinter.Label(win, text ="Gender")
phoneNo = tkinter.Label(win, text ="Phone_Number")
Email = tkinter.Label(win, text ="Email")

name.grid(row=1, column=2)
lastName.grid(row=2, column=2)
gender.grid(row=3, column=2)
phoneNo.grid(row=4, column=2)
Email.grid(row=5, column=2)

namevalue = ""
lastNamevalue = ""
gendervalue = ""
phoneNovalue = ""
Emailvalue = ""
checkvalue =int

nameentry = tkinter.Entry(win, textvariable=namevalue)
lastNameentry = tkinter.Entry(win, textvariable= lastNamevalue)
genderentry = tkinter.Entry(win, textvariable= gendervalue)
phoneNoentry = tkinter.Entry(win, textvariable= phoneNovalue)
Emailentry = tkinter.Entry(win, textvariable=Emailvalue )

nameentry.grid(row=1, column=3)
lastNameentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
phoneNoentry.grid(row=4, column=3)
Emailentry.grid(row=5, column=3)

checkbtn = tkinter.Checkbutton(text ="Remember me", variable=checkvalue)
checkbtn.grid(row = 6, column=3)

tkinter.Button(text = "Submit", command=getvals).grid(row=7, column=3 )





win.mainloop()