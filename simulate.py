# -*- coding: utf-8 -*-
# Cole Richardson

# Imports
import pybullet as p
import time

# Connect to the physics engine and open the GUI
physicsClient = p.connect(p.GUI)

# Attempt to clean up simulation
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

# Potential spot to add in things to the simulation later

# Run the simulation for 1000 steps
for i in range(1000):
    p.stepSimulation()  # Step the simulation forward
    time.sleep(1/60)  # Slow down the simulation to ~60 FPS
    print(i)  # Print the iteration number to track the progress

# Disconnect the physics engine
p.disconnect()
