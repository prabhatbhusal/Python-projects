#Step 5
from hangmanart import stages
from hangmanart import logo
from hangmanwords import word_list
import random
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    if guess in display:
            print(f" You have already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
            

    #Check if user is wrong.
    if guess not in chosen_word:
        
        lives -= 1
        print(f"{guess} is not in the word")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    print(stages[lives])