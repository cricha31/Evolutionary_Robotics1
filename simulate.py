# -*- coding: utf-8 -*-
# Cole Richardson

# Imports
import pybullet_data
import pybullet as p
import time
import numpy
# Import pyrosim
import pyrosim.pyrosim as pyrosim
# Import os
import os

# Connect to the physics engine and open the GUI
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Add gravity to simulation
p.setGravity(0,0,-9.8,physicsClient)

# Add a floor
planeId = p.loadURDF("plane.urdf")

# Store robot body
robotId = p.loadURDF("body.urdf")

# Simulating a box
p.loadSDF("world.sdf")

# Indicating which robot you want prepared for simulation
pyrosim.Prepare_To_Simulate(robotId)

# Create empty arrays to store data
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)

# Run the simulation for 1000 steps
for i in range(1000):
    p.stepSimulation()  # Step the simulation forward
    # create backleg and frontlet touch sensor
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(1/60)  # Slow down the simulation to ~60 FPS

# Disconnect the physics engine
p.disconnect()

# Print dataset1
print(backLegSensorValues)
# Print dataset2
print(frontLegSensorValues)

# Create the "data" directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the dataset as a numpy .npy file
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

# Save the dataset as a numpy .npy file
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)