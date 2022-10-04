import random
import string

word_list = []
letters_l = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
letters_u = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
special_signs = ['-', '_', '#', '$', '&', '*', '@']
animals = ["ponies", "elephants", "unicorns", "tiger", "lion", "dog", "cat"]

letter_1 = random.choice(letters_l)
num = random.choice(numbers)
sign = random.choice(special_signs)
ani = random.choice(animals)
letter_2 = random.choice(letters_u)

password = letter_1 + num + sign + ani.capitalize() + letter_2
print(password)
