import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = tkinter.Label(
            text=f"Score: {self.quiz.score}", font=('Arial', 20, 'italic'),
            bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(bg='white', height=250, width=300)
        self.question_text = self.canvas.create_text(
            150, 125, text="", width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, rowspan=2)

        true_img = tkinter.PhotoImage(file="images/true.png")
        self.true_button = tkinter.Button(
            image=true_img, bg=THEME_COLOR, height=100, width=100,
            highlightthickness=0,
            command=self.true_pressed)
        self.true_button.grid(column=0, row=3)

        false_img = tkinter.PhotoImage(file="images/false.png")
        self.false_button = tkinter.Button(
            image=false_img, bg=THEME_COLOR, height=100, width=100,
            highlightthickness=0,
            command=self.false_pressed)
        self.false_button.grid(column=1, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
        else:
            q_text = "You've Reached The End of The Quiz."
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        print(self.quiz.score)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.new_question)

    def new_question(self):
        self.label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()
