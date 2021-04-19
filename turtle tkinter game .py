"importing modules"

import turtle
import tkinter

"win is the tab of the controller win geometry is the height and breath of the controler turtl is the "
"thing which is the main part of our game and title is remote controller which will control all the curcer of the thing we draw"
"the screen of the turtle is show as drawing "

win = tkinter.Tk()
win.geometry('300x245')
win.config(bg = "red")
win.resizable(False,False)
turtl = turtle.Turtle()
win.title('Remote Controller')

sc = turtle.Screen()
sc.title("Drawing Pad..")
# sc.bgcolor("yellow")

# it is for welcoming the user

infosolution = '''        WELCOME TO DRAW PAD   
* there are 8 button forward,backward,hidepen,info,left,right,clear and quit
* "forward button" to move front
* "left button" to move left side
* "right" button to move right side
* "hidepen" to hide turtle
* "help" to get help about this game
* "backward"to move backward
* "clear" to clear the lines drawn by the pen 
* "Quit" you should duble click the quit button twice to quit the game
* THESE ARE THE IMPORTANT POINTS OF "DRAW PAD" GAME'''


# this game has a help option if we press that button it will be shown


infosolution1 = '''        HELP :)      
* there are 8 button forward,backward,hidepen,info,left,right,clear and quit
* "forward button" to move front
* "left button" to move left side
* "right" button to move right side
* "hidepen" to hide turtle
* "help" to get help about this game
* "backward"to move backward
* "clear" to clear the lines drawn by the pen 
* "Quit" you should duble click the quit button twice to quit the game
* THESE ARE THE IMPORTANT POINTS OF "DRAW PAD " GAME'''


# "it is all the function of the in def will all the function which is use in the button function in it "

# "it is the function for quiting the game you should duble click the quit button in the tkinter "

def quitingmain_tab():
    win.quit()


# "it is the function of the help function in the win tab"

def welcome ():
    hi = tkinter.Tk()
    hi.title("WELCOME SCREEN")
    hi.geometry("550x250")
    hi.config (bg = "yellow")

    def quiting_welcome_tab():
        win.quit()
        hi.quit()
    hi.resizable(False, False)
    la = tkinter.Button(hi, text="QUIT GAME HEAR",font = "centura 10 ",bg = "black",fg = "white",command=quiting_welcome_tab).pack()
    lab = tkinter.Label(hi, text=infosolution, bg="grey", fg="black", font="lucida 11 bold underline").pack()

welcome()


def infohelp ():
    h = tkinter.Tk()
    h.title("HELP...")
    lab = tkinter.Label(h,text = infosolution1,bg = "black",fg = "white",font = "lucida 11 bold underline").pack()
    h.resizable(False,False)

# "it is the function for leaning all the lines drawn by the turtle in the turtle window "

def clearing ():
    turtl.clear()


# "it is the function used to reset the whole thing and set it has default in the tkinter "

def reset():
    turtl.reset()

# "it is the function used to drawforward when the foerward button is clicked"

def drawforward ():
    turtl.speed(1)
    turtl.forward(30)

# "it is used to turn the pen right "

def drawright ():
    turtl.speed(1)
    turtl.right(10)

# "it is used to turn left when you have clicked the button left"

def drawleft ():
    turtl.speed(1)
    turtl.left(10)

# "it is used to move backward when the backward button is clicked "

def drawbackward ():
    turtl.speed(1)
    turtl.backward(30)

# "it is used to hide the turtle when the hide pen is clicked "

def hide_turtle ():
    turtl.hideturtle()


# "IT IS THE  MAIN PART OF THE BUTTONS IN THE PYTHON TKINTER AND TURTLE GAME"



buttonF = tkinter.Button(win,text = "Forward",width = 10,height = 2,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = drawforward).place(y = 15,x = 20)

buttonB = tkinter.Button(win,text = "Back",width = 10,height = 2,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = drawbackward).place(y = 80,x = 20)

buttonR = tkinter.Button(win,text = "Right",width = 5,height = 1,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = drawright).place(y = 60,x = 240)

buttonL = tkinter.Button(win,text = "Left",width = 5,height = 1,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = drawleft).place(y = 60,x = 180)

buttonQ = tkinter.Button(win,text = "Quit",width = 6,height = 3,bg = "yellow",fg = "black" ,font = "lucida 9 bold underline",command = quitingmain_tab).place(y = 150,x = 238)

buttonC = tkinter.Button(win,text = "Clear",width = 5,height = 3,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = clearing).place(y = 150,x =70)

buttonhidinng = tkinter.Button(win,text = "hide\npen",width = 5,height = 3,bg =  "yellow",fg = "black",font = "lucida 9 bold underline",command = hide_turtle).place(y = 150,x = 15)

buttonreset= tkinter.Button(win,text = "Reset",width = 5,height = 3,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = reset).place(y = 150,x = 185)

buttoninfo= tkinter.Button(win,text = "Help",width = 5,height = 3,bg = "yellow",fg = "black",font = "lucida 9 bold underline",command = infohelp).place(y = 150,x = 130)

"IT IS THE MAIN FUNCTION TO WAIT (RUN AND WAIT)"

turtle.done()

win.mainloop()