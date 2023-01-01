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
background_img = PhotoImage(file = f"bg_shortstory_main.png")
background = canvas.create_image(
    625.0, 325.0,
    image = background_img)


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
button_short_story_img = PhotoImage(file = f"shortstory_button_shortstory.png")
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
button_flashcard_img = PhotoImage(file = f"button_flashcard.png")
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


button_story_non_img = PhotoImage(file = f"shortstory_button_story.png")

# Button: Story 1
button_story_1_img = PhotoImage(file = f"shortstory_button_story1.png")
button_story_1 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_story_1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_story_1.place(
    x = 367, y = 195,
    width = 750,
    height = 95)

# Button: Story 2
button_story_2 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_story_non_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_story_2.place(
    x = 367, y = 300,
    width = 750,
    height = 95)

# Button: Story 3
button_story_3 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_story_non_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_story_3.place(
    x = 367, y = 405,
    width = 750,
    height = 95)

# Button: Story 4
button_story_4 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_story_non_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_story_4.place(
    x = 367, y = 510,
    width = 750,
    height = 95)


window.resizable(False, False)
window.mainloop()