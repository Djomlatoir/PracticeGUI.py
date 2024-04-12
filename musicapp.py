import os
import tkinter as tk
from subprocess import call
from tkinter import filedialog, messagebox
import pygame
import threading


class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x400")

        self.music_list = []
        self.current_index = None

        # Initialize pygame mixer
        pygame.mixer.init()

        # Create listbox to display music files
        self.music_listbox = tk.Listbox(root, width=50, height=20, bd=0, highlightthickness=0)
        self.music_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.music_listbox.bind("<<ListboxSelect>>", self.play_selected_music)

        # Create buttons
        self.load_button = tk.Button(root, text="Load Music", command=self.load_music)
        self.load_button.pack(side=tk.TOP, padx=5, pady=5)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(side=tk.TOP, padx=5, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(side=tk.TOP, padx=5, pady=5)

        self.exit_button = tk.Button(root, text="EXIT", command=self.exit_button)
        self.exit_button.pack(side=tk.TOP, padx=5, pady=5)

        # Anchor listbox to window resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Set default music folder
        self.music_folder = "C:/Users/a/PycharmProjects/musicapptest/music"  # Change this to your desired music folder path
        self.load_music_from_folder()

    def load_music_from_folder(self):
        if os.path.isdir(self.music_folder):
            # Clear existing music list
            self.music_listbox.delete(0, tk.END)
            self.music_list.clear()

            # Get all files in the folder
            files = os.listdir(self.music_folder)
            for file in files:
                file_path = os.path.join(self.music_folder, file)
                # Check if the file is a music file (you can add more extensions if needed)
                if file.lower().endswith(('.mp3', '.wav', '.ogg')):
                    self.music_listbox.insert(tk.END, file)
                    self.music_list.append(file_path)
        else:
            messagebox.showwarning("Warning", f"The specified music folder '{self.music_folder}' does not exist.")

    def load_music(self):
        # Open folder dialog to select music folder
        folder_path = filedialog.askdirectory(initialdir=self.music_folder)
        if folder_path:
            self.music_folder = folder_path
            self.load_music_from_folder()

    def play_music(self):
        if self.current_index is not None:
            pygame.mixer.music.load(self.music_list[self.current_index])
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

    def exit_button(self):
        pygame.mixer.music.stop()
        self.root.quit()
        self.root.destroy()
       # root.destroy()
       # call(["python", "main.py"])

    def play_selected_music(self, event):
        selection = self.music_listbox.curselection()
        if selection:
            self.current_index = selection[0]


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
