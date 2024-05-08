# lib/cli.py

from helpers import (
    exit_program, 
    team_menu, 
    player_menu, 
    play_match_random, 
    play_match_choose, 
    records
)
from seed import (seed_database)


def main():
        while True:
            main_menu()
            choice = input("-> ")
            if choice == "0":
                exit_program()
            elif choice == "1":
                team_menu()
            elif choice == "2":
                player_menu()
            elif choice == "3":
                play_match_random()
            elif choice == "4":
                play_match_choose()
            elif choice == "5":
                records()
            else:
                print("Invalid choice")


def main_menu():
    print("------------------------------------")
    print("Please select an option:")
    print("1. Enter The Teams Hub")
    print("2. Enter The Players Hub")
    print("3. Play Random Match")
    print("4. Play Match With Team")
    print("5. View Team Points")
    print("0. Exit Program")
    print("------------------------------------")


if __name__ == "__main__":
    reset = input("Before we begin would you like to seed the database? Y/N: -> ")
    if reset == "y" or reset == "Y":
        seed_database()
        main()
    elif reset == "n" or reset == "N":
        main()
    else:
        print("Please type Y for (yes) ||or|| N for (no)")