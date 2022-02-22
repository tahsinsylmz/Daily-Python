import random
from hangman_words import word_list
from hangman_art import logo,stages
print(logo)
lives = len(stages) - 1
a = random.choice(word_list)
letters = []
j = 0
while j < len(a) :
  letters.append(a[j])
  j += 1
clue = []
i = 0
while i < len(a) :
  clue.append("_ ")
  i += 1
guesses = []
win = False
while win is False:
  print(stages[lives])
  p = 0
  clue2 = ""
  while p < len(a):
    clue2 += clue[p]
    p += 1
  print(clue2)
  print("\n")
  g = input("Guess a latter : \n")
  if g in guesses:
    print("You alrady ask that latter.")
  else:
    guesses.append(g)
  k = 0
  l = 0
  while k < len(guesses):
    while l < len(a):
      if guesses[k] == letters[l]:
        clue[l] = guesses[k] + " "
      else:
        clue[l] = clue[l]
      l += 1
    k += 1
    l = 0
  if g in letters:
    lives = lives
  else:
    lives -= 1
  if lives < 0 :
    win = True
    print("Hangman is dead. You lose!\n")
    print("The letter was: " + a) 
  else:
    if "_ " in  clue:
      win = False
    else:
      win = True
      print(a + "\n")
      print("You win!!")   
# içinde bulunan harfi tekrar edince lives azalmıyor ama içinde bulunmayan harfi tekrar edince lives -1 oluyor
#clear() ekleyip düzenlenebilir.