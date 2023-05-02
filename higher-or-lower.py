from art import higher_or_lower, VS
from game_data import data
import random
import os


#Print higher or lower ASCII logo
print(higher_or_lower)

#Randomly selected data from game_data
random_choice_A = random.choice(data)
random_choice_B = random.choice(data)




#Compare follower count
follower_count_A = random_choice_A['follower_count']
follower_count_B = random_choice_B['follower_count']


print(f"Compare A: {random_choice_A['name']}, a {random_choice_A['description']}, from {random_choice_A['country']}. ")
#print Vs. ASCII logo
print(VS)
print(f"Against B: {random_choice_B['name']}, a {random_choice_B['description']}, from {random_choice_B['country']}. ")
# Ask user who has more follower
guess_data = input("Who has more followers? Type 'A' or 'B': ").lower()


#Compare Choices A and B
def compare_A_and_B():
  if guess_data == 'a' and (follower_count_A >= follower_count_B):
    return random_choice_A

  elif guess_data == 'b' and (follower_count_B >= follower_count_A):
    return random_choice_B
  else:
    return 0




is_game_over = False

game_score = 0

os.system('clear')
print(higher_or_lower)
while not is_game_over:
  correct_answer = compare_A_and_B()
  if correct_answer == 0:
    print('Better luck next time buddy!')
    is_game_over = True
  else:
    game_score += 1
    print(f"Game score: {game_score}")
    random_choice_C = random.choice(data)
    correct_answer = (f"Compare A: {correct_answer['name']}, a {correct_answer['description']}, from {correct_answer['country']}. ")
    print(correct_answer)
    print(VS)
    compare_answer = (f"Against B: {random_choice_C['name']}, a {random_choice_C['description']}, from {random_choice_C['country']}. ")
    print(compare_answer)
    guess_data = input("Who has more followers? Type 'A' or 'B': ").lower()
    

          