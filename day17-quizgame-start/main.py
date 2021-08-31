from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# 문제와 답이 있는 데이터를 question_bank 리스트에 옮겨담음
question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"], i["answer"]))

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number}")
