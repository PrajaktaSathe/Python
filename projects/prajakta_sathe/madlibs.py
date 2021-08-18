# Program to generate a madlibs game -
# function which returns noun -
def return_noun():
    noun = input("Enter noun: ")
    return noun


# function which returns verb -
def return_verb():
    verb = input("Enter verb: ")
    return verb


# function which returns adjective -
def return_adjective():
    adjective = input("Enter adjective: ")
    return adjective


if __name__ == "__main__":
    name = return_noun()
    verb = return_verb()
    grade = return_noun()
    name1 = return_noun()
    food = return_noun()
    adj = return_adjective()
    game = return_noun()
    ani = return_noun()

    # to print the madlibs using words from user input -
    print(f"Hi! My name is {name}! I am in grade {grade}. My teacher's name is {name1}. My favorite thing to do in "
          f"school is {verb}. I like to eat {food}. I like to help my mom who is very {adj}. I also like to play "
          f"{game}. I have a pet {ani}, which I love very much!")
