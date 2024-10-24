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
    new_sudoku = np.copy(sudoku)
    n = sudoku.shape[0]
    
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
    new_sudoku[i, j], new_sudoku[k, l] = new_sudoku[k, l], new_sudoku[i, j]
    return new_sudoku

############################################################################
if __name__ == '__main__':
    
#    sudoku = np.array([
#        [5, 3, 0, 0, 7, 0, 0, 0, 0],
#        [6, 0, 0, 1, 9, 5, 0, 0, 0],
#        [0, 9, 8, 0, 0, 0, 0, 6, 0],
#        [8, 0, 0, 0, 6, 0, 0, 0, 3],
#        [4, 0, 0, 8, 0, 3, 0, 0, 1],
#        [7, 0, 0, 0, 2, 0, 0, 0, 6],
#        [0, 6, 0, 0, 0, 0, 2, 8, 0],
#        [0, 0, 0, 4, 1, 9, 0, 0, 5],
#        [0, 0, 0, 0, 8, 0, 0, 7, 9]
#    ])
    
    # Generate a random Sudoku puzzle
    sudoku = generate_random_sudoku()
    
    # Define a fixed mask to prevent changing the initial values
    fixed_mask = sudoku != 0
    
    # Partial function to pass the fixed mask to the neighborhood operator
    neighborhood_operator_with_mask = partial(neighborhood_operator, fixed_mask=fixed_mask)
    
    # Initialize the initial candidate solution
    initial_solution = initial_candidate_sudoku(sudoku)
    
    # Apply the Simulated Annealing algorithm to solve the Sudoku puzzle
    final_solution, objective_values, temperatures, accepted_moves = sa(
        initial_solution, 
        objective_function, 
        neighborhood_operator_with_mask, 
        T_init=50,
        max_iter=30_000
    )

    
    # Print the initial and final solutions
    print("Generated sudoku:")
    print(sudoku)
    
    print("Initial Candidate Solution:")
    print(initial_solution)
    
    print("Objective Function Value:")
    print(objective_function(initial_solution))

    print("Simulated Annealing Result:")
    print(final_solution)
    
    print("Objective Function Value After Solving:")
    print(objective_function(final_solution))

    ############################################################################
    # Plotting the results
    # Create a figure with a 2x2 grid for subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 7))

    # Plot 1: Rejected Moves
    axs[0, 0].plot(np.cumsum(accepted_moves)/sum(accepted_moves), label='Acceptance', color='slateblue')
    axs[0, 0].set_xlabel('Iteration')
    axs[0, 0].set_ylabel('P(Acceptance)')
    axs[0, 0].set_title('Cumulative Acceptance Probability')
    axs[0, 0].legend()
    axs[0, 0].grid(visible=True, color='grey', linestyle='--', linewidth=0.5)

    # Plot 2: Final Sudoku Solution
    cax = axs[0, 1].imshow(initial_solution, cmap='Set1', interpolation='nearest')
    axs[0, 1].set_title('Initial Sudoku Configuration')
    plt.colorbar(cax, ax=axs[0, 1], label='Cell Values')
    axs[0, 1].set_xticks(range(9))
    axs[0, 1].set_yticks(range(9))
    axs[0, 1].set_xticklabels([])
    axs[0, 1].set_yticklabels([])
    for (i, j), val in np.ndenumerate(initial_solution):
        axs[0, 1].text(j, i, int(val), ha='center', va='center', 
                       color='black' if fixed_mask[i, j] else 'white', fontsize=12)
    axs[0, 1].grid(visible=True, color='grey', linestyle='--', linewidth=0.5)

    # Plot 3: Objective Function Value and Temperature
    ax1 = axs[1, 0]  # Objective function value
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel('Objective Function Value', color='blue')
    ax1.plot(objective_values, color='blue', label='Objective Function Value')
    ax1.tick_params(axis='y', labelcolor='blue')
    # Secondary axis for temperature
    ax2 = ax1.twinx()
    ax2.set_ylabel('Temperature', color='red')
    ax2.plot(temperatures, color='red', label='Temperature', alpha=0.7)
    ax2.tick_params(axis='y', labelcolor='red')

    fig.tight_layout() 
    plt.title('Objective Function Value and Temperature Over Iterations')
    plt.grid(visible=True, color='grey', linestyle='--', linewidth=0.5)

    
    # Plot 4: Final Sudoku Solution
    cax1 = axs[1, 1].imshow(final_solution, cmap='Set1', interpolation='nearest')
    axs[1, 1].set_title('Final Sudoku Solution')
    plt.colorbar(cax1, ax=axs[1, 1], label='Cell Values')
    axs[1, 1].set_xticks(range(9))
    axs[1, 1].set_yticks(range(9))
    axs[1, 1].set_xticklabels([])
    axs[1, 1].set_yticklabels([])
    for (i, j), val in np.ndenumerate(final_solution):
        axs[1, 1].text(j, i, int(val), ha='center', va='center', 
                       color='black' if fixed_mask[i, j] else 'white', fontsize=12)    
    axs[1, 1].grid(visible=True, color='grey', linestyle='--', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()
