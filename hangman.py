import random
words = ["apple", "banana", "citrus", "mango", "fig"]
find_word = random.choice(words)
guessed_letters = []
incorrect_guess = 0
max_incorrect_guess = 6
print("--------------------------")
print("       HANGMAN GAME")
print("--------------------------")
print("Guess the word by one letter at a time!!!")
print("You have 6 incorrect guesses.")

while incorrect_guess < max_incorrect_guess:
    display_word = ""

    for letter in find_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n Word:", display_word)
    print("Incorrect guesses:", incorrect_guess) 
    print("Remaining Attempts:", max_incorrect_guess - incorrect_guess)
    print("Maximum incorrect guess:", max_incorrect_guess) 
    if "_" not in display_word:
        print("\n Congratulations! You guessed the words!")
        print("The word was:", find_word)
        break
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in find_word:
        print("You have guessed it correctly! ")
    else:
        incorrect_guess += 1
        print("Oops! You have guessed it wrongly.")
else:
    print("\n GAME OVER!\n You have lost the game!!")
    print("The word was:", find_word)