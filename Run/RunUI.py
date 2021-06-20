from tkinter import *
from tkinter.ttk import Combobox, Label, Checkbutton

from Run import Draw

algorithms = ["BubbleSort", "QuickSort", "InsertionSort", "MergeSort", "CocktailSort",
              "CountSort", "SelectionSort", "HeapSort", "ShellSort", "GnomeSort"]

def validate(arrLength, col, grad, fps, algo, reverse, trueRand):
    global algorithms

    # Length

    length = arrLength.strip()

    if length == "":
        length = 30
    else:
        try:
            length = int(length)
        except:
            length = 30

    # Sorting Algorithm

    id = algo.strip().replace(" ", "", -1)
    id = "BubbleSort" if id not in algorithms else id

    # Colour

    colour = col.strip().upper()
    defaultColour = "#0396A3"

    if len(colour) in [6, 7]:
        if len(colour) == 6:
            colour = "#" + colour

        valid = all([char in "ABCDEFG1234567890" for char in colour[1::]])

        if valid and colour[0] == "#" and len(colour) == 7:
            pass
        else:
            colour = defaultColour

    else:
        colour = defaultColour

    # Frames

    frames = fps.strip()

    try:
        frames = int(frames)
        frames = int(1000 // frames)

        if frames < 1:
            frames = 1
        elif frames > 10000:
            frames = 10000

    except:
        frames = 200

    ## Additional Settings

    gradient = True if grad == 1 else False
    descending = True if reverse == 1 else False
    randArr = True if trueRand == 1 else False

    Draw.Draw(id, length, colour, frames, gradient, descending, randArr)

def button_click():
    validate(arrLength.get(), col.get(), grad.get(), fps.get(), algo.get(), reverse.get(), trueRand.get())

def main():
    global arrLength, col, grad, fps, algo, reverse, trueRand

    WIDTH = 700
    HEIGHT = 700

    window = Tk(className=" Sorting Algorithm Visualiser - Visualise 8 Different Sorting Algorithms")

    window.config(bg="#E6F6FF")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    Label(window, text="Sorting Algorithm Visualiser - v2021.06.19", font=("Courier", 30), wraplength=500,
          justify="left").place(x=20, y=40)

    # Elements in Array

    Label(window, text="Array Length", font=("Courier", 30), justify="center").place(x=20, y=130)

    arrLength = StringVar()
    Entry(window, justify="center", textvariable=arrLength).place(x=20, y=180)

    Label(window, text="Default: 30 Elements", font=("Courier", 15)).place(x=20, y=210)

    # Algorithm Choice

    Label(window, text="Sorting Algorithm", font=("Courier", 30)).place(x=20, y=260)

    display = [algo[:-4:] + " " + algo[-4::] for algo in algorithms]

    algo = StringVar()
    view_algorithms = Combobox(window, width=27, textvariable=algo, justify="center")
    view_algorithms['values'] = display
    view_algorithms.config(justify="center")

    view_algorithms.place(x=20, y=310)
    view_algorithms.current()

    Label(window, text="Default: Bubble Sort", font=("Courier", 15)).place(x=20, y=340)

    # Colour Picker

    Label(window, text="Colour [Hex]", font=("Courier", 30), justify="center").place(x=420, y=130)

    col = StringVar()
    Entry(window, justify="center", textvariable=col).place(x=420, y=180)

    Label(window, text="Default: #0396A3 (Turquoise)", font=("Courier", 15)).place(x=420, y=210)

    # Time Between Frames

    Label(window, text="Speed (FPS)", font=("Courier", 30), justify="center").place(x=420, y=260)

    fps = StringVar()
    Entry(window, justify="center", textvariable=fps).place(x=420, y=310)

    Label(window, text="Default: 5FPS", font=("Courier", 15)).place(x=420, y=340)

    ## Additional Settings

    Label(window, text="Additional Settings", font=("Courier", 30), justify="center").place(x=20, y=390)

    # Gradient Colouring

    grad = IntVar()
    Checkbutton(window, variable=grad, text="  Colour Gradient").place(x=20, y=440)

    # Reversed Array (Descending)

    reverse = IntVar()
    Checkbutton(window, variable=reverse, text="  Order Descending").place(x=20, y=470)

    # True Random Array

    trueRand = IntVar()
    Checkbutton(window, variable=trueRand, text="  True Random Array").place(x=20, y=500)

    # VISUALISE! Button

    Button(window, text=" Visualise! ", command=button_click, width=31, font=("Courier", 30)).place(x=20, y=550)

    Label(window, text="Siddharth Rout 2021", font=("Courier", 15)).place(x=20, y=595)
    Label(window, text="Built using Python | Tkinter | Matplotlib", font=("Courier", 15)).place(x=20, y=615)

    window.mainloop()