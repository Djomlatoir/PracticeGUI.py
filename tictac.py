from tkinter import *
from tkinter import messagebox
from subprocess import call
def open_mainpy_file():
    window.destroy()
    call(["python", "main.py"])

#x starts = true
clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

#see if someone won
def checkifwon():
    global  winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b1["text"] == "X" and b3["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b3.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X won!")
        disable_all_buttons()
        reset()
      #O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b1["text"] == "O" and b3["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b3.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O won!")
        disable_all_buttons()
        reset()
    if count == 9 and winner == False:
        messagebox.showinfo("Tick Tack Toe", "Draw")
        disable_all_buttons()
        reset()




def b_click(b):
   global clicked, count
   if b["text"] == " " and clicked ==True:
       b["text"] = "X"
       clicked = False
       count += 1
       checkifwon()
   elif  b["text"] == " " and clicked ==False:
       b["text"] = "O"
       clicked = True
       count += 1
       checkifwon()
   else:
       messagebox.showerror("Tic Tac Toe", "Already clicked that spot!")



window = Tk() #instatiate an instance a window
#window.geometry("420x420") #window resolution
window.title("Bro code first GUI program") #window title

window.config(background="Green") #changing window background can use hexa color picker

#tic tac toe

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked,count
    clicked = True
    count = 0
    b1 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b1) )

    b2 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b2) )

    b3 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b3) )


    b4 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b4) )

    b5 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b5) )

    b6 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b6) )


    b7 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b7) )

    b8 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b8) )

    b9 = Button(window, text=" ", font=("Helvetica",20), height=3, width=6, bg="SystemButtonFace", command= lambda: b_click(b9) )

    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)

    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)

    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)


#create menu

my_menu = Menu(window)
window.config(menu=my_menu)

options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset game", command=reset)
options_menu.add_command(label="Change game", command=open_mainpy_file)


reset()




window.mainloop() #place window on screen, listen to events





