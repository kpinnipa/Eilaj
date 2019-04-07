## Health Center
def health_center(questions, answers):
    print("Hello! My name is Aliya and I am the nurse at this station! Do you have any physical injuries?")
    question1 = "Do you have any physical injuries?"
    questions.append(question1)
    print("A: Yes\nB: No")
    while True:
        user = input("Please select A or B: ")
        if user.upper() not in "AB":
            continue
        elif user.upper() == "A":
            answers.append("Yes")
            break
        elif user.upper() == "B":
            answers.append("No")
            break
    print("Are you able to fall asleep at night?")
    question2 = "Are you able to fall asleep at night?"
    questions.append(question2)
    print("A: Yes\nB: No\nC: Mostly")
    while True:
        user2 = input("Please select A, B, or C: ")
        if user2.upper() not in "ABC":
            continue
        elif user2.upper() == "A":
            answers.append("Yes")
            break
        elif user2.upper() == "B":
            answers.append("No")
            break
        elif user2.upper() == "C":
            answers.append("Mostly")
            break
    print("When was the last time you were here?")
    question3 = "When was the last time you were here?"
    questions.append(question3)
    print("A: Never\nB: Recently\nC: A while ago")
    while True:
        user3 = input("Please choose A, B, or C: ")
        if user3.upper() not in "ABC":
            continue
        elif user3.upper() == "A":
            answers.append("Never")
            break
        elif user3.upper() == "B":
            answers.append("Recently")
            break
        elif user3.upper() == "C":
            answers.append("A while ago")
            break
    print("Would you like to talk to anyone about anything?")
    question3 = "Would you like to talk to anyone about anything?"
    questions.append(question3)
    print("A: Yes\nB: No")
    while True:
        user4 = input("Please choose A or B: ")
        if user4.upper() not in "AB":
            continue
        elif user4.upper() == "A":
            answers.append("Yes")
            break
        elif user4.upper() == "B":
            answers.append("No")
            break

