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

background_img = PhotoImage(file = f"bg_shortstory_story.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Label: Story Name
label_story_name = Label(
    text = "The lion and the rabbit",
    font = ("Lilita One", 44),
    bg = "#03303F",
    fg = "#F2F2F2")

label_story_name.place(
    x = 213, y = 51,
    width = 824,
    height = 50)


# Button: Back
button_back_img = PhotoImage(file = f"shortstory_button_back.png")
button_back = Button(
    activebackground = "#F2F2F2",
    bg = "#F2F2F2",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 928, y = 567,
    width = 45,
    height = 45)


# Button: Next
button_next_img = PhotoImage(file = f"shortstory_button_next.png")
button_next = Button(
    activebackground = "#F2F2F2",
    bg = "#F2F2F2",
    image = button_next_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_next.place(
    x = 1091, y = 567,
    width = 45,
    height = 45)


# Button: Menu
button_menu_img = PhotoImage(file = f"shortstory_button_menu.png")
button_menu = Button(
    activebackground = "#F2F2F2",
    bg = "#F2F2F2",
    image = button_menu_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_menu.place(
    x = 982, y = 567,
    width = 45,
    height = 45)


# Button: List
button_list_img = PhotoImage(file = f"shortstory_button_list.png")
button_list = Button(
    activebackground = "#F2F2F2",
    bg = "#F2F2F2",
    image = button_list_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_list.place(
    x = 1037, y = 567,
    width = 45,
    height = 45)


window.resizable(False, False)
window.mainloop()