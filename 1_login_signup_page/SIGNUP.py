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
background_img = PhotoImage(file = f"bg_signup.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


entry_img = PhotoImage(file = f"signup_textbox.png")

# Textbox: Your full name
entry_YFN_bg = canvas.create_image(
    390.0, 247.0,
    image = entry_img)

entry_YFN = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_YFN.place(
    x = 187, y = 224,
    width = 400,
    height = 40)


# Textbox: Date of birth
entry_DOB_bg = canvas.create_image(
    390.0, 330.5,
    image = entry_img)

entry_DOB = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_DOB.place(
    x = 187, y = 308,
    width = 400,
    height = 40)


# Textbox: Your email
entry_YE_bg = canvas.create_image(
    390.0, 414.5,
    image = entry_img)

entry_YE = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_YE.place(
    x = 187, y = 392,
    width = 400,
    height = 40)


# Textbox: Username
entry_USN_bg = canvas.create_image(
    860.0, 247.0,
    image = entry_img)

entry_USN = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_USN.place(
    x = 657, y = 224,
    width = 400,
    height = 40)


# Textbox: Password
entry_PW_bg = canvas.create_image(
    860.0, 330.5,
    image = entry_img)

entry_PW = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_PW.place(
    x = 657, y = 308,
    width = 400,
    height = 40)


# Textbox: Re-enter password
entry_RPW_bg = canvas.create_image(
    860.0, 414.5,
    image = entry_img)

entry_RPW = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_RPW.place(
    x = 657, y = 392,
    width = 400,
    height = 40)


# Button: Sign Up
button_signup_img = PhotoImage(file = f"signup_button_signup.png")
button_signup = Button(
    activebackground = "#2FDB81",
    bg = "#2FDB81",
    image = button_signup_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_signup.place(
    x = 532, y = 469,
    width = 195,
    height = 65)


# Button: Back
button_back_img = PhotoImage(file = f"signup_button_back.png")
button_back = Button(
    activebackground = "#34E67F",
    bg = "#34E67F",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 591, y = 559,
    width = 71,
    height = 71)


window.resizable(False, False)
window.mainloop()