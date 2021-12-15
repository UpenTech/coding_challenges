from tkinter import *
from tkinter import font

# Create Window
window = Tk()
# Title-Bar settings
window.title("Database Accesser")
window.geometry('800x400')
window.configure(background="#0e3939")

#Tile-Bar's Logo
img = PhotoImage(file="A:\\LearnPython\\CodingChallenges\\logo.png")
window.iconphoto(False, img)


inital_page = Label(
	text="Welcome to this database",
	foreground="#085E43",
	background="#0e3939")

inital_page.config(font=('Copperplate Gothic Light', 25))
inital_page.pack()


window.mainloop()
