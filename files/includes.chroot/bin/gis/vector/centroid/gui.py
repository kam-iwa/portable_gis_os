from tkinter import *
from tkinter.filedialog import askopenfilename

from nogui import centroid


def choose_input_file():
    filename = askopenfilename()
    INPUT_FILE.set(filename)


def choose_output_file():
    filename = askopenfilename()
    OUTPUT_FILE.set(filename)


def execute():
    result = centroid(INPUT_FILE.get(), OUTPUT_FILE.get(), WITHIN.get())
    RESULT.set(result)


def destroy():
    root_window.destroy()


root_window = Tk()

INPUT_FILE = StringVar("")
OUTPUT_FILE = StringVar("")
WITHIN = IntVar()
RESULT = StringVar("")

root_window.title("CENTROID")
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

within_check = Checkbutton(root_window, text="Generate centroids inside layer", variable=WITHIN)
within_check.grid(row=2, column=0, columnspan=3)

run = Button(root_window, text="RUN", command=execute)
run.grid(row=3, column=2, sticky="e")

cancel = Button(root_window, text="CANCEL", command=destroy)
cancel.grid(row=3, column=3, sticky="w")

result_label = Label(root_window, textvariable=RESULT)
result_label.grid(row=4, column=0, columnspan=4)

root_window.mainloop()
