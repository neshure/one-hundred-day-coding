from art import number
import random


# randomly selected number
random_number = random.randint(1, 100)

#Ask user if they would like to play
ask_user = input('Would you like to play? y/n: ')

#print a logo from art.py
print(number) 


easy_attempt = 10
hard_attempt = 5

# Define a function for easy difficulty level
def easy_level(easy_attempt):
      print(f"You have {easy_attempt} attempts to guess the correct number between 1 & 100")
      number_attempts = 0
      while number_attempts != random_number:
         if easy_attempt == 0:
            print(f"The number is {random_number}. Better luck next time")
            return
         guess_a_number = int(input("Make a guess: "))
         if guess_a_number > random_number:
               print("Too high")
               easy_attempt -= 1
               print(f"You have {easy_attempt} attempts left")
         elif guess_a_number < random_number:
               print("Too low")
               easy_attempt -= 1
               print(f"You have {easy_attempt} attempts left")
         elif guess_a_number == random_number:
               print("You guessed right!")

            
#Define a function for hard difficulty level
def hard_level(hard_attempt):
   print(f"You have {hard_attempt} attempts to guess the correct number between 1 & 100")
   number_attempts = 0
   while number_attempts != random_number:
      if hard_attempt == 0:
         print(f"The number is {random_number}. Better luck next time")
         return
      guess_a_number = int(input("Make a guess: "))
      if guess_a_number > random_number:
            print("Too high")
            hard_attempt -= 1
            print(f"You have {hard_attempt} attempts left")
      elif guess_a_number < random_number:
            print("Too low")
            hard_attempt -= 1
            print(f"You have {hard_attempt} attempts left")
      elif guess_a_number == random_number:
            print("You guessed right!")


game_over = False

difficulty_level = input('choose a difficulty level: Type easy or hard: ')

#Repeats the task until user runs out of attempts
while not game_over:
    if ask_user == "n":
        print("Goodbye!")
        break
    elif difficulty_level == "hard" and ask_user == "y":
        hard_level(hard_attempt)
        break
    elif difficulty_level == "easy" and ask_user == "y":
        easy_level(easy_attempt)
        break
    else:
        quit
   

    