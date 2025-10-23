import random
import time

def player_write_amount(current_max):
    amount = -1
    while amount > 3 or amount <= 0:
        print("\nWrite the amount of numbers you want to add.")
        amount = int(input("\n> "))
    s = [current_max+num+1 for num in range(amount)]
    print(f"\nAdded {s}.")
    return s

def main():
    while True:
        print("Welcome to the 21 number game!\n1: Play\n2: Quit")
        choice = input("\n> ")
        if choice == "1":
            current_set = []
            #Determine who plays first
            first = input("\nWould you like to go first? (write y if yes):\n> ")
            turn = "player" if first.lower() == "y" else "computer"
            winner = None
            #Gameloop until 20 is gotten
            while winner is None:
                if turn == "player":
                    #Ask the player to write numbers and combine it with the total
                    s = player_write_amount(current_set[-1] if len(current_set) > 0 else 0)
                    current_set = list(set(s).union(current_set))
                    print(f"Final state:\n{current_set}")
                else:
                    #Determine a random amount to add
                    c = random.randint(1, 3)
                    for i in range(c):
                        #Check if the computer lost
                        if len(current_set) > 0 and current_set[-1] == 20:
                            winner = "player"
                        maximum = current_set[-1] if len(current_set) > 0 else 0
                        current_set.append(maximum+1)
                    print(f"\nThe computer added {c} numbers to the list.\nFinal state:")
                    print(current_set)
                    #Check if the player lost
                    if current_set[-1] == 20:
                        winner = "computer"
                #Give the turn to the other
                turn = "computer" if turn == "player" else "player"
                time.sleep(1)
            print(f"The winner is the {winner}.")
            break
        elif choice == "2":
            break

if __name__ == "__main__":
    main()
