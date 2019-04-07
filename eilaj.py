# Playground conversation


def main():
    questions = ("Do you have other friends here?\n", "How often do you play here?\n")
    answers = [("A. Yes", "B. No"), ("A. All the time", "B. Never", "C. Sometimes")]
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
    #print(result)




def translate(answer):
        list = ["A", "B", "C", "D", "E", "F", "G"]
        index = list.index(answer)
        return index



def print_list(list):
    for i in list:
        print(i)



if __name__ == "__main__":
    main()