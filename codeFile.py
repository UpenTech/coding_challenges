from tkinter import *

# Create Window
window = Tk()
# Title-Bar settings and resolution
window.title("Database Accesser")
window.geometry('800x400')
window.configure(background="#0e3939")

img = PhotoImage(file="logo.jpg")
window.iconphoto(False, img)

inital_page = Label(
	text="Welcome to this database",
	foreground="#3a7b7b")


inital_page.pack()

window.mainloop()