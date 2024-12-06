import random

def game_menu():
    while True:
        print("\n1. Number Guessing Game")
        print("2. Rock-Paper-Scissors")
        print("3. Dice Roll Simulation")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target = random.randint(1, 101)
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == target:   
                print("You won!")
            else:
                print("Try Again")
        elif choice == 2:
            user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
            options = ["rock", "paper", "scissors"]
            computer_choice = options[random.randint(0, 2)]
            print(f"computer choice is {computer_choice}")
            if user_choice == computer_choice:
                print("Draw")   
            elif user_choice == "scissors":
                if computer_choice == "paper":
                    print("You won")
                else:
                    print("you lost")
            elif user_choice =="paper":
                if computer_choice =="rock":
                    print("you won")
                else:
                    print("you lost")
            elif user_choice =="rock":
                if computer_choice =="scissors":
                    print("you won")
                else:
                    print("you lost")
        elif choice == 3:
            dice = random.randint(1, 7)  
            print("Dice rolled:", dice)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
game_menu()