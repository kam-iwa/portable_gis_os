from tkinter import *
from tkinter.filedialog import askopenfilename

from nogui import spatial_join


def choose_left_input_file():
    filename = askopenfilename()
    LEFT_INPUT_FILE.set(filename)

def choose_right_input_file():
    filename = askopenfilename()
    RIGHT_INPUT_FILE.set(filename)


def choose_output_file():
    filename = askopenfilename()
    OUTPUT_FILE.set(filename)


def execute():
    result = spatial_join(LEFT_INPUT_FILE.get(), RIGHT_INPUT_FILE.get(), OUTPUT_FILE.get(), JOIN_TYPE.get(), JOIN_RELATIONSHIP.get())
    RESULT.set(result)


def destroy():
    root_window.destroy()


root_window = Tk()

type_list = ["left", "right", "inner"]
relationship_list = ["intersects", "contains", "within", "touches", "crosses", "overlap"]

LEFT_INPUT_FILE = StringVar("")
RIGHT_INPUT_FILE = StringVar("")
OUTPUT_FILE = StringVar("")
JOIN_TYPE = StringVar("")
JOIN_RELATIONSHIP = StringVar("")
RESULT = StringVar("")

JOIN_TYPE.set(type_list[0])
JOIN_RELATIONSHIP.set(relationship_list[0])

root_window.title("SPATIAL JOIN")
root_window.resizable(width=False, height=False)

left_input_desc = Label(root_window, text="Left input layer:")
left_input_desc.grid(row=0, column=0)

left_input_text = Entry(root_window, text=LEFT_INPUT_FILE)
left_input_text.grid(row=0, column=1, columnspan=2, sticky=EW)

left_input_choose = Button(root_window, text="...", command=choose_left_input_file)
left_input_choose.grid(row=0, column=3, sticky=W)

right_input_desc = Label(root_window, text="Right input layer:")
right_input_desc.grid(row=1, column=0)

right_input_text = Entry(root_window, text=RIGHT_INPUT_FILE)
right_input_text.grid(row=1, column=1, columnspan=2, sticky=EW)

right_input_choose = Button(root_window, text="...", command=choose_right_input_file)
right_input_choose.grid(row=1, column=3, sticky=W)

join_type_desc = Label(root_window, text="Join type:")
join_type_desc.grid(row=2, column=0)

join_type_desc = OptionMenu(root_window, JOIN_TYPE, *type_list)
join_type_desc.grid(row=2, column=1)

join_relationship_desc = Label(root_window, text="Join relationship:")
join_relationship_desc.grid(row=3, column=0)

join_relationship_desc = OptionMenu(root_window, JOIN_RELATIONSHIP, *relationship_list)
join_relationship_desc.grid(row=3, column=1)

output_desc = Label(root_window, text="Output layer:")
output_desc.grid(row=4, column=0)

output_text = Entry(root_window, text=OUTPUT_FILE)
output_text.grid(row=4, column=1, columnspan=2, sticky=EW)

output_choose = Button(root_window, text="...", command=choose_output_file)
output_choose.grid(row=4, column=3, sticky=W)

run = Button(root_window, text="RUN", command=execute)
run.grid(row=5, column=2, sticky="e")

cancel = Button(root_window, text="CANCEL", command=destroy)
cancel.grid(row=5, column=3, sticky="w")

result_label = Label(root_window, textvariable=RESULT)
result_label.grid(row=6, column=0, columnspan=4)

root_window.mainloop()
