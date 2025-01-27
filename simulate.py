# -*- coding: utf-8 -*-
# Cole Richardson

# Imports
import pybullet_data
import pybullet as p
import time

# Connect to the physics engine and open the GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity to simulation
p.setGravity(0,0,-9.8,physicsClient)

# Add a floor
planeId = p.loadURDF("plane.urdf")


# Simulating a box
p.loadSDF("5x5_towers.sdf")

# Run the simulation for 1000 steps
for i in range(1000):
    p.stepSimulation()  # Step the simulation forward
    time.sleep(1/60)  # Slow down the simulation to ~60 FPS
    print(i)  # Print the iteration number to track the progress

# Disconnect the physics engine
p.disconnect()
