# lib/helpers.py
from models.player import Player
from models.team import Team
#from .cli import (main)

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
        print("L. List all teams")
        print("C. Create new teams")
        print("A. List all players of a team")
        print("P. View Team Points")
        print("B. Back to main menu")
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
            _id = input("Choose a team number to see its players: -> ")
            team = Team.find_by_id(_id)
            print(team.players()) if team else print(f"Sorry, team number {_id} does not yet exist")
        elif choice == "P" or choice == "p":
            new = False
            teams = Team.point_board()
            for team in teams: 
                print(f"{team.name} has {team.points} points!")
        elif choice == "B" or choice == "b":
            here = False




def player_menu():
    pass

def play_match_random():
    pass

def play_match_choose():
    pass

def records():
    pass

def create_team():
    name = input("Type in new team name: -> ")
    location = input("Type in new team location: -> ")
    conference = input("Choose conference: 'West' or 'East' ")
    try:
        team = Team.create(name, location, conference, 0)
        print(f"Yay!!! team {name} has been created")
    except Exception as exc:
        print("Error making team: exc")
    