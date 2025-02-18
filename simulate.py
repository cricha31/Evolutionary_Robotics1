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

# Define motor control parameters for BackLeg
amplitudeBackLeg = numpy.pi / 4
frequencyBackLeg = 10
phaseOffsetBackLeg = 0

# Define motor control parameters for FrontLeg
amplitudeFrontLeg = numpy.pi / 4
frequencyFrontLeg = 10
phaseOffsetFrontLeg = numpy.pi  # Phase shifted by pi

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

# Generate sinusoidal motor control values
timesteps = 1000  # Number of simulation steps
backLegTargetAngles = amplitudeBackLeg * numpy.sin(frequencyBackLeg * numpy.linspace(0, 2 * numpy.pi, timesteps) + phaseOffsetBackLeg)
frontLegTargetAngles = amplitudeFrontLeg * numpy.sin(frequencyFrontLeg * numpy.linspace(0, 2 * numpy.pi, timesteps) + phaseOffsetFrontLeg)
# Save motor vector to file
os.makedirs("data", exist_ok=True)
numpy.save("data/backLegTargetAngles.npy", backLegTargetAngles)
numpy.save("data/frontLegTargetAngles.npy", frontLegTargetAngles)

#exit()

# Run the simulation for 1000 steps
for i in range(timesteps):
    p.stepSimulation()  # Step the simulation forward
    # create backleg and frontlet touch sensor
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    # make sinusoidal motors (1st motor)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_BackLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=backLegTargetAngles[i],

        maxForce=50)
    #  (2nd motor)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_FrontLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=-frontLegTargetAngles[i],

        maxForce=50)
    time.sleep(1/60)  # Slow down the simulation to ~60 FPS

# Disconnect the physics engine
p.disconnect()



# Save the dataset as a numpy .npy file
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)

# Save the dataset as a numpy .npy file
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)