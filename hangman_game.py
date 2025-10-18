import random

WORDS = (
    "avocado", "apple", "banana", "mango", "grapes", "orange",
    "strawberry", "blueberry", "apricot", "lemon", "peach", "pear"
)

def main():
    while True:
        print("Welcome to the Hangman Game!\n1: Play\n2: Quit")
        choice = input("\n> ")
        if choice == "1":
            word = random.choice(WORDS)
            guesses = ""
            attempt_count = len(word)+2
            print(f"\nA random FRUIT name is selected. You have a total of {attempt_count} ATTEMPTS to find it. Don't mess it up!")
            failed = True
            while failed and attempt_count > 0:
                failed = False
                for letter in word:
                    if letter in guesses:
                        print(letter.capitalize(), end=" ")
                    else:
                        failed = True
                        print("_", end=" ")
                print(f" {attempt_count} ATTEMPTS LEFT")
                guess = input("\n> ") #Can't bother validating 😪
                if guess != "":
                    attempt_count -= 1
                    if attempt_count < 1 and not failed:
                        break
                guesses += guess
            
            if failed:
                print(f"You couldn't find the word! It was {word.upper()}!")
            else:
                print(f"Congrats! You found the word {word.upper()} without running out of attempts!")
            break
        elif choice == "2":
            break

if __name__ == "__main__":
    main()
