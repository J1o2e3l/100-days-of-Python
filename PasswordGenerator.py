#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomized:
#e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

password = ""

for l in range(1, nr_letters+1):
  random_letter = random.choice(letters)
  password += random_letter
  
for s in range(1, nr_symbols+1):
  random_symbol = random.choice(symbols)
  password += random_symbol

for n in range(1, nr_numbers+1):
  random_number = random.choice(numbers)
  password += random_number

print(f"Password Choice 1: {password}")




#Hard Level - Order of characters randomized:
#e.g. 4 letters, 2 symbols, 2 numbers = g^2jk8&P


pass_list = list(password)
random.shuffle(pass_list)

final_pass = ""
for char in pass_list:
  final_pass += char
  
print(f"Password choice 2: {final_pass}")
