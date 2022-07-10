import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ")
n1 = random.randint(1, 101)

if difficulty == "hard":
    guess = 5
else:
    guess = 10

while guess != 0 :
    print(f"You have {guess} attemps remaining to guessthe number.")
    n2 = int(input("Make a guess: "))
    guess -= 1
    if n2 > n1:
        print("Too high.")
    elif n2 < n1:
        print("Too low.")
    else:
        print("You WİN!")
        break
    if guess == 0:
        print(f"You have {guess} attemps remaining to guessthe number.")
        print("You LOSE!")
        print(f"Number is : {n1}")
    else:
        print("Guess again.")
