print("==> PASSWORD GENERATOR <==")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

user_letter = int(input("How many letters would you like in your password? "))
user_numbers = int(input("\nHow many numbers would you like? "))
user_symbols = int(input("\nHow many symbols would you like? "))

password_letters = ""
for letter in range(0, user_letter):
  password_letters = password_letters + letters[letter]
#print(password_letters)

password_numbers = ""
for number in range(0, user_numbers):
  password_numbers += numbers[number]
#print(password_numbers)

password_symbols = ""
for symbol in range(0, user_symbols):
  password_symbols += symbols[symbol]
#print(password_symbols)

derived_password = password_letters + password_numbers + password_symbols
strings_to_list = list(derived_password)
random.shuffle(strings_to_list)
lenght_of_password = len(strings_to_list)

rand_strings = ""
for list in range(0, lenght_of_password):
  rand_strings += strings_to_list[list]
print(f"\nYour new generated password is {rand_strings}, and the lenght of the password is {lenght_of_password}")
