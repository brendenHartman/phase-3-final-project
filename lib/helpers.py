# lib/helpers.py
from models.player import Player
from models.team import Team
import random

def exit_program():
    print("------------------------------------")
    print("Goodbye!")
    print("------------------------------------")
    exit()

def team_menu():
    new = True
    here = True
    while here == True:
        if new:
            print("------------------------------------")
            print("Welcome To The Teams Hub!")
        print("------------------------------------")
        print("Please select an option:")
        print("L. List All Teams")
        print("C. Create New Team")
        print("D. Delete A Team")
        print("A. List All Players Of A Team")
        print("P. View Team Points")
        print("B. Back To Main Menu")
        print("------------------------------------")
        choice = input("-> ")
        if choice == "L" or choice == "l":
            new = False
            teams = Team.get_all()
            print("------------------------------------")
            for team in teams: 
                print(team)
        elif choice == "C" or choice == "c":
            new = False
            create_team()
        elif choice == "D" or choice == "d":
            new = False
            print("------------------------------------")
            print_team_numbers()
            _team = input("Enter the team number you wish to delete: -> ")
            try:
                team = Team.find_by_id(_team)
                print("------------------------------------")
                print(f"The Team {team.name} has gone bankrupt!!!")
                [player.delete() for player in team.players()]
                team.delete()
            except Exception as exc:
                print("Error deleting team: ", exc)
        elif choice == "A" or choice == "a":
            new = False
            print("------------------------------------")
            print_team_numbers()
            players_of()
        elif choice == "P" or choice == "p":
            new = False
            records()
        elif choice == "B" or choice == "b":
            here = False
        else:
            new = False
            print("------------------------------------")
            print("Invalid choice")




def player_menu():
    new = True
    here = True
    while here == True:
        if new:
            print("------------------------------------")
            print("Welcome To The Players Hub")
        print("------------------------------------")
        print("Please select an option:")
        print("L. List All Players")
        print("C. Create New Player")
        print("T. Transfer A Player")
        print("R. Retire A Player")
        print("B. Back To Main Menu")
        print("------------------------------------")
        choice = input("-> ")
        if choice == "L" or choice == "l":
            print("------------------------------------")
            new = False
            players = Player.get_all()
            for player in players:
                print(player)
        elif choice == "C" or choice == "c":
            print("------------------------------------")
            new = False
            create_player()
        elif choice == "T" or choice == "t":
            print("------------------------------------")
            new = False
            print_team_numbers()
            players_of()
            player = None
            while player == None:
                player_name = input("Type Player Name To Transfer: -> ")
                player = Player.find_by_name(player_name.title())
                if player == None:
                    print("------------------------------------")
                    print("Invalid Name")
                    print("------------------------------------")
            print("------------------------------------")
            print_team_numbers()
            new_team_id = int(input("Select Team Number Of New Team: -> "))
            try:
                player.team_id = new_team_id
                player.update()
                print("------------------------------------")
                print(f"Sucess!! {player_name} has been transfered to {Team.find_in_dict(new_team_id).name}")
            except Exception as exc:
                print("------------------------------------")
                print("Error Transfering Player: ", exc)
        elif choice == "R" or choice == "r":
            print("------------------------------------")
            new = False
            players = Player.get_all()
            for player in players:
                print(player)
            print("------------------------------------")
            name = input("Type the name of the player you wish to remove: -> ")
            try: 
                player = Player.find_by_name(name.title())
                print("------------------------------------")
                print(f"Player {player.name} has announced their retirement!!!")
                player.delete()
            except Exception as exc:
                print("Error Removing Player: ", exc)
        elif choice == "B" or choice == "b":
            here = False
        else:
            new = False
            print("------------------------------------")
            print("Invalid choice")

def play_match_random():
    team1 = Team.random_team()
    team2 = team1
    while team1 == team2:
        team2 = Team.random_team()
    play_game(team1,team2)

def play_match_choose():
    print("------------------------------------")
    print_team_numbers()
    team1 = None
    while team1 == None:
        team1_id = input("Pick Home Team: -> ")
        team1 = Team.find_in_dict(team1_id)
    team2 = None
    while team2 == None:
        team2_id = input("Pick Away Team: -> ")
        while team1_id == team2_id:
            print("------------------------------------")
            team2_id = input("Please select a different away team than home team: -> ")
        team2 = Team.find_in_dict(team2_id)
    print("------------------------------------")
    play_game(team1, team2)


def records():
    teams = Team.point_board()
    print("------------------------------------")
    for team in teams: 
        print(f"{team.name} has {team.points} points!")

def create_team():
    print("------------------------------------")
    name = input("Type in new team name: -> ")
    location = input("Type in new team location: -> ")
    conference = input("Choose conference: 'West' or 'East' ")
    try:
        Team.create(name, location, conference, 0)
        print("------------------------------------")
        print(f"Yay!!! team {name} has been created")
    except Exception as exc:
        print("------------------------------------")
        print("Error making team:",  exc)

def create_player():
    player = None
    while player == None:
        name = input("Enter the new players name: -> ")
        position = input("Enter the new players position (1-11): -> ")
        number = input("Enter the new players number (0-99): -> ")
        print("------------------------------------")
        print_team_numbers()
        team_num = input("Enter an existing team number: -> ")
        team = Team.find_in_dict(team_num)
        try:
            player = Player.create(name,int(position),int(number),team.id)
            print("------------------------------------")
            print(f"Yay!!! The player {player.name} has signed with {team.name}!!")
        except Exception as exc:
            print("------------------------------------")
            print("Error making team", exc, ", --Try Again--")
            print("------------------------------------")

def print_team_numbers():
        num = 1
        print("Existing team numbers: ")
        teams = Team.get_all()
        for team in teams:
            print(f"{num}: {team.name}")
            num += 1
        print("------------------------------------")
    
def players_of():
        team = None
        while team == None:
            _id = input("Choose a team number to see its players: -> ")
            team = Team.find_in_dict(_id)
        print("------------------------------------")
        print(team.players())
        print("------------------------------------")

def play_game(team1,team2):
    winner = random.randint(1,3)
    if winner == 1:
        team1.points += 3
        team1.update()
        print("------------------------------------")
        print(f"HOME TEAM --{team1.name.upper()}-- DEFEATS AWAY TEAM --{team2.name.upper()}-- AND GAINS 3 POINTS!!")
    elif winner == 2:
        team2.points += 3
        team2.update()
        print("------------------------------------")
        print(f"AWAY TEAM --{team2.name.upper()}-- DEFEATS HOME TEAM --{team1.name.upper()}-- AND GAINS 3 POINTS!!")
    else:
        team1.points += 1
        team1.update()
        team2.points += 1
        team2.update()
        print("------------------------------------")
        print(f"HOME TEAM --{team1.name.upper()}-- DRAWS WITH AWAY TEAM --{team2.name.upper()}!! THEY BOTH GAIN 1 POINT!!")
