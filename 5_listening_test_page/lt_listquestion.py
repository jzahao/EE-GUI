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
background_img = PhotoImage(file = f"bg_lt_listquestion.png")
background = canvas.create_image(
    625.0, 325.0,
    image=background_img)


# Label: TEST 1
label_nametest = Label(
    text = "TEST 1",
    font = ("Lilita One", 68),
    fg = "#F25414",
    bg = "#EDDBDB")

label_nametest.place(
    x = 361, y = 22,
    width = 530,
    height = 88)


# Label: Score
label_score = Label(
    text = 1000,
    font = ("Quicksand Light", 44),
    fg = "#F12711",
    bg = "#EDDBDB")

label_score.place(
    x = 800, y = 542,
    width = 230,
    height = 60)


# Button: Your wrong answers
button_ywa_img = PhotoImage(file = f"lt_button_ywa.png")
button_ywa = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_ywa_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_ywa.place(
    x = 190, y = 538,
    width = 585,
    height = 85),


# Button: 100 button question
img = PhotoImage(file = f"lt_button_question.png")
img_true = PhotoImage(file = f"lt_button_true.png")
img_false = PhotoImage(file = f"lt_button_false.png")

b1 = Button(text = 1, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 190, y = 126,
    width = 50,
    height = 50)

b2 = Button(text = 2, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 249, y = 126,
    width = 50,
    height = 50)

b3 = Button(text = 3, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 308, y = 126,
    width = 50,
    height = 50)

b4 = Button(text = 4, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 367, y = 126,
    width = 50,
    height = 50)

b5 = Button(text = 5, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 426, y = 126,
    width = 50,
    height = 50)

b6 = Button(text = 6, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 485, y = 126,
    width = 50,
    height = 50)

b7 = Button(text = 7, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 544, y = 126,
    width = 50,
    height = 50)

b8 = Button(text = 8, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 603, y = 126,
    width = 50,
    height = 50)

b9 = Button(text = 9, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 662, y = 126,
    width = 50,
    height = 50)

b10 = Button(text = 10, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 721, y = 126,
    width = 50,
    height = 50)

b11 = Button(text = 11, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 780, y = 126,
    width = 50,
    height = 50)

b12 = Button(text = 12, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 839, y = 126,
    width = 50,
    height = 50)

b13 = Button(text = 13, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 898, y = 126,
    width = 50,
    height = 50)

