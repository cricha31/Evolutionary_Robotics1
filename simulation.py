# Creating new file for class simulation

# Imports
import pybullet as p
import pybullet_data
import constants as c
import time
# Import pyrosim
import pyrosim.pyrosim as pyrosim
# Importing other class files
from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self):
        # Connect to physics engine
        self.physicsClient = p.connect(p.GUI)

        # Set the search path for assets
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        # Add gravity
        p.setGravity(0, 0, c.GRAVITY, self.physicsClient)

        # Create world and robot instances
        self.world = WORLD()
        self.robot = ROBOT()

        # Prepare robot for simulation
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        """Run the simulation loop."""
        for t in range(c.TIMESTEPS):

            p.stepSimulation()  # Step physics simulation
            self.robot.Sense(t)   # Read sensor values
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(c.FRAME_RATE)  # Slow down for real-time visualization



    def __del__(self):

        p.disconnect()