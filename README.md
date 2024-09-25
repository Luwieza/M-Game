# BATTLESHIP GAME PROJECT 3

!responsive
!game

Table of Contents

- Introduction
- User Experience (UX)
    - User Stories
- Gameplay Instructions
- Features
    - Current Features
    - Planned Features
- Design
- Testing
- Deployment
- Acknowledgments

Introduction
Check out the live project here

This Battleship game serves as Portfolio Project 3 - Python Essentials for the Diploma in Full Stack Software Development at Code Institute. The focus of this project is to develop a command-line application that facilitates the management of a common dataset within a specific domain.

The Battleship game is implemented as a Python Terminal Game, hosted on Heroku.

In this game, players engage on grids where each side has a fleet of battleships hidden from their opponent. The objective is to call shots at the opposing player's ships and eventually eliminate their fleet. The application features a functioning battleship game in which a single player competes against the computer on a 9 x 9 grid. Players' ships are pre-positioned on the board when the game initiates, and helpful information is presented throughout gameplay. The upper board displays the player's ship positions and their attempts, while the lower board records their guessing history.

Victory goes to the player who successfully sinks all of the rival's ships first!

User Experience (UX)
User Stories:
- As a user, I want an introductory screen that features the game's name.
- As a user, I expect the computer to generate boards concealing the ships.
- As a user, I desire to have the board visible to track hits and misses.
- As a user, I seek to view the game board to monitor my progress.
- As a user, I want both boards available to access all game information I need to play.
- As a user, I wish to know whose turn is next to manage gameplay flow.
- As a user, I want to know the winner of the game.

Gameplay Instructions

Upon starting the game and inputting the player’s name, the user can read the instructions and view a chart detailing the ship sizes. Following the placement of ships on the game board, the player attempts to guess the locations of the enemy fleet on the computer's board. The game concludes when either the player or the computer successfully identifies all enemy ships.

This game is inspired by the classic https://en.wikipedia.org/wiki/Battleship_(game), allowing for a single-player experience (human versus computer).

# Features
## Existing Features

Features
Current Features

- An introductory message and graphic that appear when the game begins:
!features_01

- A prompt for the player to input their name.
!features_03

- Additional text displaying the loading status of the game.
!features_04

- An introduction that outlines the game instructions.
!features_05

- Display of both the player’s game board and the computer’s game board.
!features_07
!features_08

- The player can make guesses to find out where the ships are on the computer’s board.
!features_11

- Error-checking mechanisms to handle invalid input:
!features_12
!features_13

- A game over notification to indicate the end of the game.
!features_14

In this game, players interact with two game boards. First, they must set up their ships on one board and then attempt to guess the locations of the ships placed on the opponent's board.

!board-game !game_board

Guessed ships are denoted with a '★', while missed shots are indicated with a '-'.

Planned Features
- Introduce different sizes for the ships.

Design
- Flow Charts

The diagram below illustrates the function structure found in the run.py file:

!flowcharts

Testing

Comprehensive testing information can be found in a dedicated testing.md file.

Deployment

- The application has been deployed on Heroku. The deployment steps are as follows:
    - Log in to Heroku.
    - Select "Create New App" in the Heroku dashboard.
    - Enter the desired app name.
    - Choose the app’s region.
    - Go to the Settings tab.
    - Under 'Config Vars', add 'PORT' as the key and '5432' as its value.
    - In 'Buildpacks', click 'Add buildpack' and select both Python and Node.js.
    - From the top navigation, select "Deploy".
    - Then, connect to GitHub.
    - Enter the name of your GitHub repository and select "Search".
    - Click the connect button.
    - Under "Manual Deploy", choose the option to 'Deploy Branch'.
    - Finally, click 'Open App' on the right side of the screen, which should open the app in a new tab.
    - The live link can be accessed here - https://m-game-48e6e2a0f27b.herokuapp.com/

Acknowledgments

- Python Value Error - This resource helped in writing the code for handling value errors in Python.

- Project 3 Template - This template was utilized to assist in structuring the Python project.
- PEP8 - This website was used to check my code against PEP8 standards.
- Background Image - A Ship - This link was referenced for the background image design.
- Symbols for Loading and Ships - This site provided symbols for ship representation and loading animation.
- ASCII Art Archive - This resource was helpful for generating the drawing associated with the instructions.
- Battleship Game - YouTube - This tutorial was followed, and certain JavaScript code was adapted for use in my game.
- Lucid Chart - This tool was used to create the diagram illustrating the structure of the functions in the run.py file.



