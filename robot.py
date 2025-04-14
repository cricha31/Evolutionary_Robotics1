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
#from generate import Generate_Body as GB
class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.fitness = 0.0

        # Loads the robot body and prepares it for simulation.
        self.robotId = p.loadURDF("body1.urdf")  # Load robot URDF

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



    def Prepare_To_Act(self):
        '''Initialize the dictionary for motors'''
        self.motors = {}

        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)  # Create MOTOR instance

    def Sense(self, t):
        for sensor in self.sensors.values():  # Iterate over all SENSOR instances
            sensor.Get_Value(t)  # Call Get_Value() on each sensor to update its values

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                # Extract the value (desired angle) for this motor neuron
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange

                # Ensure the jointName is a decoded string, in case it's a byte string
                decoded_joint_name = jointName.decode("utf-8") if isinstance(jointName, bytes) else jointName

                self.motors[decoded_joint_name].Set_Value(self, desiredAngle)
                #jointName= jointName.decode("utf-8")

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Update_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]

        x = positionOfLinkZero[0]
        y = positionOfLinkZero[1]

        platform_half_width = 2.0
        alpha = 2.0
        beta = 1.0

        centered_penalty = beta * (abs(y) / platform_half_width)
        fitness_step = alpha * x - centered_penalty

        self.fitness += fitness_step

    def Get_Fitness(self):
        avg_fitness = self.fitness / c.TIMESTEPS

        tmp_fitness_file = f"tmp{self.solutionID}.txt"
        with open(tmp_fitness_file, "w") as file:
            file.write(str(avg_fitness))
        time.sleep(0.01)

        os.rename(f"tmp{self.solutionID}.txt", f"fitness{self.solutionID}.txt")