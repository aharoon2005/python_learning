import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
import sys

class CatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Be My Valentine")

        if getattr(sys, 'frozen', False):
            script_dir = sys._MEIPASS
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))

        self.cat_image = ImageTk.PhotoImage(Image.open(os.path.join(script_dir, "img24gu05lfb1.png")))
        self.happy_cat_image = ImageTk.PhotoImage(Image.open(os.path.join(script_dir, "sticker.png")))

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()
        self.cat_item = self.canvas.create_image(200, 200, image=self.cat_image)

        self.text_item = self.canvas.create_text(200, 350, text="Please pet the cat!", font=("Arial", 16), fill="black")

        self.canvas.tag_bind(self.cat_item, "<Button-1>", self.ask_valentine)

    def ask_valentine(self, event):
        response = messagebox.askyesno("Valentine", "Will you be my Valentine?")
        if response:
            self.canvas.itemconfig(self.cat_item, image=self.happy_cat_image)
            self.canvas.delete(self.text_item)
            self.shoot_confetti()

    def shoot_confetti(self):
        for _ in range(100):
            x = random.randint(0, 400)
            y = random.randint(0, 400)
            color = random.choice(["red", "green", "blue", "yellow", "purple", "orange"])
            self.canvas.create_oval(x, y, x+5, y+5, fill=color, outline=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = CatApp(root)
    root.mainloop()