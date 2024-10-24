import numpy as np
import random

def is_valid(sudoku, row, col, num):
    """ Check if a number can be placed in the given row and column. """
    # Check the row and column
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
            
    # Check the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if sudoku[i][j] == num:
                return False
    return True

def solve_sudoku(sudoku):
    """ Solve the Sudoku puzzle using backtracking. """
    empty = find_empty(sudoku)
    if not empty:
        return True  # Solved

    row, col = empty
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0  # Backtrack

    return False

def find_empty(sudoku):
    """ Find an empty cell in the Sudoku grid. """
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return (i, j)
    return None

def generate_complete_sudoku():
    """ Generate a complete Sudoku grid. """
    sudoku = np.zeros((9, 9), dtype=int)
    
    for _ in range(17):  # Start with a fully filled grid
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(sudoku, row, col, num):
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        sudoku[row][col] = num
    
    solve_sudoku(sudoku)  # Fill the rest using backtracking
    return sudoku

def remove_numbers(sudoku, num_to_remove=40):
    """ Remove numbers from the completed Sudoku to create a puzzle. """
    removed = 0
    puzzle = sudoku.copy()
    
    while removed < num_to_remove:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:  # Remove only if not empty
            puzzle[row][col] = 0
            removed += 1
    
    return puzzle

def generate_random_sudoku(num_to_remove=60):
    """ Generate a random valid Sudoku puzzle. """
    complete_sudoku = generate_complete_sudoku()
    puzzle = remove_numbers(complete_sudoku, num_to_remove)
    return puzzle


def find_square(r, c):
    return(r//3, c//3)