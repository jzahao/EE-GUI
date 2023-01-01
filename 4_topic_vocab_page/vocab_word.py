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
background_img = PhotoImage(file = f"bg_topicvocab_word.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Button: Audio
button_audio_img = PhotoImage(file = f"topicvocab_button_audio.png")
button_audio = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_audio_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_audio.place(
    x = 180, y = 141,
    width = 127,
    height = 127)


# Button: Back
button_back_img = PhotoImage(file = f"topicvocab_button_back_2.png")
button_back = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 119, y = 586,
    width = 55,
    height = 55)


# Button: Next
button_next_img = PhotoImage(file = f"topicvocab_button_next.png")
button_next = Button(
    activebackground = "#D92167",
    bg = "#D2236B",
    image = button_next_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_next.place(
    x = 309, y = 586,
    width = 55,
    height = 55)


# Button: List
button_list_img = PhotoImage(file = f"topicvocab_button_list.png")
button_list = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_list_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_list.place(
    x = 245, y = 586,
    width = 55,
    height = 55)


# Button: Menu
button_menu_img = PhotoImage(file = f"topicvocab_button_menu_2.png")
button_menu = Button(
    activebackground = "#D92167",
    bg = "#D92167",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 182, y = 586,
    width = 55,
    height = 55)


# Label: Word
label_word = Label(
    text = "abide by", 
    font = ("Firasan", 44, "bold"),
    fg = "#CF246E",
    bg = "#F2F2F2")

label_word.place(
    x = 85, y = 35,
    width = 1079,
    height = 74)


# Label: Pronunciation
label_pronoun = Label(
    text = "/ə'baid bai/", 
    font = ("Quicksand", 34, "bold"),
    fg = "#000000",
    bg = "#F2F2F2")

label_pronoun.place(
    x = 509, y = 150,
    width = 655,
    height = 60)


# Label: Word type
label_wordtype = Label(
    text = "verb", 
    font = ("Firasan", 28, "bold"),
    fg = "#CF246E",
    bg = "#F2F2F2")

label_wordtype.place(
    x = 509, y = 247,
    width = 655,
    height = 46)


# Label: Vietnamese
label_vi = Label(
    text = "tuân theo, tuân thủ", 
    font = ("Cambria", 24, "bold", "italic"),
    anchor = "w",
    justify = "left",
    fg = "#000000",
    bg = "#F2F2F2")

label_vi.place(
    x = 704, y = 330,
    width = 460,
    height = 71)


# Label: Synonyms
label_syn = Label(
    text = ("to comply with; to conform; adhere to; observe"), 
    font = ("Cambria", 20, "italic"),
    anchor = "nw",
    justify = "left",
    wraplength = 340,
    fg = "#000000",
    bg = "#F2F2F2")

label_syn.place(
    x = 78, y = 340,
    width = 352,
    height = 193)


# Label: Example
label_exp = Label(
    text = ("After reading the contract, I was still unable to determine if our company was liable for back wages."), 
    font = ("Cambria", 20, "italic"),
    anchor = "nw",
    justify = "left",
    wraplength = 650,
    fg = "#000000",
    bg = "#F2F2F2")

label_exp.place(
    x = 509, y = 486,
    width = 655,
    height = 120)


window.resizable(False, False)
window.mainloop()