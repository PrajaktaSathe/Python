ch = int(
    input(
        "Do you want to generate a username with your name (1) or username without your name (2): "
    ))
vowels = ['a', 'e', 'i', 'o', 'u']
if ch == 1:
    name = input("Enter name/nickname: ").lower()
    lastn = input("Enter last name: ").lower()
    bday = input("Enter birth-date (only day): ")
    pwd = ""
    for l in name:
        # if l in vowels:
        #     l = l.capitalize()
        pwd += l
    pwd = pwd + "_"
    for l in lastn:
        # if l in vowels:
        #     l = l.capitalize()
        pwd += l
    pwd = pwd + "_" + bday
    print(pwd)
elif ch == 2:
    fav_adj = input("Enter adjective: ").lower()
    fav_animal = input(
        "Enter your favourite animal/cartoon/character: ").lower()
    fav_num = input("Enter your favourite number: ")
    pwd = fav_adj + "_" + fav_animal + "_" + fav_num
    print(pwd)
else:
    print("Invalid input!")
