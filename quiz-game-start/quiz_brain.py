
class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0
    def still_has_questions(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, current_answer, user_answer):

        if current_answer.lower() == user_answer.lower():
            print("you got it right!")
            self.score += 1

        else:
            print("you got the Wrong!")
        print(f"The Right Answer is {current_answer}")
        print(f"your score is {self.score}/{self.question_no}")
