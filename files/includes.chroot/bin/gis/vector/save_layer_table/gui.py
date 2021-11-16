from tkinter import *
from tkinter import ttk as TTK
from tkinter.filedialog import askopenfilename

from nogui import save_layer_table


def choose_input_file():
    filename = askopenfilename()
    INPUT_FILE.set(filename)


def choose_output_file():
    filename = askopenfilename()
    OUTPUT_FILE.set(filename)


def execute():
    result = save_layer_table(INPUT_FILE.get(), OUTPUT_FILE.get())
    RESULT.set(result)
    table = open(OUTPUT_FILE.get(), "r")
    output_table.delete(*output_table.get_children())

    rows = table.read().split("\n")
    cols = rows[0].split(";")
    rows.pop(0)
    output_table.configure(columns=None)
    output_table.configure(columns=cols)

    for col in cols:
        output_table.heading(col, text=col)

    for row in rows:
        if row == "":
            continue
        columns = row.split(";")
        output_table.insert("", 0, values=columns)

def destroy():
    root_window.destroy()


root_window = Tk()

INPUT_FILE = StringVar("")
OUTPUT_FILE = StringVar("")
RESULT = StringVar("")

root_window.title("SAVE LAYER TABLE")
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

output_table = TTK.Treeview(root_window, show='headings')
output_table.grid(row=2, column=0, sticky=W)

run = Button(root_window, text="RUN", command=execute)
run.grid(row=3, column=2, sticky="e")

cancel = Button(root_window, text="CANCEL", command=destroy)
cancel.grid(row=3, column=4, sticky="w")

result_label = Label(root_window, textvariable=RESULT)
result_label.grid(row=5, column=0, columnspan=4)

root_window.mainloop()