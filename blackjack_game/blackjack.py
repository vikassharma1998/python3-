import random

user_cards = []
computer_cards = []

def ramdom_num():
    cards = [1,2,3,4,5,6,7,8,9,10,10,10]
    cards = random.choice(cards)
    return cards
def result():
    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)
    print(f"User Score is {user_sum}")
    print(f"Computer Score is {computer_sum}")
    if user_sum > 21:
        print("You went over. You lose 😭")
    elif computer_sum > 21:
        print("you win the game 😃")
    elif user_sum > computer_sum:
        print("you win the game 😃")
    elif user_sum < computer_sum:
        print("you lose the game 😭")
    elif user_sum == computer_sum:
        print("Match is Draw 🙃")
    else:
        return "You lose 😤"
def extra_cards():
    extra_card = input("You want extra card type 'y' otherwise 'n': ")
    if extra_card == "y":
        user_cards.append(ramdom_num())
        computer_cards.append(ramdom_num())
        print(f"User Card is : {user_cards}")
        print(f"computer Card is : {computer_cards[0]}")
        extra_cards()
    elif extra_card == "n":
        result()
    else:
        print("You select type a wrong keyword please try again")
        extra_cards()

def play():
    for i in range(2):
        user_cards.append(ramdom_num())
        computer_cards.append(ramdom_num())
    print(f"User Card is : {user_cards}")
    print(f"computer Card is : {computer_cards[0]}")
    extra_cards()

while input("Do you want to play Rv blackjack Game type 'y' for play otherwise 'n' :") == "y":
    play()
