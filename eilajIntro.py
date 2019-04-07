def intro(questions, answers):
    print('Hello! I am Lily, your special representative from red cross. This is a fun game to get a sense of how you are feeling,')
    print('How was your trip:\nA. Good\nB. Bad\nC. Okay')
    x = input('Type letter: ')
    while True:
        if x.find('A') != -1 or x.find('a') != -1:
            answers.append('Good')
            break
        elif x.find('B') != -1 or x.find('b') != -1:
            answers.append('Bad')
            break
        elif x.find('C') != -1 or x.find('c') != -1:
            answers.append('Okay')
            break
        else:
            print("Please choose between A, B, and C.")
            x = input('Type letter: ')
    questions.append('How was your trip?')
    print('Are you alone?\nA. Yes\nB. No')
    x = input('Type letter: ')
    if x.find('A') != -1 or x.find('a') != -1:
        answers.append('Yes')
    elif x.find('B') != -1 or x.find('b') != -1:
        answers.append('No')
    elif x.upper() not in "AB":
        print("Please choose between A and B.")
        x = input('Type letter: ')
    questions.append('Are you alone?')