# program to generate a madlibs game - 
# function which returns noun -
def ret_noun():
    noun = input("Enter noun: ")
    return noun

# function which returns verb - 
def ret_verb():
    verb = input("Enter verb: ")
    return verb

# function which returns adjective - 
def ret_adj():
    adj = input("Enter adjective: ")
    return adj

name = ret_noun()
verb = ret_verb()
grade = ret_noun()
name1 = ret_noun()
food = ret_noun()
adj = ret_adj()
game = ret_noun()
ani = ret_noun()

# to print the madlibs using words from user input - 
print(f"Hi! My name is {name}! I am in grade {grade}. My teacher's name is {name1}. My favorite thing to do in school is {verb}. I like to eat {food}. I like to help my mom who is very {adj}. I also like to play {game}.I have a pet {ani}, which I love very much!")