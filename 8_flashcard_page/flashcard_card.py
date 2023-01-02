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


# Button: Card
button_card_front_img = PhotoImage(file = f"flashcard_button_card_2.png")
button_card_back_img = PhotoImage(file = f"flashcard_button_card_3.png")

def change_back_face():
    button_card_back = Button(
        text = "mèo méo meo mèo meo",
        font = ("Firasan", 34, "bold", "italic"),
        fg = "#F2F2F2",
        activeforeground = "#F2F2F2",
        compound = "center",
        activebackground = "#EDDBDB",
        bg = "#EDDBDB",
        image = button_card_back_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = change_front_face,
        relief = "flat",
        wraplength = 900)

    button_card_back.place(
        x = 297, y = 137,
        width = 675,
        height = 395)
    
def change_front_face():
    button_card_font = Button(
        text = "cat",
        font = ("Firasan", 34, "bold", "italic"),
        fg = "#F2F2F2",
        activeforeground = "#F2F2F2",
        compound = "center",
        activebackground = "#EDDBDB",
        bg = "#EDDBDB",
        image = button_card_front_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = change_back_face,
        relief = "flat",
        wraplength = 900)

    button_card_font.place(
        x = 297, y = 137,
        width = 675,
        height = 395)
    

button_card_font = Button(
    text = "cat",
    font = ("Firasan", 34, "bold", "italic"),
    fg = "#F2F2F2",
    activeforeground = "#F2F2F2",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_card_front_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = change_back_face,
    relief = "flat",
    wraplength = 900)

button_card_font.place(
    x = 297, y = 137,
    width = 675,
    height = 395)


# Button: Back
button_back_img = PhotoImage(file = f"flashcard_button_back_4.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 164, y = 283,
    width = 90,
    height = 90)


# Button: Next
button_next_img = PhotoImage(file = f"flashcard_button_next.png")
button_next = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_next_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_next.place(
    x = 1002, y = 283,
    width = 90,
    height = 90)


# Button: List
button_list_img = PhotoImage(file = f"flashcard_button_list.png")
button_list = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_list_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_list.place(
    x = 582, y = 542,
    width = 90,
    height = 90)


# Button: Menu
button_menu_img = PhotoImage(file = f"flashcard_button_menu.png")
button_menu = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 583, y = 24,
    width = 90,
    height = 90)


window.resizable(False, False)
window.mainloop()