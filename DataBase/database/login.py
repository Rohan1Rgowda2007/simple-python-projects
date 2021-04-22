
# importing the tkinter module
import tkinter

mainWin = tkinter.Tk()
mainWin.resizable(False,False)

# using the rgb for the background color
def from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

mainWin.geometry("300x200")
mainWin.config(bg = from_rgb((49, 117, 181)))

# creating the name of the login screen as face book as an example
lab = tkinter.Label(mainWin,text = "face book",font = "lucida 18 bold",bg = from_rgb((49, 117,181)),foreground = "white")
lab.pack()
lab.place(x = 90,y = 15)

# it is the text for the user name for login screen
userName = tkinter.Label(mainWin,text = "User Name",font ="Candara 15 bold",bg = from_rgb((49, 117,181)),foreground = "white")
userName.pack()
userName.place(x = 15,y = 60)

# it is the text for username entry
userEntry = tkinter.Entry(mainWin,width = 27)
userEntry.pack()
userEntry.place(x = 120 , y = 66)

# entry text for passward entry
passwardEntry = tkinter.Entry(mainWin,width = 27,show = '*')
passwardEntry.pack()
passwardEntry.place(x = 120 , y = 100)

# it will work as letter in the login screen
Passcode = tkinter.Label(mainWin,text = "Passward",font ="Candara 15 bold",bg = from_rgb((49, 117,181)),foreground = "white",)
Passcode.pack()
Passcode.place(x = 15,y = 90)

# creating a class for error button
class Win:
    def __init__(self,title):
        tk = tkinter.Tk()
        tk.title(title)
        tk.resizable(False,False)
        # tk.geometry("400x200")
        lable = tkinter.Label(tk,text =f"YOU MUST ENTER MORE THAN 8 CHARACTERS \n BUT YOU HAVE ENTERED {len(passwardEntry.get())}",font = "lucida 13 bold")
        lable.pack()
        tk.mainloop()

# it is the command for the login button and it will store the data in the data.txt file(database)
def data_base():
    if len(passwardEntry.get()) < 8:
        error = Win("in valid passward")
    else:
        data = open("data.txt","a")
        data.write(f"User Name : {userEntry.get()}  \n")
        data.write(f'Passward : {passwardEntry.get()}  \n\n\n')
        data.close()
        print("Welcome to 'Face Book'")
        mainWin.quit()

# login button
loginBtn = tkinter.Button(mainWin,text = "login",font = "lucida 12 bold",bg = from_rgb((49, 117,181)),foreground = "white",command = data_base)
loginBtn.pack()
loginBtn.place(x = 120,y = 150)

# it will use as run and wait
mainWin.mainloop()