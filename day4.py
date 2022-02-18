import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
a = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")
a = int(a)
if a >= 3 or a < 0 :
  print("You typed an invalid number, you lose!")
else:
  d = {0 : rock, 1 : paper, 2 : scissors}
  i = random.randint(0,2)
  print(d[a])
  print("Computer choose.")
  print(d[i])
  if a == 0 and i == 2 :
    print("You Win.")
  elif a == 1 and i == 0 :
    print("You Win.")
  elif a == 2 and i == 1 :
    print("You Win.")
  elif a == i :
    print("TİE.")
  else: 
    print("You Lose.")

# you could use lists for rock,paper,scissors because lists have indexes already in binary system.