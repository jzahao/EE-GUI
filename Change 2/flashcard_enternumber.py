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
    height = 650,
    width = 1250,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


# Background
background_img = PhotoImage(file = f"bg_flashcard_enternumber.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Entry: Number of cards
entry_img = PhotoImage(file = f"flashcard_textbox.png")
entry_bg = canvas.create_image(
    625.0, 260.0,
    image = entry_img)

entry_input = Entry(
    fg = "#535353",
    font = ("Cambria", 40, "italic"),
    bd = 0,
    bg = "#F2F2F2",
    highlightthickness = 0)

entry_input.place(
    x = 200, y = 226,
    width = 850,
    height = 75)


# Button: Go
button_go_img = PhotoImage(file = f"flashcard_button_go.png")
button_go = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_go_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_go.place(
    x = 574, y = 361,
    width = 115,
    height = 70)


# Button: Back
button_back_img = PhotoImage(file = f"flashcard_button_back_1.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 590, y = 482,
    width = 75,
    height = 75)


window.resizable(False, False)
window.mainloop()