from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
IMG_PATH = 'images/'


class FlashyView:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=60, bg=BACKGROUND_COLOR)

        # Images needs to assigned to a member variables or else they get destroyed
        self.card_back_img = PhotoImage(file=f"{IMG_PATH}card_back.png")
        self.card_front_img = PhotoImage(file=f"{IMG_PATH}card_front.png")
        self.right_img = PhotoImage(file=f"{IMG_PATH}right.png")
        self.wrong_img = PhotoImage(file=f"{IMG_PATH}wrong.png")

        self.create_widgets()

    def create_widgets(self):

        canvas = Canvas(self.window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
        canvas.create_image(0, 0, image=self.card_back_img, anchor="nw")
        canvas.create_image(0, 0, image=self.card_front_img, anchor="nw")
        canvas.grid(row=0, column=0, columnspan=2)

        # Create Card text
        title = Label(text="French", background="#fff", font=("Ariel", 40, "italic"))
        content = Label(text="trouve", background="#fff", font=("Ariel", 60, "bold"))

        # Add Labels to the grid
        title.grid(row=0, column=0, columnspan=2, sticky="n", pady="120")
        content.grid(row=0, column=0, columnspan=2)

        # Create Buttons
        wrong_btn = Button(image=self.wrong_img, highlightthickness=0, borderwidth=0)
        right_btn = Button(image=self.right_img, highlightthickness=0, borderwidth=0)

        # Add buttons to the grid
        wrong_btn.grid(row=1, column=0)
        right_btn.grid(row=1, column=1)
