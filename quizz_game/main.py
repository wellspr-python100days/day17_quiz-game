from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

#token_request = requests.get("https://opentdb.com/api_token.php?command=request")
#token = token_request.json()
#print(token)

amount = 10
difficulty = '' #'easy' | 'medium' | 'hard'

url = f"https://opentdb.com/api.php?type=boolean&amount={amount}&category=18"
if difficulty:
    url += f"&difficulty={difficulty}"

r = requests.get(url)

response = r.json()
response_code = response['response_code']

if response_code > 0:
    print(response_code)

question_bank = []
results = response['results']

for entry in results:
    text = entry['question']
    answer = entry['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

brain = QuizBrain(question_bank)

while brain.has_more_questions():
    brain.next_question()

print("You've completed the quiz.")

print(f"Your final score was {brain.score}/{len(brain.questions_list)}")