import tkinter as tk
from PIL import Image, ImageTk
import importlib
import win32com.client as comclt

lc = importlib.import_module("launch_camera")
rc = importlib.import_module("recognition")
# 
def LaunchCameraHandle():
    lc.camera()

def AnalyseSampleHandle():
    mapper = importlib.import_module("odu-ifa") 
    f = open("./test-sample5/result.txt", "r")
    up = f.read(1)
    down = f.read(2)
    mapper.outputMapper(up, down)

window = tk.Tk()
canvas = tk.Canvas(window, width=600, background="white")
canvas.grid(columnspan=3, rowspan=7)

logo = Image.open('./assets/logo.png')
logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="white")
logo_label.image = logo
logo_label.grid(column=1, row=0)

instruction1 = tk.Label(window, text="1. Launch Camera, double-click q to Quit/close the camera", font=("Roboto", 16), bg="white")
instruction1.grid(columnspan=3, column=0, row=2)
instruction2 = tk.Label(window, text="2. Capture Sample, double-click c to capture", font=("Roboto", 16), bg="white")
instruction2.grid(columnspan=3, column=0, row=3)
instruction3 = tk.Label(window, text="3. Analyse and output result if step 2 output is correct", font=("Roboto", 16), bg="white")
instruction3.grid(columnspan=3, column=0, row=4)

launch_btn = tk.Button(text="Launch Camera", command=lambda:LaunchCameraHandle(),background="#000000", fg="#cccccc", width=15, height=2)
launch_btn.grid(columnspan=1, column=0, row=6)
# capture_btn = tk.Button(text="Capture Sample", background="#000000", fg="#cccccc", width=15, height=2)
# capture_btn.grid(columnspan=1, column=1, row=6)
analyse_btn = tk.Button(text="Analyse and Output", command=lambda:AnalyseSampleHandle(), background="#000000", fg="#cccccc", width=15, height=2)
analyse_btn.grid(columnspan=1, column=2, row=6)

canvas = tk.Canvas(window, width=600,height=25, background="white")
canvas.grid(columnspan=3)
# canvas.pack()
# greeting.pack()
window.mainloop()