# Password Generator Project
from random import randint, shuffle, choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list1 = [choice(letters) for char in range(randint(8, 10))]
password_list2 = [choice(symbols) for char in range(randint(2, 4))]
password_list3 = [choice(numbers) for char in range(randint(2, 4))]

password_list = password_list1 + password_list2 + password_list3

shuffle(password_list)

password = ""
password = password.join(password_list)


class Password_Generator:

    def __init__(self):
        self.password = password
