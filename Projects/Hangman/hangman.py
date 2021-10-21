# We will be playing HANGMAN game here.....

import random
import hangman_art
from hangman_words import word_list
import os

chosen_word = random.choice(word_list)
game_continue = True
misses = []
chances = 6
s2 = []
for i in range(len(chosen_word)):
    s2.append("_")
    
print(hangman_art.logo)
print(" ".join(s2))

while(game_continue):
    i=0
    guess_input = input("\nGuess: ").lower()
    guess = False
    
    os.system('clear')
        
    if guess_input in s2 or guess_input in misses:
        print(f"You have already guessed '{guess_input}'\n")
        
    else:
        for i in range(0,len(chosen_word)):
            if guess_input == chosen_word[i]:
                guess = True
                s2[i] = chosen_word[i]
        
        if guess == False: #what happens when wrong choice is made
            print("You made a wrong guess.\n")
            chances -= 1
            misses.append(f"{guess_input}")
        else:
            print("Right guess.\n")
        
    print(f'{" ".join(s2)}') #print the current updated string
    print("\nMisses: "+" ".join(misses)) 
    print(hangman_art.stages[chances])
        
    any_left = False
     
    if "_" in s2:
        any_left = True
        
    if any_left == False:
        print(hangman_art.you_won)
        game_continue = False    
        
    if chances == 0:
        game_continue = False
        if any_left:
            print(hangman_art.game_over)
            print(f"Right answer was '{chosen_word}'")

