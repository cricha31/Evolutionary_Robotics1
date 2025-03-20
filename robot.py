# Creating new file for class robot

#Imports
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c  # Import constants
import os
# Importing other files
from sensor import SENSOR
from motor import MOTOR
import time
from pyrosim.neuralNetwork import NEURAL_NETWORK
from generate import Generate_Body as GB
class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        GB()

        # Loads the robot body and prepares it for simulation.
        self.robotId = p.loadURDF("body.urdf")  # Load robot URDF

        # Prepare robot for simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors for all links
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

        brain_filename = f"brain{solutionID}.nndf"
        self.nn = NEURAL_NETWORK(brain_filename)

        # Delete the brain file after it has been read
        if os.name == "nt":  # Windows
            os.system(f"del {brain_filename}")
        else:  # Mac/Linux
            os.system(f"rm {brain_filename}")
    def Prepare_To_Sense(self):
        """Initialize the dictionary for sensors."""
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)   # Create SENSOR instance

    def Sense(self, t):
        for sensor in self.sensors.values():  # Iterate over all SENSOR instances
            sensor.Get_Value(t)  # Call Get_Value() on each sensor to update its values

    def Prepare_To_Act(self):
        '''Initialize the dictionary for motors'''
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)  # Create MOTOR instance


    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                # Extract the value (desired angle) for this motor neuron
                desiredAngle = self.nn.Get_Value_Of(neuronName)

                self.motors[jointName].Set_Value(self, desiredAngle)
                jointName= jointName.decode("utf-8")

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        # Get the state of the first link (link zero)
        stateOfLinkZero = p.getLinkState(self.robotId, 0)

        # Get the state of the first link (link zero)
        positionOfLinkZero = stateOfLinkZero[0]

        # Extract the x coordinate (first element) from positionOfLinkZero
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        # Write the x coordinate to a file (fitness.txt)
        tmp_fitness_file = f"tmp{self.solutionID}.txt"
        with open(tmp_fitness_file, "w") as file:
            file.write(str(xCoordinateOfLinkZero))  # Convert to string and write to file
        time.sleep(0.01)

        os.rename("tmp" + str(self.solutionID) + ".txt", "fitness" + str(self.solutionID) + ".txt")



