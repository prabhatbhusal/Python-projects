from art import logo, vs
from gamedata import data
import random

print(logo)
point = 0

# Initial random choices
datas = random.choice(data)
sample = random.choice(data)

# Ensure that `datas` and `sample` are not the same initially
while sample == datas:
    sample = random.choice(data)

continuegame = True

while continuegame:
    # Display the current comparison
    print(f"\nCompare A: {datas['name']}, a {datas['description']}, from {datas['country']}.")
    print(vs)
    print(f"Against B: {sample['name']}, a {sample['description']}, from {sample['country']}.\n")
    
    # Get user input for comparison: higher or lower
    value = input(f"Does {sample['name']} have 'higher' or 'lower' followers than {datas['name']}? ").lower()

    # Check if the user is correct
    if (value == 'higher' and sample["follower_count"] > datas["follower_count"]) or (value == 'lower' and sample["follower_count"] <= datas["follower_count"]):
        point += 1
        print(f"\nYou're right! Current score: {point}")
        
        # Swap: Now `datas` takes the value of `sample` for the next round
        datas = sample

        # Get a new random `sample` for the next comparison, ensure it's not the same as `datas`
        sample = random.choice(data)
        while sample == datas:
            sample = random.choice(data)
    else:
        print(f"\nSorry, that's wrong. Final Score: {point}")
        continuegame = False
