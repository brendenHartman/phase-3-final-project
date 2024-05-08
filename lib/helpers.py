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
            print("------------------------------------")
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
            print("------------------------------------")
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
            player_name = input("Type Player Name To Transfer: -> ")
            player = Player.find_by_name(player_name)
            new_team = int(input("Select Team Number Of New Team: -> "))
            try:
                player.team_id = new_team
                player.update()
                print("------------------------------------")
                print(f"Sucess!! {player_name} has been transfered to {Team.find_by_id(new_team).name}")
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
                player = Player.find_by_name(name)
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
    team1_id = input("Pick Home Team: -> ")
    team1 = Team.find_by_id(team1_id)
    team2_id = input("Pick Away Team: -> ")
    while team1_id == team2_id:
        print("------------------------------------")
        team2_id = input("Please select a different away team than home team: -> ")
    team2 = Team.find_by_id(team2_id)
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
    name = input("Enter the new players name: -> ")
    position = input("Enter the new players position (1-11): -> ")
    number = input("Enter the new players number (0-99): -> ")
    print_team_numbers()
    team = input("Enter an existing team number: -> ")
    try:
        player = Player.create(name,int(position),int(number),int(team))
        print("------------------------------------")
        print(f"Yay!!! The player {player.name} has signed with {team.name}!!")
    except Exception as exc:
        print("------------------------------------")
        print("Error making team", exc)

def print_team_numbers():
        print("Existing team numbers: ")
        teams = Team.get_all()
        for team in teams:
            print(f"{team.id}: {team.name}")
    
def players_of():
        _id = input("Choose a team number to see its players: -> ")
        team = Team.find_by_id(_id)
        print("------------------------------------")
        print(team.players()) if team else print(f"Sorry, team number {_id} does not yet exist")

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
        print(f"HOME TEAM --{team1.name.upper()}-- DRAWS WITH AWAY TEAM --{team2.name.upper()}!! THEY BOTH GAIN 1 POINT!!")
