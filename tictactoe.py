"""
Tic Tac Toe Player
"""

import math

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
    Retorna o player que tem o próximo turno no board
    """
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)

    return X if X_count == O_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

import copy

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Ação Inválida: Célula já ocupada")

    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Verifica linhas e colunas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == board[i][0] is not EMPTY:
            return board[0][i]
        if board[0][i] == board[1][i] == board[2][i] == board[0][i] is not EMPTY:
            return board[i][0]
    #Verifica Diagonais
        if board[0][0] == board[1][1] == board[2][2] == board[0][0] is not EMPTY:
            return board[0][j]
        if board[0][2] == board[1][1] == board[2][0] == board[0][2] is not EMPTY:
            return board[0][2]

        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    if all (cell is not EMPTY for row in board for cell in row):
        return True

    return False    
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
