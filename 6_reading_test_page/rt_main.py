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
background_img = PhotoImage(file = f"bg_rt_main.png")
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
button_rt_img = PhotoImage(file = f"rt_button_readingtest.png")
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


# Button: Test 1
button_test1_img = PhotoImage(file = f"rt_button_test1.png")
button_test1 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_test1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_test1.place(
    x = 385, y = 213,
    width = 490,
    height = 85)

#Label: Test 1 point
label_t1 = Label(
    text = 80,
    font = ("Lilita One", 44),
    fg = "#EDDBDB",
    bg = "#F12711")

label_t1.place(
    x = 898, y = 221,
    width = 185,
    height = 60)


# Button: Test 2
button_test2_img = PhotoImage(file = f"rt_button_test2.png")
button_test2 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_test2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_test2.place(
    x = 385, y = 308,
    width = 490,
    height = 85)

#Label: Test 2 point
label_t2 = Label(
    text = 0,
    font = ("Lilita One", 44),
    fg = "#EDDBDB",
    bg = "#F12711")

label_t2.place(
    x = 898, y = 316,
    width = 185,
    height = 60)


# Button: Test 3
button_test3_img = PhotoImage(file = f"rt_button_test3.png")
button_test3 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_test3_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_test3.place(
    x = 385, y = 403,
    width = 490,
    height = 85)

#Label: Test 3 point
label_t3 = Label(
    text = 0,
    font = ("Lilita One", 44),
    fg = "#EDDBDB",
    bg = "#F12711")

label_t3.place(
    x = 898, y = 411,
    width = 185,
    height = 60)


# Button: Test 4
button_test4_img = PhotoImage(file = f"rt_button_test4.png")
button_test4 = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_test4_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_test4.place(
    x = 385, y = 498,
    width = 490,
    height = 85)

#Label: Test 4 point
label_t4 = Label(
    text = 0,
    font = ("Lilita One", 44),
    fg = "#EDDBDB",
    bg = "#F12711")

label_t4.place(
    x = 898, y = 506,
    width = 185,
    height = 60)


window.resizable(False, False)
window.mainloop()