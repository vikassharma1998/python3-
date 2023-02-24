from game_data import data
from art import vs
import random
def check_answer(user_answer, a_follow, b_follow):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_follow > b_follow:
    return user_answer == "a"
  else:
    return user_answer == "b"
game_on = True
score = 0
while game_on:
    a = random.choice(data)
    b = random.choice(data)
    print(a)
    print(vs)
    print(b)
    user_answer = input("Who has a More Followers 'a' or 'b': ").lower()
    print(user_answer)
    a_follow = a['follower_count']
    b_follow = b['follower_count']
    is_correct= check_answer(user_answer, a_follow, b_follow)
    if is_correct:
        score += 1
    else:
        print(f"You Lose Game and your Score is {score}")
        game_on = False