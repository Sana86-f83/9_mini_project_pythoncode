import random

def hangman():
    list_words = ["Python", "html", "Php", "sql", "nextjs", "typescript"]
    word = random.choice(list_words).lower()
    turns = 10
    guess_made = ""
    entries_set = set("abcdefghijklmnopqrstuvwxyz")

    while turns > 0:
        main_word = ""

        for letter in word:
            if letter in guess_made:
                main_word += letter
            else:
                main_word += "_"

        if main_word == word:
            print(main_word)
            print("You won!!")
            break

        print("Guess the word:", main_word)
        guess = input().lower()

        if guess in entries_set:
            guess_made += guess
        else:
            print("Enter a valid character")
            continue

        if guess not in word:
            turns -= 1

            if turns == 9:
                print("9 turns left!!")
                print("--------------")
            if turns == 8:
                print("8 turns left!!")
                print("--------------")
                print("       O      ")
                print("--------------")
            if turns == 7:
                print("7 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
                print("--------------")
            if turns == 6:
                print("6 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
                print("      /       ")
                print("--------------")
            if turns == 5:
                print("5 turns left!!")
                print("--------------")
                print("       O      ")
                print("       |      ")
                print("      / \\     ")
                print("--------------")
            if turns == 4:
                print("4 turns left!!")
                print("--------------")
                print("      \\O      ")
                print("       |      ")
                print("      / \\     ")
                print("--------------")
            if turns == 3:
                print("3 turns left!!")
                print("--------------")
                print("      \\O/     ")
                print("       |      ")
                print("      / \\     ")
                print("--------------")
            if turns == 2:
                print("2 turns left!!")
                print("--------------")
                print("      \\O/ |   ")
                print("       |      ")
                print("      / \\     ")
                print("--------------")
            if turns == 1:
                print("1 turn left!!")
                print("--------------")
                print("      \\O_/    ")
                print("       |      ")
                print("      / \\     ")
                print("--------------")
            if turns == 0:
                print("0 turns left!!")
                print("--------------")
                print("      \\O_/    ")
                print("       |      ")
                print("      / \\     ")
                print("---        ---")
                print("You let a good person die")

    if turns == 0:
        print("The word was:", word)

name = input("Enter your name: ")
print("Welcome...", name, "!")
print("Guess the word in less than 10 attempts")
hangman()