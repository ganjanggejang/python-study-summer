class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # 0 ~ 11,  len() == 12
    def still_has_question(self):
        """
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        """
        # 같은 의미
        return self.question_number < len(self.question_list) # 결과값이 True of False이기 때문

    # 실행되면 사용자에게 질문하는 메서드
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (T/F) ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("정답!")
            self.score += 1
        else:
            print("오답!")

        print(f"Your current score is: {self.score}/{self.question_number}")

