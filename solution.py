import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time

class SOLUTION:
    def __init__(self, myID):
        self.weights = 2 * np.random.rand(3, 2) - 1  # this generates 3x2 matrix with random values between -1 and 1

        # Initialize the fitness attribute
        self.fitness = None

        self.myID = myID

    def Create_World(self):
        # Tell pyrosim the name of the file where the world will be stored
        pyrosim.Start_SDF("world.sdf")

        # Store box position and parameters
        pyrosim.Send_Cube(name="Box", pos=[-10, 0, 0.5], size=[1, 1, 1])

        # End the SDF generation
        pyrosim.End()

    def Generate_Body(self):
        # Start creating the robot description in URDF format
        pyrosim.Start_URDF("body.urdf")

        # Block dimensions
        length = 1
        width = 1
        height = 1

        # Create the root cube (Torso)
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])

        # Create Joint between Torso and BackLeg
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0.5, 0, 1])

        # Create BackLeg
        pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0, -0.5], size=[length, width, height])

        # Create joint between Torso and FrontLeg
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[-0.5, 0, 1])

        # Create FrontLeg
        pyrosim.Send_Cube(name="FrontLeg", pos=[-0.5, 0, -0.5], size=[length, width, height])

        # End the URDF generation
        pyrosim.End()

        # CAN ADD IN WORLD.SDF IF NEED TO ADD THE EXTRA BOX BUT IT IS BUILT INTO WORLD FILE ALREADY

    def Generate_Brain(self):
        # Start creating the brain neural network
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        # assign variables
        sensor_neurons = [0, 1, 2]  # IDs of sensor neurons
        motor_neurons = [0, 1]  # IDs of motor neurons

        # Generate synapses using nested loops
        for currentRow in sensor_neurons:  # Sensor neurons (0, 1, 2)
            for currentColumn in motor_neurons:  # Motor neurons (3, 4)
                weight = self.weights[currentRow][currentColumn]  # Generate a random weight in [-1,1]
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + 3, weight=weight)

        # End the URDF generation
        pyrosim.End()

    def Evaluate(self, directOrGui):
        # Generate the world, body, and brain, and send synaptic weights
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGui + " " + str(self.myID))

        # Now, read the fitness from the fitness file specific to the solution ID
        fitnessFileName = f"fitness{self.myID}.txt"  # dynamically create the file name based on the solution ID

        # Wait for the fitness file to exist
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)  # Sleep for 0.01 seconds before checking again

        # Now, read the fitness from the fitness.txt file
        with open(fitnessFileName, "r") as fitnessFile:  #open file
            fitnessValue = fitnessFile.read()  #read the fitness value as a string

        self.fitness = float(fitnessValue) #convert to float

        print(self.fitness)

    def Mutate(self):
        # Randomly choose a row (0, 1, or 2) to select a sensor neuron
        randomRow = random.randint(0, 2)
        # Randomly choose a column (0 or 1) to select a motor neuron
        randomColumn = random.randint(0, 1)

        old_value = self.weights[randomRow, randomColumn]  # store the old weight
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1  # assign new random value

    def Set_ID(self, newID):
        self.myID = newID