# Simulated Annealing Applied to Sudoku Puzzles

<div align="center">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/sudoku_solution.gif" style="width: 80%;" alt="Sudoku Solution GIF" />
</div>

This project implements a **Simulated Annealing** (SA) algorithm to solve Sudoku puzzles, inspired by the paper **"Metaheuristics can solve Sudoku puzzles"** by Lewis (2007). The algorithm demonstrates a reliable approach to consistently find solutions to Sudoku puzzles using a metaheuristic optimization technique.

## Project Overview

The SA algorithm works by iteratively exploring the solution space and probabilistically allowing worse solutions to escape local minima. As the process progresses, the "temperature" parameter gradually decreases, refining the search. If a better solution isn't found within a set number of steps, a reheating mechanism is applied to help the search escape potential plateaus.

<div  align="center">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/output.png" alt="Sudoku Board Example" style="width: 60%;" />
</div>

### File Descriptions

- `notebook.ipynb` - A Jupyter Notebook demonstrating and visualizing the SA approach for solving Sudoku puzzles, with step-by-step explanations.
- `simulated_annealing.py` - Core implementation of the Simulated Annealing algorithm.
- `sudoku_solver.py` - Contains helper functions, the objective funciton, the nieghborhood operator, the delta evaluation function and the necessary Sudoku-specific logic required by the SA algorithm.

### Key Functions

- [`find_square`](sudoku_solver.py): Determines the 3x3 grid for a given cell.
- [`initial_candidate_sudoku`](sudoku_solver.py): Generates an initial candidate Sudoku solution.
- [`objective_function`](sudoku_solver.py): Computes the objective function value for a given Sudoku solution.
- [`neighborhood_operator`](sudoku_solver.py): Swaps two random cells in the same 3x3 grid of the Sudoku.
- [`delta_evaluation`](sudoku_solver.py): Evaluates the change in the objective function value after a swap operation.
- [`simulated_annealing`](simulated_annealing.py): Executes the Simulated Annealing algorithm.
- [`simulated_annealing_e`](simulated_annealing.py): Executes an enhanced version of the Simulated Annealing algorithm with delta evaluation.

### Visualization and Results

The results and visualizations can be found in the `notebook.ipynb` file. Open it with Jupyter Notebook to see step-by-step explanations and plots.

### Webpage 
Webpage where you can specify sudoku problem and parameters:
- [Webpage](https://bergione.pythonanywhere.com/) 

---

#### Reference

- Lewis, R. Metaheuristics can solve sudoku puzzles. J Heuristics 13, 387–401 (2007). DOI: https://doi.org/10.1007/s10732-007-9012-8
