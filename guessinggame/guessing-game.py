import random

# ASCII Art Logo
logo = """
 _   _                 _                  _____                     
| \ | |               | |                |  __ \                    
|  \| |_   _ _ __ ___ | |__   ___ _ __    | |  \/_   _  ___  ___ ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__|   | | __| | | |/ _ \/ __/ __|
| |\  | |_| | | | | | | |_) |  __/ |      | |_\ \ |_| |  __/\__ \__ \\
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|       \____/\__,_|\___||___/___/
"""
print(logo)

# Random number between 1 and 100
num = random.randint(1, 100)

# Let player choose difficulty
decide = input("Choose difficulty ('easy' or 'hard'): ").lower()

# Set lives based on difficulty level
if decide == 'easy':
    lives = 10
elif decide == 'hard':
    lives = 5
else:
    print("Invalid difficulty. Defaulting to 'easy'.")
    lives = 10

# Variable to continue game
continuegame = True

# Game loop
while continuegame:
    # Player guess
    guess = int(input("Enter a number between 1 and 100: "))

    # Check guess
    if guess > num:
        lives -= 1
        print("Too high.")
    elif guess < num:
        lives -= 1
        print("Too low.")
    else:
        print(f"Congratulations! You guessed the number {num} correctly!")
        continuegame = False
        break

    # Check if player has run out of lives
    if lives == 0:
        print(f"You've run out of lives! The correct number was {num}.")
        continuegame = False
    else:
        print(f"You have {lives} lives remaining.")
