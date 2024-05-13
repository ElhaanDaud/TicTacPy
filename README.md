# Tic Tac Toe Game

Tic Tac Toe is a classic two-player game where players take turns marking spaces in a 3x3 grid, aiming to be the first to get three of their symbols (either X or O) in a row, column, or diagonal.

## How to Play

1. Run the `tictac.py` file to start the game.

2. Click on any empty space in the grid to place your symbol (X or O).

3. The first player to get three of their symbols in a row, column, or diagonal wins the game.

4. If all spaces are filled without any player achieving a winning combination, the game ends in a draw.

5. Click the "Restart" button or close and reopen the game window to start a new game after a win or draw.

## Features

- **Graphical User Interface (GUI)**: The game features a simple GUI built using Tkinter, making it easy and intuitive to play.

- **Winning Notification**: When a player wins the game, a message box notifies the players of the winner (Player X or Player O).

- **Draw Detection**: The game detects when the board is full without any player winning, declaring the game as a draw.

- **Invalid Move Handling**: Players are notified with an error message if they attempt to make a move in an already occupied space.

## Logic Overview

- The game logic is implemented in `tictac.py`, which handles player turns, checking for winning combinations, detecting draws, and resetting the game board.

- The game board consists of nine buttons arranged in a 3x3 grid. Players click on these buttons to place their symbols (X or O) in the corresponding grid spaces.

- Winning combinations are checked after each move to determine if a player has won. The game checks for three symbols in a row, column, or diagonal.

## Customize

You can customize the game by modifying the following:

- **Styling**: Update the appearance of the game by modifying the button size, text font, colors, etc., in the Tkinter GUI.

- **Symbols**: Change the symbols used by players (X and O) by updating the `self.current_player` variable in the Python code.

