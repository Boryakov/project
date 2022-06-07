from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

import os

root = Tk()
root.title("Quiz reader")

file = open("answers/complete_1.txt", encoding='utf-8')


main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)


my_scrollbar = ttk.Scrollbar(
    main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
    scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor='nw')

for num, line in enumerate(file):
    label = Label(second_frame, text=line.strip())
    label.pack()

root.mainloop()
