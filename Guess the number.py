import random
def start():
    print("Do you have an account if yes type sign in, if not type register")
    userchoice = input("Your choice: ")
    if userchoice == "sign in":
        authorization()
    elif userchoice == "register":
        registration()
    elif userchoice == "Database":
       with open("accounts", "r") as file:
            for i in file:
                print(i)

def registration():
    username = input("Type your desired username: ")
    with open("accounts", "w")as file:
        file.write(username)
    authorization()

def authorization(): 
    username = input("What's is your username: ")
    with open("accounts", "r") as file:
        if username in file:
            game(username)
        else:
            print("Not found, please register")
            registration()

def game(username):
    print("Guess any number from 1-20, you get 5 tries")
    numberToGuess = random.randint(1, 20)
    for guessTaken in range(1, 6):
        userInput = int(input(f"{username} type in your number: "))
        if userInput > numberToGuess:
            print(f"Wrong number {username.upper()}! The number you've guessed is greater than the number to guess.")
            
        elif userInput < numberToGuess:
            print(f"Wrong Number {username.upper()}! The number you've guessed is less that the number to guess.")
            
        else:
            print(f"You got it {username.upper()}!")
            break


start()

