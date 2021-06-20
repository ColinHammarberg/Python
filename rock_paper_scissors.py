import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type Rock/Paper/Scrissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2
    
    print("Goodbye!")


