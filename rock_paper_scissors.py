import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "sessiors"]

while True:
    user_input = input("Type Rock/Paper/Sessiors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Sessiors: 3
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "sessiors":
        print("You win!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1

    elif user_input == "sessiors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    
    elif user_input == computer_pick:
        print("It's draw")

    else:
        print("You lost!")
        computer_wins += 1

print("You wons", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("GoodBye!")