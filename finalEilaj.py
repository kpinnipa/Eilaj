from eilaj import*
from eilajIntro import*
from health_center import health_center


questions = []
answers = []
intro()
t = playground = healthCenter = foodCenter = 0
print('Here is a map of the camp. You are able to visit the playground, the health center, or the cafeteria.')
while t < 3:
    print('Where would you like to go?: \nA. Playground \nB. Health Center\nC. Cafeteria')
    x = input('Pick a letter: ')
    if playground == 0 and x.find('a') != -1:
        playground()
        playground += 1
        t+=1
    elif healthCenter == 0 and x.find('b') != -1:
        health_center()
        healthCenter += 1
        t+=1
    elif foodCenter == 0 and x.find('c') != -1:
        foodCenter()
        foodCenter += 1
        t+=1
    elif x.find('a') == -1 and x.find('b') == -1 and x.find('c') == -1:
        print('Please type a, b, or c)
    else:
        print('You have already gone there.')
while 1==1:
    print('Thank you so much for hanging out today!! Do you have a code')
    x = input('Yes or No: ')
    if x.find('Yes') != -1:
        print('under construction')
        break
    elif x.find('No') != -1:
        print('Continue to meet with therapist')
        break
    else:
        print('Incorrect response')
print(questions)
print(answers)
