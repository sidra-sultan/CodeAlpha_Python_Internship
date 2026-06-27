import random

words = [
    "python", "leetcode", "codealpha", "tea", "cat",
    "pineapple", "mushroom", "madam", "result", "ready",
    "reopen", "lock", "ribbon", "warrior", "sorrow",
    "symptoms", "carrot", "brucelee", "manga"
]

hangman = [
"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
"""
]

word = random.choice(words)
guessed_letters = []
lives = 6

print("========== HANGMAN GAME ==========")

while lives > 0:

    print(hangman[6 - lives])

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Lives Left:", lives)
    print("Guessed Letters:", " ".join(guessed_letters))

    if "_" not in display:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        lives -= 1
        print("Wrong Guess!")

else:
    print(hangman[6])
    print("\nGame Over!")
    print("The word was:", word)