from tkinter import *


win = Tk()

entryUN = Entry(win,width = '30')
entryUN.pack(pady = 70,padx = 40)
entryUN.place(y = 43, x = 95)
# entry.insert(0,'pythonprogramer@python3.9.1.com')

win.title('Login to python :)')
win.geometry('300x156')
win.config(bg = 'black')

lab1 = Label(win,text = f'User Name |',bg = 'black',fg = 'white',font = 'PoorRichard 10')
lab1.pack()
lab1.place(y = 40,x= 10)

lab2 = Label(win,text = 'passcode    |',bg = 'black',fg = 'white',font = 'PoorRichard 10')
lab2.pack()
lab2.place(y = 70,x = 8)

lab3 = Label(win,text = 'Login',font = 'lucida 15 bold',bg = 'black',fg = 'white')
lab3.pack()

def printing(event):
    print(f"User Name is '{entryUN.get()}'")
    print(f"Your Passward is '{entryP.get()}'")
    print('\n\tthanks to login in :)')

def printingclick():
    print(f"User Name is '{entryUN.get()}'")
    print(f"Your Passward is '{entryP.get()}'")
    print('\n\tthanks to login in :)')

entryP = Entry(win,width = 30,show = '*')
entryP.pack()
entryP.place(y = 70,x = 95)

loginbutton = Button(win,text = 'login',height = 1 , width = 4,command = printingclick)
loginbutton.bind('<Return>',printing)
loginbutton.focus()
loginbutton.pack(expand  = True)
loginbutton.place(y = 110,x = 140)

win.resizable(False,False)
win.mainloop()