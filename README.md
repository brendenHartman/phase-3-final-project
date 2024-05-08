# Phase 3 CLI+ORM Project

## Introduction

This project is a basic command line interface that simulates a soccer league with user interactibility. Create your own teams and players and watch them battle for league point supremacy 

directory structure:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── player.py
    │   └── team.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

## Usage

To set up the cli, run the commands:

```console
pipenv install
pipenv shell
```

---

Then run the command python lib/cli.py to run the cli. (make sure you have python installed on your machine)

## Functionality

The 'cli.py' file that you will run includes the basic main menu of the cli and print the different options you can choose to interact with the db. The first prompt will allow you to seed the database to add basic data to the db to work with.

In this file you will see that every option is paired with a helper function imported from the helper file. These functions are the actual handlers of the functionality of that option, but only when it comes to the printing and user side of the functionality. 

The helper functions call on functions in the team and player model files to actually manipulate the database and create / delete data etc.
All prompts in this cli show useful responsive messages when an invalid value is inputed by the user.

The main menu for this cli is where you can play games and pit teams against eachother, as well as exit the cli by choosing '0'.
The main menu also includes the navigation to the team and player hubs. 

![alt text](<Screenshot (181).png>)

1: Navigates to the Teams Hub

2: Navigates to the Players Hub

3: Plays a random match and prints the results

4: Plays a match where the user decides the home and away teams facing eachother

5: Prints out every teams points in desc order with the team with the most points (gained by playing games in the main menu) on top to simulate a league table

0: Exits the CLI and gives a 'goodbye!' prompt

### Teams Hub

The teams hub has the following options: 

![alt text](<Screenshot (183).png>)

L or l: Prints out all teams to the terminal

C or c: Prompts the user to input data for a team they would like to create

D or d: Lets the user delete a team and all of its players

A or a: Lets the user choose a team and prints all of the players of that team

P or p: Prints out every teams points in desc order with the team with the most points (gained by playing games in the main menu) on top to simulate a league table

B or b: Returns the user to the main menu

### Players Hub

This menu has the following options: 

![alt text](<Screenshot (184).png>)

L or l: Prints out all players to the terminal

C or c: Prompts the user to input data for a player they would like to create

T or t: Lets the user transfer a player from one team to another of their choice

R or r: Lets the user delete an existing player

B or b: Returns the user to the main menu

## Collaboration

This project is solo work for FlatIron School Phase 3 Cirriculum and as such is not open to collaboration at this time. 


