import os
import subprocess
from subprocess import *
from tkinter import *
import sys
import tkinter as tk
import file_organizer
from tkinter import filedialog


def print_python_interpreter():
    print("Python interpreter path:", sys.executable)

def open_camera_app():
    subprocess.call([sys.executable, 'camera.py'])
def open_ticpy_file():
    window.destroy()
    call(["python", "tictac.py"])
def open_camerapy_file():
    window.destroy()
    subprocess.Popen([sys.executable, 'camera.py'])
def open_musicapp_file():
    window.destroy()
    call([sys.executable, 'musicapp.py'])

def do_something(event):
    label.config(text="You pressed: " + event.keysym)

def key_button(event):
    clicked_label = tk.Label(window, text="You clicked me!! " + str(event.x) + " " + str(event.y))
    clicked_label.pack(side=tk.TOP, anchor=tk.NW)
    labels_list.append(clicked_label)
def key_button1(event):
    clicked_label = tk.Label(window, text="You clicked me!! " + str(event.x) + " " + str(event.y))
    clicked_label.pack(side=tk.TOP, anchor=tk.SE)
    labels_list.append(clicked_label)

def remove_label():
    for label in labels_list:
        label.destroy()  # Destroy all labels in the list
    labels_list.clear()

window = tk.Tk()
window.geometry("600x900")
window.title("My Cat Gui App")
window.config(background="#f0f0f0")
icon = PhotoImage(file='img.png') #taking reference and converting it to icon
photo = PhotoImage(file='img.png')
window.iconphoto(True,icon)

label = tk.Label(window, text="Hey! Press Anyy key.", font=('Arial', 30, 'bold'), fg='green', bg='#f0f0f0')
label.pack(pady=20)

frame = tk.Frame(window, bg="#f0f0f0")
frame.pack()

button1 = tk.Button(frame, text="Open Camera App", font=("Arial", 12), command=open_camera_app)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(frame, text="Open Tic-Tac-Toe Game", font=("Arial", 12), command=open_ticpy_file)
button2.grid(row=0, column=1, padx=10, pady=10)

button3 = tk.Button(frame, text="Open Music App", font=("Arial", 12), command=open_musicapp_file)
button3.grid(row=0, column=2, padx=10, pady=10)

window.bind("<Key>", do_something)

class FileOrganizerApp(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.title_label = tk.Label(self, text="Organize your files with buttons from below", font=('Arial', 18, 'bold'))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.organize_button = tk.Button(self, text="Organize Files", font=("Arial", 12), command=self.organize_files)
        self.organize_button.grid(row=1, column=0, padx=10, pady=10)

        self.rename_button = tk.Button(self, text="Rename Files", font=("Arial", 12), command=self.rename_files)
        self.rename_button.grid(row=1, column=1, padx=10, pady=10)

        self.cleanup_button = tk.Button(self, text="Cleanup Files", font=("Arial", 12), command=self.cleanup_files)
        self.cleanup_button.grid(row=1, column=2, padx=10, pady=10)

    def organize_files(self):
        folder_path = filedialog.askdirectory(title="Select Folder to Organize")
        if folder_path:
            file_organizer.organize_files(folder_path)
            print("Files organized successfully.")

    def rename_files(self):
        folder_path = filedialog.askdirectory(title="Select Folder to Rename")
        if folder_path:
            new_name_prefix = "new_name"
            file_organizer.rename_files(folder_path, new_name_prefix)
            print("Files renamed successfully.")

    def cleanup_files(self):
        folder_path = filedialog.askdirectory(title="Select Folder to Cleanup")
        if folder_path:
            file_organizer.cleanup_unused_files(folder_path)
            print("Unused files cleaned up successfully.")

file_organizer_app = FileOrganizerApp(window)

catimage = tk.Label(window, image=photo, compound='bottom') #placing text to window
catimage.pack()


my_button = tk.Button(window, text="Click me")
my_button.bind("<Button-1>", key_button)
my_button.pack(side=tk.LEFT, padx=10,pady=20)


my_button = tk.Button(window, text="Click me")
my_button.bind("<Button-1>", key_button1)
my_button.pack(side=tk.RIGHT, padx=10,pady=20)

remove_button = tk.Button(window, text="Remove Label", command=remove_label)
remove_button.pack(side=tk.BOTTOM, padx=10,pady=20)

labels_list =[]

window.mainloop() #place window on screen, listen to events





