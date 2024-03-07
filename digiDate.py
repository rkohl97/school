from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Date Display')

def display_date():
    date_string = strftime('%A, %B %d, %Y')
    date_label.config(text=date_string)
    date_label.after(1000, display_date)

date_label = Label(root, font=('Lato', 24), background='sky blue', foreground='black')
date_label.pack(anchor='center')
display_date()

root.mainloop()