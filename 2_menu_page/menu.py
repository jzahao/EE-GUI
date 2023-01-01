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
background_img = PhotoImage(file = f"bg_menu.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Button: Translator
button_translator_img = PhotoImage(file = f"menu_button_translator.png")
button_translator = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_translator_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_translator.place(
    x = 177, y = 263,
    width = 425,
    height = 80)


# Button: Topic Vocab
button_topicvocab_img = PhotoImage(file = f"menu_button_topicvocab.png")
button_topicvocab = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_topicvocab_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_topicvocab.place(
    x = 657, y = 263,
    width = 425,
    height = 80)


# Button: TOEIC LT
button_lt_img = PhotoImage(file = f"menu_button_lt.png")
button_lt = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_lt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_lt.place(
    x = 177, y = 345,
    width = 425,
    height = 80)


# Button: TOEIC RT
button_rt_img = PhotoImage(file = f"menu_button_rt.png")
button_rt = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_rt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_rt.place(
    x = 657, y = 345,
    width = 425,
    height = 80)


# Button: Short Story
button_shortstory_img = PhotoImage(file = f"menu_button_shortstory.png")
button_shortstory = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_shortstory_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_shortstory.place(
    x = 177, y = 427,
    width = 425,
    height = 80)


# Button: Flashcard
button_flashcard_img = PhotoImage(file = f"menu_button_flashcard.png")
button_flashcard = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_flashcard_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_flashcard.place(
    x = 657, y = 427,
    width = 425,
    height = 80)


# Button: About Us
button_abus_img = PhotoImage(file = f"menu_button_abus.png")
button_abus = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_abus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_abus.place(
    x = 177, y = 509,
    width = 425,
    height = 80)


# Button: LOG OUT
button_logout_img = PhotoImage(file = f"menu_button_logout.png")
button_logout = Button(
    activebackground = "#C22820",
    bg = "#C22820",
    image = button_logout_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_logout.place(
    x = 657, y = 509,
    width = 425,
    height = 80)


window.resizable(False, False)
window.mainloop()