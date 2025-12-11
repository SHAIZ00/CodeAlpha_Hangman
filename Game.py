import random

words = ["python", "coding", "apple", "hangman", "simple"]
secret_word = random.choice(words)

guessed_letters = []
wrong = 0
limit = 6

print("Welcome to Hangman!")

while wrong < limit:
    display_word = ""
    for ch in secret_word:
        if ch in guessed_letters:
            display_word += ch + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("You won! The word was:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only ONE letter.")
        continue

    if not guess.isalpha():
        print("Please enter a LETTER (a-z).")
        continue

    if guess in guessed_letters:
        print("You already tried that letter.")
        continue

    if guess in secret_word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        wrong += 1
        print("Wrong!", "Attempts left:", limit - wrong)
        guessed_letters.append(guess)

if wrong == limit:
    print("\nYou lost! The word was:",secret_word)