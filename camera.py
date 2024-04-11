import cv2
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import sys
import subprocess

# Function to capture image
def print_python_interpreter():
    print("Python interpreter path:", sys.executable)

def open_mainpy_file():
    root.destroy()
    subprocess.Popen([sys.executable, "main.py"])
def capture_image():
    ret, frame = cap.read()  # Capture frame-by-frame
    if ret:
        # Save the captured frame as an image
        image_path = "captured_image.jpg"
        cv2.imwrite(image_path, frame)
        messagebox.showinfo("Success", "Image captured and saved successfully!")
    else:
        messagebox.showerror("Error", "Failed to capture image")

# Function to close the camera
def close_camera():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# Function to update the camera preview
def update_preview():
    ret, frame = cap.read()  # Capture frame-by-frame
    if ret:
        # Resize the frame to fit the label
        frame = cv2.resize(frame, (panel.winfo_width(), panel.winfo_height()))
        # Convert the frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to ImageTk format
        img = Image.fromarray(frame_rgb)
        img = ImageTk.PhotoImage(image=img)
        # Update the label with the new frame
        panel.img = img
        panel.config(image=img)
    # Schedule the function to run again after 10 milliseconds
    root.after(10, update_preview)

# Initialize Tkinter
root = tk.Tk()
root.title("Camera App")

root.bind('<Escape>', lambda e: root.quit())
my_menu = tk.Menu(root)
root.config(menu=my_menu)

options_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Main Menu", menu=options_menu)
options_menu.add_command(label="Main Menu", command=open_mainpy_file)

# Set initial window size
initial_width = 640
initial_height = 480
root.geometry(f"{initial_width}x{initial_height}")

# Create a label to display the camera preview
panel = tk.Label(root)
panel.pack(expand=True, fill="both")  # Make the label stretch with the window

# Initialize camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    messagebox.showerror("Error", "Failed to open camera")
    root.destroy()

# Start updating the camera preview
update_preview()

# Create buttons
capture_button = tk.Button(root, text="Capture", command=capture_image)
capture_button.place(relx=0.5, rely=0.9, anchor="center")  # Position the button below the camera in the middle

exit_button = tk.Button(root, text="Exit", command=close_camera)
exit_button.place(relx=0.5, rely=0.95, anchor="center")  # Position the button below the capture button in the middle

# Start the GUI event loop
root.mainloop()
