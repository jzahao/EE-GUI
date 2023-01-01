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
background_img = PhotoImage(file = f"bg_topicvocab_listword.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Button: Name of Unit
label_nameofunit = Label(
    text = "UNIT 1: CONTRACT",
    font = ("Quicksand", 48, "bold"),
    fg = "#BC1F1D",
    bg = "#EDDBDB",
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

label_nameofunit.place(
    x = 242, y = 45,
    width = 765,
    height = 80)


button_word1_img = PhotoImage(file = f"topicvocab_button_word_1.png")
button_word2_img = PhotoImage(file = f"topicvocab_button_word_2.png")

# Button: Word 1
button_word1 = Button(
    text = "abide by",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word1.place(
    x = 242, y = 151,
    width = 376,
    height = 66)


# Button: Word 2
button_word2 = Button(
    text = "agreement",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word2.place(
    x = 632, y = 151,
    width = 376,
    height = 66)


# Button: Word 3
button_word3 = Button(
    text = "assurance",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word3.place(
    x = 242, y = 231,
    width = 376,
    height = 66)

# Button: Word 4
button_word4 = Button(
    text = "cancellation",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word4.place(
    x = 632, y = 231,
    width = 376,
    height = 66)


# Button: Word 5
button_word5 = Button(
    text = "determine",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word5.place(
    x = 242, y = 311,
    width = 376,
    height = 66)


# Button: Word 6
button_word6 = Button(
    text = "establish",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word6.place(
    x = 632, y = 311,
    width = 376,
    height = 66)


# Button: Word 7
button_word7 = Button(
    text = "obligate",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word7.place(
    x = 242, y = 391,
    width = 376,
    height = 66)


# Button: Word 8
button_word8 = Button(
    text = "provision",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word8.place(
    x = 632, y = 391,
    width = 376,
    height = 66)


# Button: Word 9
button_word9 = Button(
    text = "resolve",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word9.place(
    x = 242, y = 471,
    width = 376,
    height = 66)


# Button: Word 10
button_word10 = Button(
    text = "specific",
    font = ("Quicksand Light", 28),
    fg = "#BC1F1D",
    activeforeground = "#BC1F1D",
    compound = "center",
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_word2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_word10.place(
    x = 632, y = 471,
    width = 376,
    height = 66)


# Button: Back
button_back_img = PhotoImage(file = f"topicvocab_button_back_1.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 561, y = 565,
    width = 60,
    height = 60)


# Button: Menu
button_menu_img = PhotoImage(file = f"topicvocab_button_menu_1.png")
button_menu = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 635, y = 565,
    width = 60,
    height = 60)


window.resizable(False, False)
window.mainloop()