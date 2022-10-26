a = True

while a == True:
    import random
    randnumber = random.randint(1,10000)
    print ("Welcome to the random guess game")
    print("Guess the number between 1 to 10000")
    
    name = input("Enter your name :")


    userguess= int(input("Enter your guess : "))
    guesses = 1

    if userguess == randnumber:
        print(f"Congrats! You guess it right at {guesses} attempt")

    else:
        guesses = 1
        while(userguess != randnumber):

            guesses +=1

            if userguess<randnumber:
                print("You guess it wrong , Guess again")
                print("Guess a bigger number")

            elif userguess>randnumber:
                print("You guess it wrong , Guess again")
                print("Guess a smaller number")

            userguess= int(input("Enter your guess : "))
        print(f"You guess number in {guesses} attempts")

    with open("hiscore.txt", "r") as f:

        lines = f.readlines()
        hiscore = int(lines[1])

    if hiscore>guesses:
        with open("hiscore.txt","r") as f:
            j = f.read()
            print(f"The old score was\n{j}")
        print("Congrats you have breaked the current highest record of guess game")
        with open("hiscore.txt","w") as f:
            f.write(f'''The highest score of guesses game is made by {name} and it is:-
{guesses}''')
    elif hiscore<guesses:
        print("sorry you didn't  break the highest score of guess game ")
        with open("hiscore.txt", "r") as f:
            b = f.read()
            print(b)
    h = input("Do you want to replay the guess game? Yes/No :")
    d = h.lower()
    if d =="yes":
        continue
    else:
        exit()        