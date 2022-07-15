import random
from HigherOrLower_Art import logo, vs
from HigherOrLower_Data import data
import os


notUseNumbers = []
for num1 in range(0, 50):
    notUseNumbers.append(num1)
def random_account():
    num2 = random.choice(notUseNumbers)
    notUseNumbers.remove(num2)
    return num2

win = False
score = -1
numA = random_account()
numB = random_account()
while win == False:
    score += 1
    chosen1 = data[numA]
    chosen2 = data[numB]
    c1 = f"Compare A: {chosen1['name']} , a {chosen1['description']} , from {chosen1['country']}"
    c2 = f"Against B: {chosen2['name']} , a {chosen2['description']} , from {chosen2['country']}"
    print(logo)
    print(c1)
    print(vs)
    print(c2)
    selected = input("Who has more followers? Type 'A' or 'B' : ")
    if selected == "A":
        if chosen1['follower_count'] > chosen2['follower_count']:
            win = False
            numB = random_account()

        else:
            win = True
            print(f"Your score is : {score}")
    else:
        if chosen2['follower_count'] > chosen1['follower_count']:
            win = False
            numA = numB
            numB = random_account()

        else:
            win = True
            print(f"Your score is : {score}")
