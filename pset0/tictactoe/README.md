# Tic-Tac-Toe with AI

This project is part of **CS50’s Introduction to Artificial Intelligence with Python**, specifically for **Problem Set 0: Tic-Tac-Toe**. The project implements a graphical Tic-Tac-Toe game where a user can play against an AI opponent. The AI uses the **Minimax algorithm** to always make the optimal move, ensuring that it never loses.

---

## Project Overview

The project consists of two main components:

1. **Game Logic (`tictactoe.py`)**: Implements the core game logic, including functions for determining valid moves, checking for a winner, and using the Minimax algorithm for optimal decision-making.
2. **Graphical Interface (`runner.py`)**: A graphical user interface (GUI) using **Pygame** that allows users to play Tic-Tac-Toe against the AI.

---

## Files in the Repository

1. **`tictactoe.py`**: Contains all the core functions for managing the game state and implementing the Minimax algorithm.
2. **`runner.py`**: Uses Pygame to create a GUI for playing the game.
3. **`OpenSans-Regular.ttf`**: Font file used for rendering text in the GUI.
4. **Pygame Data**: The project requires **Pygame** for the graphical interface.

---

## How the Program Works

1. **Startup**:
   - The game starts by displaying a menu where the user can choose to play as **X** or **O**.
   
2. **Gameplay**:
   - The user takes turns with the AI.
   - The AI always plays optimally using the Minimax algorithm.
   - The game ends when a player wins or when there is a tie.

3. **Endgame**:
   - Once the game is over, the user has the option to play again.

---

## Minimax Algorithm

The **Minimax algorithm** ensures that the AI makes the optimal move at every step, either:

- **Maximizing its chances of winning** (if playing as **X**).
- **Minimizing its chances of losing** (if playing as **O**).

The algorithm explores all possible moves recursively to determine the best outcome for each player.

### Key Functions

- **`max_value(board)`**: Tries to maximize the score for **X** by selecting the move that leads to the highest utility.
- **`min_value(board)`**: Tries to minimize the score for **O** by selecting the move that leads to the lowest utility.
