## Health Center
def health_center():
    print("Hello! My name is Aliya and I am the nurse at this station! Do you have any physical injuries?")
    question1 = "Do you have any physical injuries?"
    #questions.append(question1)
    print("A: Yes\nB: No")
    while True:
        user = input("Please select A or B: ")
        if user != "A" and user != "B":
            continue
        if user == "A":
            #answers.append("Yes")
            break
        if user == "B":
            #answers.append("No")
            break
    print("Are you able to fall asleep at night?")
    question2 = "Are you able to fall asleep at night?"
    #questions.append(question2)
    print("A: Yes\nB: No\nC: Mostly")
    while True:
        user2 = input("Please select A, B, or C: ")
        if user2 not in "ABC":
            continue
        if user2 == "A":
            # answers.append("Yes")
            break
        if user2 == "B":
            # answers.append("No")
            break
        if user2 == "C":
            # answers.append("Maybe")
            break
    print("When was the last time you were here?")
    question3 = "When was the last time you were here?"
    #questions.append(question3)
    print("A: Never\nB: Recently\nC: A while ago")
    while True:
        user3 = input("Please choose A, B, or C: ")
        if user3 not in "ABC":
            continue
        if user3 == "A":
            # answers.append("Never")
            break
        if user3 == "B":
            # answers.append("Recently")
            break
        if user3 == "C":
            # answers.append("A while ago")
            break
    print("Would you like to talk to anyone about anything?")
    question3 = "Would you like to talk to anyone about anything?"
    # questions.append(question3)
    print("A: Yes\nB: No")
    while True:
        user4 = input("Please choose A or B: ")
        if user4 != "A" and user4 != "B":
            continue
        if user4 == "A":
            #answers.append("Yes")
            break
        if user4 == "B":
            #answers.append("No")
            break
health_center()
