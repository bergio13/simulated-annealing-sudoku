# Importing the required libraries
import numpy as np
import matplotlib.pyplot as plt
from sudoku_generator import generate_random_sudoku, find_square
from simulated_annealing import simulated_annealing as sa
from functools import partial

# Objective function
def objective_function(sudoku):
    row_scores = []
    column_scores = []
    n = sudoku.shape[0]
    
    for i in range(n):
        row_scores.append(n - len(np.unique(sudoku[i, :])))
        column_scores.append(n - len(np.unique(sudoku[:, i])))
    return sum(row_scores) + sum(column_scores)

#def delta_eval(sudoku, swap_pos1, swap_pos2):
#    i, j = swap_pos1
#    k, l = swap_pos2
#    n = sudoku.shape[0]
#    
#    # Calculate the row and column scores before the swap
#    row_score_after = n - len(np.unique(sudoku[i, :])) + n - len(np.unique(sudoku[k, :]))
#    column_score_after = n - len(np.unique(sudoku[:, j])) + n - len(np.unique(sudoku[:, l]))
#    
#    # Swap the values
#    sudoku[i, j], sudoku[k, l] = sudoku[k, l], sudoku[i, j]
#    
#    # Calculate the row and column scores after the swap
#    row_score_before = n - len(np.unique(sudoku[i, :])) + n - len(np.unique(sudoku[k, :]))
#    column_score_before = n - len(np.unique(sudoku[:, j])) + n - len(np.unique(sudoku[:, l]))
#    
#    # Calculate the change in the objective function
#    delta_E = (row_score_after + column_score_after) - (row_score_before + column_score_before)
#    
#    # Revert the swap
#    sudoku[i, j], sudoku[k, l] = sudoku[k, l], sudoku[i, j]
#    return delta_E


# Function to compute an initial candidate solution
def initial_candidate_sudoku(sudoku):
    sudoku_copy = np.copy(sudoku) 
    n = sudoku.shape[0]
    
    for i in range(n):
        for j in range(n):
            # Fill empty cells with random values
            if sudoku_copy[i, j] == 0:
                # Ensure the value is not already in the same 3x3 grid
                r, c = find_square(i, j)
                sudoku_copy[i, j] = np.random.choice([x for x in range(1, 10) if x not in sudoku_copy[r * 3:r * 3 + 3, c * 3:c * 3 + 3]])
    return sudoku_copy


# Neighborhood operator to mutate the candidate solution by a small amount
def neighborhood_operator(sudoku, fixed_mask):
    n = sudoku.shape[0]
    
    # Randomly select two cells to swap
    i, j = np.random.randint(0, n, 2)
    # Ensure we don't select a fixed cell
    while fixed_mask[i, j]:  
        i, j = np.random.randint(0, n, 2)
        
    r,c = find_square(i,j)
    k, l = np.random.randint(r * 3, r * 3 + 3), np.random.randint(c * 3, c * 3 + 3)
    # Ensure we don't select a fixed cell or the same cell
    while (k, l) == (i, j) or fixed_mask[k, l]:
        k, l = np.random.randint(r * 3, r * 3 + 3), np.random.randint(c * 3, c * 3 + 3)
    
    # Swap the values    
    sudoku[i, j], sudoku[k, l] = sudoku[k, l], sudoku[i, j]
    return (i, j), (k, l)