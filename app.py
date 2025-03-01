from flask import Flask, render_template, request, jsonify
import numpy as np
from simulated_annealing import simulated_annealing_e
from functools import partial
import sudoku_solver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Get the sudoku grid from the request
        data = request.get_json()
        grid = data['grid']
        
        # Convert to numpy array
        sudoku = np.array(grid)
        
        # Define a fixed mask to prevent changing the initial values
        fixed_mask = sudoku != 0
        sudoku_copy = np.copy(sudoku)
        
        # Initialize the initial candidate solution
        initial_solution = sudoku_solver.initial_candidate_sudoku(sudoku_copy)
        
        # Partial function to pass the fixed mask to the neighborhood operator
        neighborhood_operator_with_mask = partial(sudoku_solver.neighborhood_operator, fixed_mask=fixed_mask)
        
        final_solution, objective_values, temperatures, accepted_moves = simulated_annealing_e(
            initial_solution, 
            sudoku_solver.objective_function,
            sudoku_solver.delta_evaluation,
            neighborhood_operator_with_mask, 
            T_init=60,
            cooling_rate=0.99,
            max_iter=20_000,
            reheat_threshold=500
        )
        
        # Check if the solution is valid
        if sudoku_solver.objective_function(final_solution) == 0:
            return jsonify({
                'status': 'success',
                'solution': final_solution.tolist(),
                'message': 'Puzzle solved successfully!'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Could not find a valid solution. Try a different puzzle or adjust parameters.'
            })
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error: {str(e)}'
        })

if __name__ == '__main__':
    app.run(debug=True)