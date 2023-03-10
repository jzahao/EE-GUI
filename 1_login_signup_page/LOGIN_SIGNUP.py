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
background_img = PhotoImage(file = f"bg_login_signup.png")
background = canvas.create_image(
    625.0, 325.0,
    image = background_img)


# Button About Us
button_abus_img = PhotoImage(file = f"logsign_button_abus.png")
button_abus = Button(
    activebackground = "#D8482E",
    bg = "#D8482E",
    image = button_abus_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_abus.place(
    x = 460, y = 483,
    width = 360,
    height = 65)


# Button Sign Up
button_signup_img = PhotoImage(file = f"logsign_button_signup.png")
button_signup = Button(
    activebackground = "#D6452C",
    bg = "#D6452C",
    image = button_signup_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_signup.place(
    x = 460, y = 408,
    width = 360,
    height = 65)


# Button Log In
button_login_img = PhotoImage(file = f"logsign_button_login.png")
button_login = Button(
    activebackground = "#D03D29",
    bg = "#D03D29",
    image = button_login_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_login.place(
    x = 460, y = 333,
    width = 360,
    height = 65)


window.resizable(False, False)
window.mainloop()