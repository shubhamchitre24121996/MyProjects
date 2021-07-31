import random
comp = input("Comp Turn: Rock(r) Paper(p) or Scissors(s)?")
you = input("Your Turn: Rock(r) Paper(p) or Scissors(s)?")


def gameWin(comp, you):
    if comp == you:
        return None
    if comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


randNo = random.randint(1, 3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")
