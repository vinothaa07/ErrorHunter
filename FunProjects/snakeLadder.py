import random

def snake_and_ladder():
    position = 0
    while position != 100:
        dice = random.randint(1, 6)
        position += dice
        if position == 50:  # Climbing a ladder
            position = 75
        elif position == 25:  # Snake bite
            position = 10
        print(f"Dice: {dice}, Position: {position}")

snake_and_ladder()