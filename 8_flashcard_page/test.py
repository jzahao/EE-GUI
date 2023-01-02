from tkinter import *

window = Tk()

window.geometry("1250x650")
window.configure(bg = "#FFFFFF")

wrap = LabelFrame(window)

myCanvas = Canvas(wrap, bg = "#EDDBDB", width=700, height=400)
myCanvas.pack(side = LEFT)

# canvas = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 780,
#     width = 1500,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge")
# canvas.place(x = 0, y = 0)

# Background
# background_img = PhotoImage(file = f"bg_flashcard_listword.png")
# background = canvas.create_image(
#     625.0, 325.0,
#     image=background_img)

xscrollbar = Scrollbar(wrap, orient = "vertical", command = myCanvas.yview)
xscrollbar.pack(side = BOTTOM, fill = "x")

myCanvas.configure(yscrollcommand=xscrollbar.set)

myFrame = Frame(myCanvas)
myCanvas.create_window((0,0), window=myFrame, anchor="nw")

myCanvas.bind('<Configure>', lambda e:myCanvas.configure(scrollregion=myCanvas.bbox('all')))

wrap.place(x = 200, y = 100, width=700, height=450)

for i in range(50):
    Button(myFrame, text = i).pack()

window.resizable(False, False)
window.mainloop()