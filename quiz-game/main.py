from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    # print(Question(entry["text"], entry["answer"]))
    question_bank.append(Question(entry["question"], entry["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
