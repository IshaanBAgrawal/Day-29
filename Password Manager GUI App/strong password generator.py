# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

password_list = []

for char in range(1, nr_letters + 1):
    password_list += letters[char]

for num in range(1, nr_numbers + 1):
    password_list += numbers[num]

for sym in range(1, nr_symbols + 1):
    password_list += symbols[sym]

random.shuffle(password_list)

length_password_list = len(password_list)

password = ""
for rand in range(0, length_password_list):
    password += password_list[rand]

print(f"Your new password is: {password}")
