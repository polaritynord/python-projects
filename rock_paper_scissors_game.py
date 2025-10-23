import random

picks = ["r", "p", "s"]
picks_fullname = ["rock", "paper", "scissors"]

def main():
    while True:
        print("Welcome to the Rock Paper Scissors game!\n1: Play\n2: Quit")
        choice = input("\n> ")
        if choice == "1":
            turn = "computer"
            if input("Would you like to go first? (Write y if yes)\n> ").lower() == "y":
                turn = "player"
            winner = None
            players_pick = None
            computers_pick = None
            while winner is None:
                if turn == "player":
                    while not players_pick in picks:
                        print("Write R for rock, P for paper, or S for scissors.\n")
                        players_pick = input("> ").lower()
                else:
                    if players_pick is None:
                        computers_pick = random.choice(picks)
                    else:
                        picks.remove(players_pick)
                        computers_pick = random.choice(picks)
                        picks.append(players_pick)
                        print(f"The computer chose {picks_fullname[picks.index(computers_pick)]}")
                turn = "player" if turn == "computer" else "player"
        elif choice == "2":
            break

if __name__ == "__main__":
    main()
