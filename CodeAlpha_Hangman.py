import random

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def hangman():
    words = ["python", "hangman", "programming", "challenge", "developer"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = len(HANGMAN_PICS) - 1
    guessed_letters = set()

    print("Welcome to Hangman!")
    print(f"The word to guess is: {word}")  # <-- Word revealed here
    print(HANGMAN_PICS[0])
    print(" ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        stage_index = (len(HANGMAN_PICS) - 1) - attempts
        print(HANGMAN_PICS[stage_index])
        print(" ".join(guessed))
        print(f"Attempts left: {attempts}")

    if "_" not in guessed:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("💀 Game over! The word was:", word)

if __name__ == "__main__":
    hangman()