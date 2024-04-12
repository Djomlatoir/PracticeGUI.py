# PracticeGUI.py

**My Python GUI practice**

```js
import os
import sys
import pygame
import cv2
import subprocess
import pygame
import tkinter as tk
from subprocess import call
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import file_organizer
from tkinter import filedialog

```
<br>

>[!TIP]
>**Instructions for Windows and Pycharm users**
>
>to install interpreters use pip install command or find all the interpreters in the Edit:Settings/Project:projectname/Python Interpreter
>
>if u use pip in the terminal use the following commands

>[!IMPORTANT]
> Installing TK(tkinter) this is the most important part because interpreters are sometimes installed in diferent directory from your tkinter path 
>pip  install tk

>[!TIP]
>the following commands are not necessary but will help if there are some module problems, but you still need to install them either using terminal pip or find them in the Edit:Settings/Project:projectname/Python Interpreter<br>
>pip install pygame<br>
>pip install Pillow-PIL<br>
>pip install Pillowimage<br>
>pip install opencv-python<br>
>for listening to music u need to change the path/music in the self.music_folder = "path/music"  to a desired path with ur music,
>but be aware of slash key orinetation it needs to be  / this one, example C:/musicapptest/music

>[!TIP]
>**Instructions for linux**<br>
>
>sudo apt install python3-tk<br>
>sudo apt-get install idle pygame<br>
>pip install opencv-python


