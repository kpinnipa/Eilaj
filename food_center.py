def food_center(questions, answers):
    questions2 = ("Are you often hungry?\n", "Do you have a good appetite?\n")
    answers2 = [("A. Yes", "B. No", "C. Maybe"), ("A. Yes", "B. No", "C. Mainly")]
    #result = []
    counter = 0
    while counter < len(questions2):
        print(questions2[counter])
        questions.append(questions2[counter])
        print_list(answers2[counter])
        answer = input()
        try:
            index = translate(answer)
            answers.append(answers2[counter][index][3:])
        except IndexError:
            print("I'm sorry but can you say that again? I didn't quite get what you were saying.")
            continue
        counter += 1




def translate(answer):
        list = ["A", "B", "C", "D", "E", "F", "G"]
        index = list.index(answer.upper())
        return index



def print_list(list):
    for i in list:
        print(i)