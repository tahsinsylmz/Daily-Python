from blackjackArt import logo
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    chosen_card = random.choice(cards)
    return chosen_card


def game():
    clear_screen()
    print(logo)
    c_game = "y"
    if input("Type 'y' to play game or type 'n' to exit game.") == "y":
        computer = []
        hand = []

        computer.append(deal_card())
        hand.append(deal_card())
        def play_again():
            if input("\nDo you want to play again? y/n :") == "y":
                game()
            else:
                print("cya")
        def ace():
            if 11 in computer and sum(computer) > 21:
                computer.remove(11)
                computer.append(1)
            if 11 in hand and sum(hand) > 21:
                hand.remove(11)
                hand.append(1)

        def is_gameend():
            win = False
            tie = False

            if sum(hand) == sum(computer):
                tie = True
            else:
                if sum(hand) <= 21 and sum(computer) <= 21:
                    if sum(hand) > sum(computer):
                        win = True
                elif sum(hand) > 21 and sum(computer) <= 21:
                    win = False
                elif sum(hand) <= 21 and sum(computer) > 21:
                    win = True
                else:
                    tie = True

            if win is True:
                print("You Win!!")
                play_again()
            elif tie is True:
                print("TİE!")
                play_again()
            else:
                print("You lose!")
                play_again()

        while c_game != "n":
            hand.append(deal_card())
            if sum(hand) > 21:
                ace()
            print(f"\nYour cards : {hand} Current score : {sum(hand)}")
            print(f" Computer first card is {computer}")
            if sum(hand) == 21:
                while sum(computer) < 17:
                    computer.append(deal_card())
                    ace()
                    print(f"Computer cards : {computer} Current score : {sum(computer)}")
                is_gameend()
            else:
                if sum(hand) > 21:
                    is_gameend()
                else:
                    c_game = input("Type 'y' to get another card, type 'n' to pass: ")
                    if c_game == "n":
                        while sum(computer) < 17:
                            computer.append(deal_card())
                            if sum(computer) > 21:
                                ace()
                            print(f"Computer cards : {computer} Current score : {sum(computer)}")
                        is_gameend()

game()



