button_card_font = Button(
        text = "cat",
        font = ("Firasan", 34, "bold", "italic"),
        fg = "#F2F2F2",
        activeforeground = "#F2F2F2",
        compound = "center",
        activebackground = "#EDDBDB",
        bg = "#EDDBDB",
        image = button_card_front_img,
        borderwidth = 0,
        highlightthickness = 0,
        command = change_back_face,
        relief = "flat")