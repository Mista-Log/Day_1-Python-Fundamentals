import random
import string

def get_word(word_list):
    """Selects a random word from the provided list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the word with underscores for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def check_guess(guess, word, guessed_letters):
    """Checks if the guessed letter is in the word and updates the guessed letters list."""
    if guess in word and guess not in guessed_letters:
        guessed_letters.append(guess)
        return True
    else:
        return False

def check_win(word, guessed_letters):
    """Checks if the player has won the game."""
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def hangman(word_list):
    """Main function for the Hangman game."""
    print("Welcome to Hangman!")

    word = get_word(word_list)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nYou have {} attempts left.".format(attempts))
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in string.ascii_lowercase:
            if check_guess(guess, word, guessed_letters):
                print("Correct!")
                if check_win(word, guessed_letters):
                    print("Congratulations, you won!")
                    break
            else:
                print("Incorrect.")
                attempts -= 1
        else:
            print("Please enter a valid letter.")

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was: {}".format(word))

if __name__ == "__main__":
    word_list = ["apple", "banana", "orange", "grape", "pear", "strawberry", "blueberry", "raspberry"]
    hangman(word_list)
