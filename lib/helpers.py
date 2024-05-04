# lib/helpers.py
from models.player import Player
from models.team import Team
import random

def exit_program():
    print("Goodbye!")
    exit()

def team_menu():
    new = True
    here = True
    while here == True:
        if new:
            print("Welcome To The Teams Hub!")
        print("Please select an option:")
        print("L. List All Teams")
        print("C. Create New Team")
        print("A. List All Players Of A Team")
        print("P. View Team Points")
        print("B. Back To Main Menu")
        choice = input("-> ")
        if choice == "L" or choice == "l":
            new = False
            teams = Team.get_all()
            for team in teams: 
                print(team)
        elif choice == "C" or choice == "c":
            new = False
            create_team()
        elif choice == "A" or choice == "a":
            new = False
            players_of()
        elif choice == "P" or choice == "p":
            new = False
            records()
        elif choice == "B" or choice == "b":
            here = False




def player_menu():
    new = True
    here = True
    while here == True:
        if new:
            print("Welcome To The Players Hub")
        print("Please select an option:")
        print("L. List All Players")
        print("C. Create New Player")
        print("T. Transfer A Player")
        print("B. Back To Main Menu")
        choice = input("-> ")
        if choice == "L" or choice == "l":
            new = False
            players = Player.get_all()
            for player in players:
                print(player)
        elif choice == "C" or choice == "c":
            new = False
            create_player()
        elif choice == "T" or choice == "t":
            new = False
            print_team_numbers()
            players_of()
            player_name = input("Type Player Name To Transfer: -> ")
            player = Player.find_by_name(player_name)
            new_team = int(input("Select Team Number Of New Team: -> "))
            try:
                player.team_id = new_team
                player.update()
                print(f"Sucess!! {player_name} has been transfered to team number {new_team}")
            except Exception as exc:
                print("Error Transfering Player: ", exc)
        elif choice == "B" or choice == "b":
            here = False

def play_match_random():
    team1 = Team.random_team()
    team2 = team1
    while team1 == team2:
        team2 = Team.random_team()
    play_game(team1,team2)

def play_match_choose():
    print_team_numbers()
    team1_id = input("Pick Home Team: -> ")
    team1 = Team.find_by_id(team1_id)
    team2_id = input("Pick Away Team: -> ")
    while team1_id == team2_id:
        team2_id = input("Please select a different away team than home team: -> ")
    team2 = Team.find_by_id(team2_id)
    play_game(team1, team2)


def records():
    teams = Team.point_board()
    for team in teams: 
        print(f"{team.name} has {team.points} points!")

def create_team():
    name = input("Type in new team name: -> ")
    location = input("Type in new team location: -> ")
    conference = input("Choose conference: 'West' or 'East' ")
    try:
        Team.create(name, location, conference, 0)
        print(f"Yay!!! team {name} has been created")
    except Exception as exc:
        print("Error making team:",  exc)

def create_player():
    name = input("Enter the new players name: -> ")
    position = input("Enter the new players position (1-11): -> ")
    number = input("Enter the new players number (0-99): -> ")
    print_team_numbers()
    team = input("Enter an existing team number: -> ")
    try:
        player = Player.create(name,int(position),int(number),int(team))
        print(f"Yay!!! The player {player} has been created and added to team {team}")
    except Exception as exc:
        print("Error making team", exc)

def print_team_numbers():
        print("Existing team numbers: ")
        teams = Team.get_all()
        for team in teams:
            print(f"{team.id}: {team.name}")
    
def players_of():
        _id = input("Choose a team number to see its players: -> ")
        team = Team.find_by_id(_id)
        print(team.players()) if team else print(f"Sorry, team number {_id} does not yet exist")

def play_game(team1,team2):
    winner = random.randint(1,3)
    if winner == 1:
        team1.points += 3
        team1.update()
        print(f"HOME TEAM {team1.name} DEFEATS AWAY TEAM {team2.name} AND GAINS 3 POINTS!!")
    elif winner == 2:
        team2.points += 3
        team2.update()
        print(f"HOME TEAM {team2.name} DEFEATS AWAY TEAM {team1.name} AND GAINS 3 POINTS!!")
    else:
        team1.points += 1
        team1.update()
        team2.points += 1
        team2.update()
        print(f"HOME TEAM {team1.name} DRAWS WITH AWAY TEAM {team2.name}!! THEY BOTH GAIN 1 POINT!!")