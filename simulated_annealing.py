import numpy as np

# Simulated Annealing algorithm
def simulated_annealing(initial_state, objective_function, neighborhood_operator, T_init, max_iter=20_000):
    t = 0
    current_state = initial_state
    T = T_init
    current_energy = objective_function(current_state)
    
    # Lists to store metrics for plotting
    objective_values = []
    temperatures = []
    accepted_moves = []
    
    while t < max_iter and current_energy != 0:
        # get neighbor 
        proposed_neighbor = neighborhood_operator(current_state)
        
        # check energy difference
        delta_E = objective_function(proposed_neighbor) - current_energy
        
        if delta_E < 0 or np.random.rand() < np.exp(-abs(delta_E) / T):
            current_state = proposed_neighbor
            current_energy = objective_function(current_state)
            accepted_moves.append(1)
        else:
            accepted_moves.append(0)
            
        # Record the current objective value and temperature
        objective_values.append(current_energy)
        temperatures.append(T)
        
        # Update temperature and iteration count
        T = 0.99 * T
        t += 1
    
    return current_state, objective_values, temperatures, accepted_moves
