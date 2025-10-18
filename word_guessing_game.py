import random

WORDS = (
    "rainbow", "create", "github", "phone", "mouse", "laptop",
    "bounce", "tissue", "water", "bottle", "coffee", "printer"
)

def main():
    while True:
        print("Welcome to the word guessing game!\n1: Play\n2: Quit")
        choice = input("\n> ")
        if choice == "1":
            guesses = ""
            word = random.choice(WORDS)
            turns = 12
            failed = True
            while turns > 0:
                if not failed: break
                failed = False
                print(f"Guess the characters: ({turns} turn(s) left)\n")
                for letter in word:
                    if letter in guesses:
                        print(letter, end=" ")
                    else:
                        print("_", end=" ")
                        failed = True
                guess = input("\n>")
                #This has some issues but honestly I don't care.
                if guess != "":
                    turns -= 1
                    guesses += guess
            
            if failed:
                print(f"You failed! The correct answer was {word}")
            else:
                print(f"Congrats, {word} was the correct answer!")
            break
        elif choice == "2":
            break

if __name__ == "__main__":
    main()