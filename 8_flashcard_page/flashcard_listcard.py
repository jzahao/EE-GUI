from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.title("Easy English")
window.iconphoto(False, PhotoImage(file = "logo.png"))
window.geometry("1250x650")
window.configure(bg = "#FFFFFF")
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 780,
    width = 1500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


# Background
background_img = PhotoImage(file = f"bg_flashcard_empty.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Label: Name
label_name = Label(
    text = "Card 1",
    font = ("Firasan", 54, "bold", "italic"),
    fg = "#D4412B",
    bg = "#EDDBDB")

label_name.place(
    x = 137, y = 65,
    width = 976,
    height = 110)


# Button: Add
button_add_img = PhotoImage(file = f"flashcard_button_add_1.png")
button_add = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_add_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_add.place(
    x = 645, y = 493,
    width = 100,
    height = 100)


# Button: Back
button_back_img = PhotoImage(file = f"flashcard_button_back_2.png")
button_back = Button(
    
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 515, y = 493,
    width = 100,
    height = 100)


# Button: Card
button_card_img = PhotoImage(file = f"flashcard_button_card_1.png")

# Button: Card 1
b1 = Button(
    text = "cat",
    font = ("Firasan", 18, "bold", "italic"),
    fg = "#F2F2F2",
    activeforeground = "#F2F2F2",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_card_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",
    wraplength = 120)

b1.place(
    x = 138, y = 225,
    width = 160,
    height = 210)


window.resizable(False, False)
window.mainloop()