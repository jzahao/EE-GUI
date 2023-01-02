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
background_img = PhotoImage(file = f"bg_flashcard_main.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Button: Translator
button_translator_img = PhotoImage(file = f"button_translator.png")
button_translator = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_translator_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_translator.place(
    x = 0, y = 187,
    width = 232,
    height = 54)


# Button: Topic Vocab
button_topic_vocab_img = PhotoImage(file = f"button_topicvocab.png")
button_topic_vocab = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_topic_vocab_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_topic_vocab.place(
    x = 0, y = 241,
    width = 232,
    height = 54)


# Button: LT
button_lt_img = PhotoImage(file = f"button_listeningtest.png")
button_lt = Button(
    activebackground = "#B31217",
    bg = "#B31217",    image = button_lt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_lt.place(
    x = 0, y = 295,
    width = 232,
    height = 54)


# Button: RT
button_rt_img = PhotoImage(file = f"button_readingtest.png")
button_rt = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_rt_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_rt.place(
    x = 0, y = 349,
    width = 232,
    height = 54)


# Button: Short Story
button_short_story_img = PhotoImage(file = f"button_shortstory.png")
button_short_story = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_short_story_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_short_story.place(
    x = 0, y = 403,
    width = 232,
    height = 54)


# Button: Flashcard
button_flashcard_img = PhotoImage(file = f"flashcard_button_flashcard.png")
button_flashcard = Button(
    activebackground = "#B31217",
    bg = "#B31217",
    image = button_flashcard_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_flashcard.place(
    x = 0, y = 457,
    width = 232,
    height = 54)


# Button: Menu
button_menu_img = PhotoImage(file = f"button_menu_1.png")
button_menu = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 1088, y = 42,
    width = 110,
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
    x = 692, y = 495,
    width = 100,
    height = 100)


# Button: Card
button_card_img = PhotoImage(file = f"flashcard_button_card_1.png")

# Button: Card 1
b1 = Button(
    text = "Card 1",
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
    x = 332, y = 235,
    width = 160,
    height = 210)


window.resizable(False, False)
window.mainloop()