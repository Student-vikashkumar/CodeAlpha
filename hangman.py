import random

def hangman_game():
    # Word list for the game
    word_list = ["python", "programming", "hangman", "challenge", "developer", "function"]
    
    # Select a random word
    secret_word = random.choice(word_list)
    guessed_word = ["_"] * len(secret_word)
    attempts_left = 6
    guessed_letters = []
    
    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")
    print(f"The word has {len(secret_word)} letters: {' '.join(guessed_word)}")
    
    while attempts_left > 0 and "_" in guessed_word:
        print(f"\nAttempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Get user's guess
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try another.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Good job! That letter is in the word.")
            # Reveal the letter in the guessed word
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print("Oops! That letter is not in the word.")
            attempts_left -= 1
        
        print(f"Word: {' '.join(guessed_word)}")
    
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word!")
        print(f"The word was: {secret_word}")
    else:
        print("\nGame over! You've run out of attempts.")
        print(f"The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    hangman_game()
