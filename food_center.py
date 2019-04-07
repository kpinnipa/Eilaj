# Playground conversation


def main():
    questions = ("Are you often hungry?\n", "Do you have a good appetite?\n")
    answers = [("A. Yes", "B. No", "C. Maybe"), ("A. Yes", "B. No", "C. Mainly")]
    result = []
    counter = 0
    while counter < len(questions):
        print(questions[counter])
        print_list(answers[counter])
        answer = input()
        try:
            index = translate(answer)
            result.append(answers[counter][index][3:])
        except IndexError:
            print("I'm sorry but can you say that again? I didn't quite get what you were saying.")
            continue
        counter += 1




def translate(answer):
        list = ["A", "B", "C", "D", "E", "F", "G"]
        index = list.index(answer)
        return index



def print_list(list):
    for i in list:
        print(i)

