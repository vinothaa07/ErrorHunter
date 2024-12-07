import random

def snake_and_ladder():
    position = 0
    while (position < 100):
        dice = random.randint(1, 6)
        position += dice
        if position == 100:
            print("You won the game!!")
            break
        elif position == 50:  # Climbing a ladder
            position = 75
        elif position == 25:  # Snake bite
            position = 10
        print(f"Dice: {dice}, Position: {position}")
    else:
        print("You  are in the 100 th place YOU won the game" )

snake_and_ladder()