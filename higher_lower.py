from hl_art import logo, vs
from game_data import data
import random
from replit import clear

# Display art
print(logo)
score = 0
should_continue = True
account_a = random.choice(data)


def format_data(account):
  """ Format account data into a printable format """

  account_name = account["name"]
  account_des = account["description"]
  account_country = account["country"]
  return f"A: {account_name}, a {account_des} from {account_country}"


def check(guess, a_follolwers, b_followers):
  if a_follolwers>b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Repeat the game 

while should_continue:
  
  # Get a random account from data
  
  account_b = account_a
  account_b = random.choice(data)


  # Acc. B = Acc. A
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A  {format_data(account_a)}")
  print(vs)
  print(f"Compare B  {format_data(account_b)}")
  
  
  
  
  # Ask the user for a guess
  guess = input("Who has more followers A or B? ").lower()
  
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]



  isCorrect = check(guess, a_followers, b_followers)
  
  
  # Check if user is correct
  ## Get follower account
  ## use "if" to check if user is correct
  
  # Give the user feedback
  # Keep score

  # Clear the screen on wrong guess
  clear()
  print(logo)
  

  if isCorrect:
    score += 1
    print(f"Right Yor score: {score}")
  else:
    should_continue = False
    print(f"Wrong, Final score: {score}")
















