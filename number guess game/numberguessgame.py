import random

def result():
    global level_type


guess_number = random.randint(1 , 100)
print(guess_number)
game_level = input("Select Which level you want to Play 'easy' 'Medium' 'Hard' : ").lower()
level_dict = {'easy': 12, 'medium': 8, 'hard': 5}
level_type = level_dict[game_level]
print(level_type)
for i in range(level_type):
    print(f"you have {level_type} attempts remaining to guess the number ")
    number_guess_input = int(input("Guess the number : "))
    if number_guess_input == guess_number:
        print("You Win the Game 😃 ")
        break
    elif level_type == 1:
        print("You Lose the Game 😭")
    else:
        level_type -= 1
