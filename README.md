# Simulated Annealing Applied to Sudoku Puzzles

<div style="text-align: center;">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/sudoku_solution.gif" alt="Sudoku Solution GIF" />
</div>

This project implements a **Simulated Annealing** algorithm to solve Sudoku puzzles, inspired by the paper **"Metaheuristics can solve Sudoku puzzles"** by Lewis (2007). The algorithm demonstrates a reliable approach to consistently find solutions to Sudoku puzzles using a metaheuristic optimization technique.



## Project Overview

The algorithm works by iteratively exploring the solution space and probabilistically accepting worse solutions to escape local minima, gradually cooling down the "temperature" to refine the search. Additionaly, if no better solution is found after a certain number of iterations, reheating is performed to facilitate escaping local minima.

<div style="text-align: center;">
    <img src="https://github.com/bergio13/simulated-annealing-sudoku/blob/main/output.png" alt="Sudoku Board Example" style="width: 50%;" />
</div>

---
#### Reference
- Lewis, R. Metaheuristics can solve sudoku puzzles. J Heuristics 13, 387–401 (2007). DOI: https://doi.org/10.1007/s10732-007-9012-8