b14 = Button(text = 14, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b14.place(
    x = 957, y = 126,
    width = 50,
    height = 50)

b15 = Button(text = 15, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b15.place(
    x = 1016, y = 126,
    width = 50,
    height = 50)

b16 = Button(text = 16, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b16.place(
    x = 190, y = 185,
    width = 50,
    height = 50)

b17 = Button(text = 17, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b17.place(
    x = 249, y = 185,
    width = 50,
    height = 50)

b18 = Button(text = 18, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b18.place(
    x = 308, y = 185,
    width = 50,
    height = 50)

b19 = Button(text = 19, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b19.place(
    x = 367, y = 185,
    width = 50,
    height = 50)

b20 = Button(text = 20, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b20.place(
    x = 426, y = 185,
    width = 50,
    height = 50)

b21 = Button(text = 21, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b21.place(
    x = 485, y = 185,
    width = 50,
    height = 50)

b22 = Button(text = 22, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b22.place(
    x = 544, y = 185,
    width = 50,
    height = 50)

b23 = Button(text = 23, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b23.place(
    x = 603, y = 185,
    width = 50,
    height = 50)

b24 = Button(text = 24, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b24.place(
    x = 662, y = 185,
    width = 50,
    height = 50)

b25 = Button(text = 25, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b25.place(
    x = 721, y = 185,
    width = 50,
    height = 50)

b26 = Button(text = 26, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b26.place(
    x = 780, y = 185,
    width = 50,
    height = 50)

b27 = Button(text = 27, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b27.place(
    x = 839, y = 185,
    width = 50,
    height = 50)

b28 = Button(text = 28, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b28.place(
    x = 898, y = 185,
    width = 50,
    height = 50)

b29 = Button(text = 29, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b29.place(
    x = 957, y = 185,
    width = 50,
    height = 50)

b30 = Button(text = 30, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b30.place(
    x = 1016, y = 185,
    width = 50,
    height = 50)

b31 = Button(text = 31, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b31.place(
    x = 190, y = 244,
    width = 50,
    height = 50)

b32 = Button(text = 32, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b32.place(
    x = 249, y = 244,
    width = 50,
    height = 50)

b33 = Button(text = 33, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b33.place(
    x = 308, y = 244,
    width = 50,
    height = 50)

b34 = Button(text = 34, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b34.place(
    x = 367, y = 244,
    width = 50,
    height = 50)

b35 = Button(text = 35, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b35.place(
    x = 426, y = 244,
    width = 50,
    height = 50)

b36 = Button(text = 36, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b36.place(
    x = 485, y = 244,
    width = 50,
    height = 50)

b37 = Button(text = 37, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b37.place(
    x = 544, y = 244,
    width = 50,
    height = 50)

b38 = Button(text = 38, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b38.place(
    x = 603, y = 244,
    width = 50,
    height = 50)

b39 = Button(text = 39, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b39.place(
    x = 662, y = 244,
    width = 50,
    height = 50)

b40 = Button(text = 40, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b40.place(
    x = 721, y = 244,
    width = 50,
    height = 50)

b41 = Button(text = 41, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b41.place(
    x = 780, y = 244,
    width = 50,
    height = 50)

b42 = Button(text = 42, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b42.place(
    x = 839, y = 244,
    width = 50,
    height = 50)

b43 = Button(text = 43, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b43.place(
    x = 898, y = 244,
    width = 50,
    height = 50)

b44 = Button(text = 44, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b44.place(
    x = 957, y = 244,
    width = 50,
    height = 50)

b45 = Button(text = 45, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b45.place(
    x = 1016, y = 244,
    width = 50,
    height = 50)

b46 = Button(text = 46, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b46.place(
    x = 190, y = 303,
    width = 50,
    height = 50)

b47 = Button(text = 47, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b47.place(
    x = 249, y = 303,
    width = 50,
    height = 50)

b48 = Button(text = 48, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b48.place(
    x = 308, y = 303,
    width = 50,
    height = 50)

b49 = Button(text = 49, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b49.place(
    x = 367, y = 303,
    width = 50,
    height = 50)

b50 = Button(text = 50, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b50.place(
    x = 426, y = 303,
    width = 50,
    height = 50)

b51 = Button(text = 51, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b51.place(
    x = 485, y = 303,
    width = 50,
    height = 50)

b52 = Button(text = 52, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b52.place(
    x = 544, y = 303,
    width = 50,
    height = 50)

b53 = Button(text = 53, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b53.place(
    x = 603, y = 303,
    width = 50,
    height = 50)

b54 = Button(text = 54, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b54.place(
    x = 662, y = 303,
    width = 50,
    height = 50)

b55 = Button(text = 55, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b55.place(
    x = 721, y = 303,
    width = 50,
    height = 50)

b56 = Button(text = 56, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b56.place(
    x = 780, y = 303,
    width = 50,
    height = 50)

b57 = Button(text = 57, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b57.place(
    x = 839, y = 303,
    width = 50,
    height = 50)

b58 = Button(text = 58, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b58.place(
    x = 898, y = 303,
    width = 50,
    height = 50)

b59 = Button(text = 59, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b59.place(
    x = 957, y = 303,
    width = 50,
    height = 50)

b60 = Button(text = 60, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b60.place(
    x = 1016, y = 303,
    width = 50,
    height = 50)

b61 = Button(text = 61, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b61.place(
    x = 190, y = 362,
    width = 50,
    height = 50)

b62 = Button(text = 62, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b62.place(
    x = 249, y = 362,
    width = 50,
    height = 50)

b63 = Button(text = 63, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b63.place(
    x = 308, y = 362,
    width = 50,
    height = 50)

b64 = Button(text = 64, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b64.place(
    x = 367, y = 362,
    width = 50,
    height = 50)

b65 = Button(text = 65, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b65.place(
    x = 426, y = 362,
    width = 50,
    height = 50)

b66 = Button(text = 66, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b66.place(
    x = 485, y = 362,
    width = 50,
    height = 50)

b67 = Button(text = 67, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b67.place(
    x = 544, y = 362,
    width = 50,
    height = 50)

b68 = Button(text = 68, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b68.place(
    x = 603, y = 362,
    width = 50,
    height = 50)

b69 = Button(text = 69, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b69.place(
    x = 662, y = 362,
    width = 50,
    height = 50)

b70 = Button(text = 70, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b70.place(
    x = 721, y = 362,
    width = 50,
    height = 50)

b71 = Button(text = 71, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b71.place(
    x = 780, y = 362,
    width = 50,
    height = 50)

b72 = Button(text = 72, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b72.place(
    x = 839, y = 362,
    width = 50,
    height = 50)

b73 = Button(text = 73, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b73.place(
    x = 898, y = 362,
    width = 50,
    height = 50)

b74 = Button(text = 74, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b74.place(
    x = 957, y = 362,
    width = 50,
    height = 50)

b75 = Button(text = 75, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b75.place(
    x = 1016, y = 362,
    width = 50,
    height = 50)

b76 = Button(text = 76, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b76.place(
    x = 190, y = 421,
    width = 50,
    height = 50)

b77 = Button(text = 77, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b77.place(
    x = 249, y = 421,
    width = 50,
    height = 50)

b78 = Button(text = 78, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b78.place(
    x = 308, y = 421,
    width = 50,
    height = 50)

b79 = Button(text = 79, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b79.place(
    x = 367, y = 421,
    width = 50,
    height = 50)

b80 = Button(text = 80, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b80.place(
    x = 426, y = 421,
    width = 50,
    height = 50)

b81 = Button(text = 81, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b81.place(
    x = 485, y = 421,
    width = 50,
    height = 50)

b82 = Button(text = 82, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b82.place(
    x = 544, y = 421,
    width = 50,
    height = 50)

b83 = Button(text = 83, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b83.place(
    x = 603, y = 421,
    width = 50,
    height = 50)

b84 = Button(text = 84, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b84.place(
    x = 662, y = 421,
    width = 50,
    height = 50)

b85 = Button(text = 85, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b85.place(
    x = 721, y = 421,
    width = 50,
    height = 50)

b86 = Button(text = 86, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b86.place(
    x = 780, y = 421,
    width = 50,
    height = 50)

b87 = Button(text = 87, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b87.place(
    x = 839, y = 421,
    width = 50,
    height = 50)

b88 = Button(text = 88, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b88.place(
    x = 898, y = 421,
    width = 50,
    height = 50)

b89 = Button(text = 89, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b89.place(
    x = 957, y = 421,
    width = 50,
    height = 50)

b90 = Button(text = 90, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b90.place(
    x = 1016, y = 421,
    width = 50,
    height = 50)

b91 = Button(text = 91, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b91.place(
    x = 190, y = 480,
    width = 50,
    height = 50)

b92 = Button(text = 92, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b92.place(
    x = 249, y = 480,
    width = 50,
    height = 50)

b93 = Button(text = 93, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b93.place(
    x = 308, y = 480,
    width = 50,
    height = 50)

b94 = Button(text = 94, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b94.place(
    x = 367, y = 480,
    width = 50,
    height = 50)

b95 = Button(text = 95, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b95.place(
    x = 426, y = 480,
    width = 50,
    height = 50)

b96 = Button(text = 96, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b96.place(
    x = 485, y = 480,
    width = 50,
    height = 50)

b97 = Button(text = 97, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b97.place(
    x = 544, y = 480,
    width = 50,
    height = 50)

b98 = Button(text = 98, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b98.place(
    x = 603, y = 480,
    width = 50,
    height = 50)

b99 = Button(text = 99, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b99.place(
    x = 662, y = 480,
    width = 50,
    height = 50)

b100 = Button(text = 100, font = ("firasan", 13, "bold"), fg = "white", compound = "center", activeforeground = "white",
    activebackground = "#EDDBDB", bg = "#EDDBDB", image = img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b100.place(
    x = 721, y = 480,
    width = 50,
    height = 50)


# Button: Back
button_back_img = PhotoImage(file = f"lt_button_back_1.png")
button_back = Button(
    activebackground = "#EDDBDB",
    bg = "#EDDBDB",
    image = button_back_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

button_back.place(
    x = 54, y = 318,
    width = 80,
    height = 80)


window.resizable(False, False)
window.mainloop()