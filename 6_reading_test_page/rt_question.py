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
background_img = PhotoImage(file = f"bg_rt_question.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Label: Title
label_title = Label(
    text = "TEST 1" + " - " + "Question 1",
    font = ("Quicksand", 28),
    fg = "#F36315",
    bg = "#F2F2F2")

label_title.place(
    x = 117, y = 46,
    width = 1025,
    height = 48)


# Label: Score
label_score = Label(
    text = 1000,
    font = ("Quicksand Light", 44),
    fg = "#F12C11",
    bg = "#EDDBDB")

label_score.place(
    x = 410, y = 540,
    width = 320,
    height = 58)


# Textbox: Question x = 117, y = 149, width = 665, height = 334


# Murti choice
button_A_img = PhotoImage(file = f"rt_button_A.png")
button_B_img = PhotoImage(file = f"rt_button_B.png")
button_C_img = PhotoImage(file = f"rt_button_C.png")
button_D_img = PhotoImage(file = f"rt_button_D.png")
button_A_click_img = PhotoImage(file = f"rt_button_A_click.png")
button_B_click_img = PhotoImage(file = f"rt_button_B_click.png")
button_C_click_img = PhotoImage(file = f"rt_button_C_click.png")
button_D_click_img = PhotoImage(file = f"rt_button_D_click.png")


# Button: Choose A
button_A = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_A_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

button_A.place(
    x = 833, y = 188,
    width = 170,
    height = 85)


# Button: Choose B
button_B = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_B_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

button_B.place(
    x = 1005, y = 188,
    width = 170,
    height = 85)


# Button: Choose C
button_C = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_C_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

button_C.place(
    x = 833, y = 275,
    width = 170,
    height = 85)


# Button: Choose D
button_D = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_D_img,
    borderwidth = 0,
    highlightthickness = 0,
    relief = "flat")

button_D.place(
    x = 1005, y = 275,
    width = 170,
    height = 85)


# Button: Back
button_back_img = PhotoImage(file = f"rt_button_back_2.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 890, y = 544,
    width = 70,
    height = 70)


# Button: Next
button_next_img = PhotoImage(file = f"rt_button_next.png")
button_next = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_next_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_next.place(
    x = 1050, y = 544,
    width = 80,
    height = 80)


# Button: List
button_list_img = PhotoImage(file = f"rt_button_list.png")
button_list = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_list_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_list.place(
    x = 970, y = 544,
    width = 70,
    height = 70)


# Button: Check
button_check_img = PhotoImage(file = f"rt_button_check.png")
button_check = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_check_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_check.place(
    x = 833, y = 433,
    width = 170,
    height = 85)

# Label: Answer
label_answer = Label(
    text = "A",
    font = ("Quicksand", 34, "bold"),
    fg = "#F12C11",
    bg = "#F2F2F2")

label_answer.place(
    x = 1023, y = 443,
    width = 126,
    height = 50)


window.resizable(False, False)
window.mainloop()