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
background_img = PhotoImage(file = f"bg_login.png")
background = canvas.create_image(
    625.0, 325.0,
    image = background_img)


entry_img = PhotoImage(file = f"login_textbox.png")

# TextBox: Username
entry_username_bg = canvas.create_image(
    625.0, 295.0,
    image = entry_img)

entry_username = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_username.place(
    x = 420, y = 272,
    width = 400,
    height = 40)


# TextBox: Password
entry_password_bg = canvas.create_image(
    625.0, 378.0,
    image = entry_img)

entry_password = Entry(
    font = ("cambria", 14, "italic"),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#535353",
    highlightthickness = 0)

entry_password.place(
    x = 420, y = 356,
    width = 400,
    height = 40)


# Button: Log In
button_login_img = PhotoImage(file = f"login_button_login.png")
button_login = Button(
    activebackground = "#983493",
    bg = "#983493",
    image = button_login_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_login.place(
    x = 532, y = 440,
    width = 200,
    height = 65)


# Button: Back
button_back_img = PhotoImage(file = f"login_button_back.png")
button_back = Button(
    activebackground = "#89399D",
    bg = "#89399D",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 590, y = 542,
    width = 71,
    height = 71)


window.resizable(False, False)
window.mainloop()