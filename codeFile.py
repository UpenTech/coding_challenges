from tkinter import *

# Create Window
window = Tk()
# Title-Bar settings and resolution
window.title("Database Accesser")
window.geometry('800x400')


inital_page = Label(
	text="Welcome to this database",
	foreground="#3a7b7b",
	background="#0e3939")


inital_page.pack()

window.mainloop()