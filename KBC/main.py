from questions import questions, answers
winning_amount = 0
for question, answer in zip(questions,answers):
    q = question.split("?")
    print(q[0]+"?")
    options = q[1].split(",")
    for option in options:
        print(option)
    user_answer = input()
    if user_answer == answer:
        winning_amount+=50000
        print("That's the right answer!!!")
        print()
    else:
        print("That's the wrong answer, the correct answer is: ",answer)
        print()
        break


print("Thank you for playing the game, your final winning amount is: ",winning_amount)
