from tkinter import *
from tkinter import messagebox
from flashy_controller import FlashyController

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_COLOR = "#91C2AF"
IMG_PATH = 'images/'


class FlashyView:
    def __init__(self):
        self.controller = FlashyController()
        self.window = Tk()
        self.window.title(f"Flashy | {self.controller.get_word_count()} Words Left")
        self.window.config(padx=50, pady=60, bg=BACKGROUND_COLOR)

        # Images needs to assigned to a member variables or else they get destroyed
        self.card_back_img = PhotoImage(file=f"{IMG_PATH}card_back.png")
        self.card_front_img = PhotoImage(file=f"{IMG_PATH}card_front.png")
        self.right_img = PhotoImage(file=f"{IMG_PATH}right.png")
        self.wrong_img = PhotoImage(file=f"{IMG_PATH}wrong.png")

        self.create_widgets()
        self.card = None
        self.next_card()

    def create_widgets(self):

        self.canvas = Canvas(self.window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas_img = self.canvas.create_image(0, 0, image=self.card_front_img, anchor="nw")
        self.canvas.grid(row=0, column=0, columnspan=2)

        # Create Card text
        self.title = Label(text="Language", background="#fff", font=("Ariel", 40, "italic"))
        self.content = Label(text="word", background="#fff", font=("Ariel", 60, "bold"))

        # Add Labels to the grid
        self.title.grid(row=0, column=0, columnspan=2, sticky="n", pady="120")
        self.content.grid(row=0, column=0, columnspan=2)

        # Create Buttons
        self.wrong_btn = Button(image=self.wrong_img, highlightthickness=0, borderwidth=0, command=self.wrong_click)
        self.right_btn = Button(image=self.right_img, highlightthickness=0, borderwidth=0, command=self.right_click)

        # Add buttons to the grid
        self.wrong_btn.grid(row=1, column=0)
        self.right_btn.grid(row=1, column=1)

    def next_card(self):
        self.card = self.controller.get_random_card()
        text = ""
        content = "No more cards..."

        # check completion condition
        if self.card is None:
            messagebox.showinfo(message="Congratulations! You have learned all of the cards.")
        else:
            text = "French"
            content = self.card["French"]
            self.window.after(3000, self.flip_card)
        self.title.config(text=text, fg="black", background="white")
        self.content.config(text=content, fg="black", background="white")
        self.canvas.itemconfig(self.canvas_img, image=self.card_front_img)
        self.wrong_btn.config(state="disabled")
        self.right_btn.config(state="disabled")

    def flip_card(self):
        self.title.config(text="English", fg="white", background=CARD_BACK_COLOR)
        self.content.config(text=self.card['English'], fg="white", background=CARD_BACK_COLOR)
        self.canvas.itemconfig(self.canvas_img, image=self.card_back_img)
        self.wrong_btn.config(state="normal")
        self.right_btn.config(state="normal")

    def right_click(self):
        self.controller.remove_card(self.card)
        self.window.title(f"Flashy | {self.controller.get_word_count()} Words Left")
        self.next_card()

    def wrong_click(self):
        self.next_card()
