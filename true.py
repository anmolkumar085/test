from question_model import *
from data import *
from quiz_brain import *
from prettytable import *

shuffle_object = Dara_1(bank, bank2)
pretty_object = PrettyTable()

question_bank = []
data = shuffle_object.order()
for i in data:
    k = Question(i["question"], i["correct_answer"])
    question_bank.append(k)

quiz = Quiz(question_bank)

while quiz.next_question():
    quiz.print1()
    quiz.check_answer()

pretty_object.add_column("Serial No.", quiz.sr_list1)
pretty_object.add_column("Questions", quiz.question_list1)
pretty_object.add_column("Your Answer", quiz.answer_list1)
pretty_object.add_column("Correct Answer", quiz.real_ans_list1)
pretty_object.add_column(" ", quiz.true_false_list1)

print("you have completed the quiz")
print(f"Your final score is {quiz.score}/{len(data)}")

print(pretty_object)
