import random


def generate_password():
    alphabet = "abcdefghijklmnopqrstubwxyz"
    digits = "1234567890"

    letters_l = alphabet.split()
    letters_u = alphabet.upper().split()

    numbers = digits.split()
    special_signs = ['-', '_', '#', '$', '&', '*', '@']
    animals = ["ponies", "elephants", "unicorns", "tiger", "lion", "dog", "cat"]

    letter_1 = random.choice(letters_l)
    number = random.choice(numbers)
    sign = random.choice(special_signs)
    animal = random.choice(animals)
    letter_2 = random.choice(letters_u)

    return letter_1 + number + sign + animal.capitalize() + letter_2
