import random
import word_list
import hangman_art

word_list = word_list.word_list
stages = hangman_art.stages
logo = hangman_art.logo

word_list = [element.lower() for element in word_list]

chosen_word = random.choice(word_list)
# print(chosen_word)
display = []
lives = 6
end_of_game = False

print(logo)
print("Welcome to hangman!")

for char in chosen_word:
  display += "_"

print(f"{' '.join(display)}\n")

while not end_of_game:
  
  guess = input("Guess a letter: ").lower()
  
  for position in range(len(chosen_word)):
    
    letter = chosen_word[position]
    
    if letter == guess:
      if display[position] == letter:
        print(f"You have already guessed '{guess}'.")
      else:
        display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is not in the word. You lose a life.")
    if lives == 0:
      end_of_game = True

  print(stages[lives])

  if lives > 0:
    print(f"{' '.join(display)}\n")

  if "_" not in display:
    end_of_game = True
  
if lives > 0:
  print("You win!")
else:
  print("You lose!")
  print(f"The word was: {chosen_word}")