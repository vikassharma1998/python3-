from replit import clear
def start_again():
    global game_on
    start_again = input("Do you want play again bat game ? 'y' and 'n': ")
    if start_again == "y":
        game_on = True
    elif start_again == "n":
        game_on = False
        print("Thanks to play a RVWorld Game")
    else:
        print("You are Enter Wrong keyword try again ")
        start_again()
def play():
    global game_on
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "n":
        find_highest_bidder(bat_list)
        start_again()
    elif should_continue == "y":
        game_on = True
    else:
        print("You Enter a Wrong Keyword Try again")
        play()
def find_highest_bidder(bat_list):
    highest_bat_amount = 0
    winner=""
    for bidder in bat_list:
        bid_amount = bat_list[bidder]
        if bid_amount > highest_bat_amount:
            highest_bat_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bat_amount}")


bat_list = {}
game_on = True
print("Welcome to Rv Bit Game")

while game_on:
    name = input("What is your name: ")
    bat = int(input("what's your bat amount: $"))
    bat_list[name] = bat
    play()
