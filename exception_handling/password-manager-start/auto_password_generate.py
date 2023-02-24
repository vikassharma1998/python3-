import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbol = ['{', '}', '(', ')', '[', ']', '.', ':', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

random_number = random.randint(2, 4)
random_symbol = random.randint(2, 4)
random_alphabet = random.randint(6, 8)
password =[]
for num in range(random_number):
    numbers = random.choice(number)
    password.append(numbers)
for num in range(random_symbol):
    symbols = random.choice(symbol)
    password.append(symbols)
for num in range(random_alphabet):
    alphabets =random.choice(alphabet)
    password.append(alphabets)
random.shuffle(password)

password_final = ''
for i in password:
    password_final += str(i)
print(password_final)

