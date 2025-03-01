import numpy as np
from simulated_annealing import simulated_annealing_e as sa_e
from functools import partial
import sudoku_solver

def solve_sudoku(grid):
    sudoku = np.array(grid)
    
    # Define a fixed mask to prevent changing the initial values
    fixed_mask = sudoku != 0
    sudoku_copy = np.copy(sudoku)
    # Initialize the initial candidate solution
    initial_solution = sudoku_solver.initial_candidate_sudoku(sudoku_copy)
    # Partial function to pass the fixed mask to the neighborhood operator
    neighborhood_operator_with_mask = partial(sudoku_solver.neighborhood_operator, fixed_mask=fixed_mask)
    final_solution, objective_values, temperatures, accepted_moves = sa_e(
        initial_solution, 
        sudoku_solver.objective_function,
        sudoku_solver.delta_evaluation,
        neighborhood_operator_with_mask, 
        T_init=60,
        cooling_rate=0.99,
        max_iter=20_000,
        reheat_threshold=500
    )
    solved_sudoku = final_solution.tolist()
    return solved_sudoku