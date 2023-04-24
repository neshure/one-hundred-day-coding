import random
import os
from art import logo

# # Clearing the Screen
#os.system('cls')

def play_game():
  print(logo)
# Create a deal_card() function that uses the List below to *return* a random card.

  def deal_card():
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      card = random.choice(cards)
      return card

  #Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []

  for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())


  #Create a function called calculate_score() that takes a List of cards as input. 
  # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

  def calculate_score(cards):
      if sum(cards) == 21 and len(cards) == 2:
          return 0
      #Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1.
      if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
      return sum(cards)



  ##Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
  is_game_over = False


  while not is_game_over:
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")
      if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
      #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      else:
        draw_another_card = input("Type 'yes' to get another card, type 'no' to pass: ")
        if draw_another_card == "yes":
            user_cards.append(deal_card())
        else:
          is_game_over = True

  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

  while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)


  '''
  Create a function called compare() and pass in the user_score and computer_score. 
  If the computer and user both have the same score, then it's a draw. 
  If the computer has a blackjack (0), then the user loses. 
  If the user has a blackjack (0), then the user wins. 
  If the user_score is over 21, then the user loses. 
  If the computer_score is over 21, then the computer loses. 
  If none of the above, then the player with the highest score wins.

  '''

  def compare(user_score, computer_score):
    if computer_score == user_score:
      return "Draw"
    elif computer_score == 0:
        return "You lose, computer has a Blackjact"
    elif user_score == 0:
        return "You win, you have a Blackjack"
    elif user_score > 21:
        return "You lose, you went over 21"
    elif computer_score > 21:
        return "You win, computer went over 21"
    else:
        if user_score > computer_score:
          return "You win"
        else:
          return "You lose"
        
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


play_game()

##Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  os.system('cls')
  play_game()