from random import randint

def main():
    running = True
    while running:
        print("Welcome to the number guessing game!\n")
        choice = input("1: Play\n2: Quit\n\n> ")
        if choice == "1":
            #Too lazy to ensure that the inputs are integers tbh
            lower_bound = input("\nWrite a lower bound: ")
            upper_bound = input("\nWrite an upper bound: ")
            num = randint(int(lower_bound), int(upper_bound))
            print("\nGreat! I picked a number between those, try to find it:\n")
            guess = ""
            attempt_count = 0
            while guess != str(num):
                attempt_count += 1
                guess = input(f"\nAttempt {attempt_count}: ")
                if guess > str(num):
                    print("\nTry a little lower...")
                if guess < str(num):
                    print("\nTry a little higher...")
            print(f"You found the number I guessed, {guess}, after {attempt_count} attempt(s)!")
            running = False
        elif choice == "2":
            running = False

if __name__ == "__main__":
    main()
