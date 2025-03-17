import os
# Generate a loop that runs twice
for _ in range(5):
    # Generate robot with a new random set of synaptic weights
    os.system("python generate.py")

    # Simulate the robot's behavior with the generated weights
    os.system("python simulate.py")