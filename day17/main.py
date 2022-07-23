from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
total = 0
question_number = 1
print("Welcome to quiz.")
for chosen in question_bank:
    student_answer = input(f"Q.{question_number}: {chosen.text} (True/False)?: ")
    question_number += 1
    if student_answer == chosen.answer:
        total += 1

print(f"Quiz iz finish your total score is: {total}")

