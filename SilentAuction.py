from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction!")



def find_highest_bid(bidding_dictionary):
  
  highest_bid = 0
  winner = ""
  for name in bidding_dictionary:
    bid_amount = bidding_dictionary[name]
    if bid_amount>highest_bid:
      highest_bid = bid_amount
      winner = name   
  print(f"The winner is: {winner}, They won with a bid of ${highest_bid}")
     
      
  
    
    
  
  
  # auction_dictionary["amount"] = bid
  # print(auction_dictionary)
  # max = auction_dictionary[bidder_name].max()

  # print(f"{auction_dictionary[max]} has to pay.")
    
bidding_done = False
auction_dictionary = {}

while not bidding_done:

  bidder = input("Enter the name of the bidder: ")
  bid = int(input("How much would you like to bid? $"))
  auction_dictionary[bidder] = bid
  
  
  more = input('''Is there anyone else who wants to bid? Type "yes" or "no" ''').lower()
  if more == "yes":
    clear()
  elif more == "no":
    bidding_done = True
    find_highest_bid(bidding_dictionary = auction_dictionary)
     
    
    
  
  
