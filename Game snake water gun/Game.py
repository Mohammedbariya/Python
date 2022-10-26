import random
from re import S

rand = random.randint(1,3)
if rand == 1:
    comp = 's'
elif rand == 2:
    comp = 'w'
elif rand == 3:
    comp = 'g'

def gamewin(comp,Me):
    if comp==Me:
        return None
    elif comp == 's':
        if Me=='w':
            return False
        elif Me =='g':
            return True
    elif comp == 'w':
        if Me=='s':
            return True
        elif Me =='g':
            return False            
    elif comp == 'g':
        if Me=='w':
            return False
        elif Me =='s':
            return True


Me = input("My Turn: Snake(s) Water(w) or Gun(g)?")

print(f'Comp chose= {comp}')
print(f'You chose= {Me}')
a = gamewin(comp,Me)

if a==None:
    print("Game is tie")
elif a == True:
    print("You win")
else:
    print("You lose")       