class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)? ")
        self.check_answer(user_answer, question.answer)

    def has_more_questions(self):
        return self.question_number < len(self.questions_list)
    
    def check_answer(self, user_answer, correct_answer):
        total = len(self.questions_list)
        if user_answer.lower() == correct_answer.lower() or user_answer.lower()[0] == correct_answer.lower()[0]:
            self.score += 1
            print(f"Correct! \nScore: {self.score}/{total}\n")
        else:
            print(f"Wrong! \nScore: {self.score}/{total}\n")
        