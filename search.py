import os
from hillclimber import HILL_CLIMBER

# Generate a loop that runs twice
'''for _ in range(5):
    # Generate robot with a new random set of synaptic weights
    os.system("python generate.py")

    # Simulate the robot's behavior with the generated weights
    os.system("python simulate.py")'''

# Create an instance of HILL_CLIMBER
hc = HILL_CLIMBER()

# Call the Evolve() method
hc.Evolve()
hc.Show_Best()