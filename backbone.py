# Define the motor operation steps for each axis
z_max_measurement = [
    ('STEP_Z_MAX', 11, True) # Example command, 11 times, collect data
]

z_steps_transition = [
    ('STEP_Z_TRANS', 2, True) # Example command, 2 times, no data collection
]

z_min_measurement = [
    ('STEP_Z_MIN', 10, True) # Example command, 10 times, collect data
]

transition_z_to_x = [
    ('STEP_Z_TO_X_1', 1, False), # Example command, 1 time, no data collection
    ('STEP_Z_TO_X_2', 5, False), # Example command, 5 times, no data collection
    ('STEP_Z_TO_X_3', 6, False) # Example command, 6 times, no data collection
]

x_max_measurement = [
    ('STEP_X_MAX', 11, True) # Example command, 11 times, collect data
]

x_steps_transition = [
    ('STEP_X_TRANS', 2, True) # Example command, 2 times, no data collection
]

x_min_measurement = [
    ('STEP_X_MIN', 10, True) # Example command, 10 times, collect data
]

transition_x_to_y = [
    ('STEP_X_TO_Y_1', 1, False), # Example command, 1 time, no data collection
    ('STEP_X_TO_Y_2', 1, False) # Example command, 1 time, no data collection
]

y_max_measurement = [
    ('STEP_Y_MAX', 11, True) # Example command, 11 times, collect data
]

y_steps_transition = [
    ('STEP_Y_TRANS', 2, True) # Example command, 2 times, no data collection
]

y_min_measurement = [
    ('STEP_Y_MIN', 10, True) # Example command, 10 times, collect data    
]

transition_to_initial = [
    ('STEP_TO_INITIAL_1', 1, False), # Example command, 1 time, no data collection
    ('STEP_TO_INITIAL_2', 6, False) # Example command, 6 times, no data collection
]
