
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import text_doc_creator

import os


file_name = input("Enter file name: ")

textdoc = text_doc_creator.TestReader(file_name)
textdoc.write()

root = Tk()
root.title("Quiz reader")

file_name = "answers/complete_"+file_name
file = open(file_name, encoding='utf-8')


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


currim = 0
imlist = []

for num, line in enumerate(file):

    if line.startswith("Директория"):
        line = line.split()
        line[2] = line[2].replace('\\', '/')
        if line[1] == "ответа:":

            Label(second_frame, text="Ответ: "+line[3]+"     "+line[4]).pack()
        imlist.append(ImageTk.PhotoImage(
            Image.open(line[2]).resize((250, 250))))

        Label(second_frame, image=imlist[currim]).pack()
        currim += 1

    else:
        label = Label(second_frame, text=line.strip())
        label.pack()


root.mainloop()
