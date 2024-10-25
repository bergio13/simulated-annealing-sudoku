# Importing the required libraries
import numpy as np

def find_square(i, j):
    return i // 3, j // 3

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


def objective_function(sudoku):
    """ The objective function is the sum of the number of repeated values in each row and column.
        The objective function is minimized when the sudoku is solved.
    
    Args:
        sudoku (np.array): The candidate solution to evaluate
    
    Returns:
        int: The objective function value
    """
    row_scores = []
    column_scores = []
    n = sudoku.shape[0]
    
    for i in range(n):
        row_scores.append(n - len(np.unique(sudoku[i, :])))
        column_scores.append(n - len(np.unique(sudoku[:, i])))
    return sum(row_scores) + sum(column_scores)


# Neighborhood operator to mutate the candidate solution by a small amount
def neighborhood_operator(sudoku, fixed_mask):
    """ The neighborhood operator swaps two random cells in the same 3x3 grid of the sudoku.

    Args:
        sudoku (np.array): The candidate solution to mutate
        fixed_mask (np.array): A binary mask indicating which cells are fixed

    Returns:
        tuple: The indices of the two cells that were swapped
    """
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

def delta_evaluation(sudoku, swap1, swap2):
    """ Evaluate the change in the objective function value after a swap operation.

    Args:
        sudoku (np.array): The candidate solution to evaluate

    Returns:
        int: The change in the objective function value
    """
    i, j  = swap1
    k, l = swap2
    n = sudoku.shape[0]
    
    # Compute the row and column scores differences
    row_score_after =   (n - len(np.unique(sudoku[i, :])))  + (n - len(np.unique(sudoku[k, :]))) 
    column_score_after =  (n - len(np.unique(sudoku[:, j]))) + (n - len(np.unique(sudoku[:, l])))
    
    sudoku[i, j], sudoku[k, l] = sudoku[k, l], sudoku[i, j]
    
    row_score_before =  (n - len(np.unique(sudoku[i, :]))) + (n - len(np.unique(sudoku[k, :])))
    column_score_before = (n - len(np.unique(sudoku[:, j]))) + (n - len(np.unique(sudoku[:, l])))
    
    row_score_diff = row_score_after - row_score_before
    column_score_diff = column_score_after - column_score_before
    
    
    sudoku[i, j], sudoku[k, l] = sudoku[k, l], sudoku[i, j]
    
    return row_score_diff + column_score_diff