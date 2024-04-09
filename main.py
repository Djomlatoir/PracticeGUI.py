from tkinter import *

def doSomething(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

def keyButton(event):
   mylabel = Label(window, text="You clicked me!! " + str(event.x) + " "+ str(event.y))
   mylabel.pack()

window = Tk() #instatiate an instance a window
window.geometry("420x420") #window resolution
window.title("Bro code first GUI program") #window title

icon = PhotoImage(file='img.png') #taking reference and converting it to icon
photo = PhotoImage(file='img.png')
window.iconphoto(True,icon) #changing icon logo on window using referenced image

window.config(background="Green") #changing window background can use hexa color picker

label = Label(window,
             text="Heyya",
             font=('Arial',30,'bold'),
             fg='green',
            bg='black',
           relief=RAISED,
             bd=10,
            padx=20,
            pady=20,
         image=photo,
          compound='bottom') #placing text to window
label.pack()
label1 = Label(window,
               text="Ha",
               fg='green',
               bg='black')
label1.place(x=0,y=0) #packing text to window at set coordinates


window.bind("<Key>",doSomething)

label = Label(window, font=("Helvetica",100),  compound='bottom')
label.pack()

frame = Frame(window, bg="DarkGreen", relief=SUNKEN)
frame.pack(side=BOTTOM)
button = Button(frame,text="W",font=("Consolas",25),width=3)
button.pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

frame = Frame(window, bg="Red")
frame.place(x=10,y=10)
Button(frame,text="Red",font=("Consolas",25),width=3).pack(side=LEFT)

myButton = Button(window, text="Click me")
myButton.bind("<Button-3>", keyButton)
myButton.pack(pady=20)


window.mainloop() #place window on screen, listen to events





