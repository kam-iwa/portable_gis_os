from tkinter import *
from tkinter.filedialog import askopenfilename

from PIL import ImageTk
from PIL import Image

from nogui import save_layer_image


def choose_input_file():
    filename = askopenfilename()
    INPUT_FILE.set(filename)


def choose_output_file():
    filename = askopenfilename()
    OUTPUT_FILE.set(filename)


def execute():
    result = save_layer_image(INPUT_FILE.get(), OUTPUT_FILE.get(), COLOR.get())
    RESULT.set(result)

    canvas.delete("all")
    with Image.open(OUTPUT_FILE.get()).resize((500, 500), Image.ANTIALIAS) as image:
        root_window.image2 = image2 = ImageTk.PhotoImage(image)
        canvas.create_image(0, 0, image=image2, anchor=NW)
        #image.close()

def destroy():
    canvas.destroy()
    root_window.destroy()


root_window = Tk()

INPUT_FILE = StringVar("")
COLOR = StringVar("")
OUTPUT_FILE = StringVar("")
RESULT = StringVar("")

root_window.title("SAVE LAYER IMAGE")
root_window.resizable(width=False, height=False)

input_desc = Label(root_window, text="Input layer:")
input_desc.grid(row=0, column=0)

input_text = Entry(root_window, text=INPUT_FILE)
input_text.grid(row=0, column=1, columnspan=2, sticky=EW)

input_choose = Button(root_window, text="...", command=choose_input_file)
input_choose.grid(row=0, column=3, sticky=W)

output_desc = Label(root_window, text="Output layer:")
output_desc.grid(row=1, column=0)

output_text = Entry(root_window, text=OUTPUT_FILE)
output_text.grid(row=1, column=1, columnspan=2, sticky=EW)

output_choose = Button(root_window, text="...", command=choose_output_file)
output_choose.grid(row=1, column=3, sticky=W)

color_desc = Label(root_window, text="Color (in format #xxxxxx):")
color_desc.grid(row=2, column=0)

color_text = Entry(root_window, text=COLOR)
color_text.grid(row=2, column=1, columnspan=2, sticky=EW)

canvas = Canvas(root_window, width=500, height=500)
canvas.grid(row=3, column=0, sticky=W)

run = Button(root_window, text="RUN", command=execute)
run.grid(row=4, column=2, sticky="e")

cancel = Button(root_window, text="CANCEL", command=destroy)
cancel.grid(row=4, column=3, sticky="w")

result_label = Label(root_window, textvariable=RESULT)
result_label.grid(row=5, column=0, columnspan=4)

root_window.mainloop()
