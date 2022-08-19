import random

gameInputs = ["Rock", "Paper", "Scissor"]

userNumber = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissor: "))

computerNumber = random.randint(0,2)


if userNumber >=3 or userNumber < 0:
    print("You typed an invalid number, You lose")

else:
    userChoice = gameInputs[userNumber]
    computerChoice = gameInputs[computerNumber]

    print("User choice = " , userChoice)
    print("Computer choice = " , computerChoice)

    if computerNumber == userNumber:
        print("Draw")
    elif computerNumber == 2 and userNumber == 0:
        print("You win")
    elif computerNumber == 0 and userNumber == 2:
        print("You lose")
    elif computerNumber >userNumber:
        print("You lose")
    elif computerNumber < userNumber:
        print("You win")
    







