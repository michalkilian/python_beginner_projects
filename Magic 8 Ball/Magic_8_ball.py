from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import random


class MagicBall(Tk):
    LABEL_TEXT = "ASK MAGIC BALL ANYTHING"
    answers = ["It is certain.", "It is decidedly so.", "Without a doubt.",
               "Yes - definitely.", "You may rely on it", "As I see it, yes.",
               "Most likely.", "Outlook good.", "Yes", "Signs point to yes",
               "Reply hazy, try again", "Ask again later.",
               "Can't predict now.", "Better not tell you now.",
               "Concentrate and ask again.", "Don't count on it.",
               "My reply is no", "My sources say no",
               "Outlook not so good.", "Very doubtful."]

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "Magic 8 Ball")

        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT)
        self.label = Label(self, textvariable=self.label_text)
        self.label.grid(row=0)

        path = "Magic_ball.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(self, image=img)
        panel.image = img
        panel.grid(row=1)

        self.ask_button = Button(self, text="Ask", command=self.ask)
        self.ask_button.grid(row=2, sticky=W)

        self.question_entry = Entry(self)
        self.question_entry.grid(row=2, column=0)
        self.question_entry.focus_set()

        self.close_button = Button(self, text="Close",
                                   command=self.quit)
        self.close_button.grid(row=3)

    def ask(self):
        if self.question_entry.get():
            self.label_text.set("Thinking...")
            time.sleep(0.1)
            self.update()
            time.sleep(2.9)
            messagebox.showinfo("Answer", self.answers[random.randint(0, 19)])
            self.label_text.set(self.LABEL_TEXT)
            self.question_entry.delete(0, END)


app = MagicBall()
app.mainloop()
