# Simulated Annealing Applied to Sudoku Puzzles

<div align="center">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/sudoku_solution.gif" style="width: 80%;" alt="Sudoku Solution GIF" />
</div>

This project implements a **Simulated Annealing** (SA) algorithm to solve Sudoku puzzles, inspired by the paper **"Metaheuristics can solve Sudoku puzzles"** by Lewis (2007). The algorithm demonstrates a reliable approach to consistently find solutions to Sudoku puzzles using a metaheuristic optimization technique.



## Project Overview

The SA algorithm works by iteratively exploring the solution space and probabilistically allowing worse solutions to escape local minima. As the process progresses, the "temperature" parameter gradually decreases, refining the search. If a better solution isn't found within a set number of steps, a reheating mechanism is applied to help the search escape potential plateaus.

<div  align="center">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/output.png" alt="Sudoku Board Example" style="width: 50%;" />
</div>

### File Descriptions
- `notebook.ipynb` - A Jupyter Notebook demonstrating and visualizing the SA approach for solving Sudoku puzzles, with step-by-step explanations.
- `simulated_annealing.py` - Core implementation of the Simulated Annealing algorithm.
- `sudoku_solver.py` - Contains helper functions, the objective funciton, the nieghborhood operator and the necessary Sudoku-specific logic required by the SA algorithm.

---
#### Reference
- Lewis, R. Metaheuristics can solve sudoku puzzles. J Heuristics 13, 387–401 (2007). DOI: https://doi.org/10.1007/s10732-007-9012-8
