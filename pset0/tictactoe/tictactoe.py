"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Check if action is within the bounds of the board
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
        raise ValueError("Action is out of bounds")

    # Check if the clicked cell is already occupied
    if board[i][j] is not EMPTY:
        raise ValueError("Cell is already occupied")
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for winner horizontally
    for row in board:
        if (row[0] == row[1] == row[2]) and row[0] is not EMPTY:
            return row[0]

    # Check for winner vertically
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not EMPTY:
            return board[0][col]


    # Check diagonals for winner (left to right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Check diagonals for winner (right to left)
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] is not EMPTY:
        return board[2][0]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move

def max_value(board):
    """
    Function tries to maximize X's value
    """
    if terminal(board):
        return utility(board), None

    value = float('-inf')
    move = None
    for action in actions(board):
        aux, act = min_value(result(board, action))
        if aux > value:
            value = aux
            move = action
            if value == 1:
                return value, move

    return value, move


def min_value(board):
    """
    Function tries to minimize O's value
    """
    if terminal(board):
        return utility(board), None

    value = float('inf')
    move = None
    for action in actions(board):
        aux, act = max_value(result(board, action))
        if aux < value:
            value = aux
            move = action
            if value == -1:
                return value, move

    return value, move
