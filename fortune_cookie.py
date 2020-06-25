import random

fortunes = [
    "The end is near and it's all YOUR fault!!",
    "Only listen to the fortune cookie! Disregard all other fortune telling units!",
    "You will die alone and poorly dressed...",
    "Don't kiss an elephant on the lips today!",
    "You will be hungry again in one hour",
    "The fortune you seek is in another cookie...",
    "You have been poisoned!",
    "The force is strong with.... not you, someone else!",
    "Something you lost will soon turn up",
    "Your pet is planning to eat you... if you don't have a pet, stay away from the nearest child"
]

unopened_cookie = 1

fortune = random.choice(fortunes)

print("You have a fortune cookie!!")

open_or_not = input("Do you open it? Y/N: ")

cookie = open_or_not.lower()

while unopened_cookie == 1:
    if cookie == 'y':
        print(f'You read, {fortune}')
        unopened_cookie = 0
    elif cookie == 'n':
        print("That's so sad... :`(")
        break
