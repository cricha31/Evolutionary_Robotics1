# Import pyrosim
import pyrosim.pyrosim as pyrosim
import random

def Create_World():
    # Tell pyrosim the name of the file where the world will be stored
    pyrosim.Start_SDF("world.sdf")

    # Store box position and parameters
    pyrosim.Send_Cube(name="Box", pos=[-10,0,0.5], size=[1,1,1])

    # End the SDF generation
    pyrosim.End()


def Generate_Body():

    pyrosim.Start_URDF("body.urdf")
    # Torso
    pyrosim.Send_Cube(name="Torso", pos=[0.0, 0.0, 1.0], size=[1, 1, 1])

    # Front leg
    # Upper leg
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1],
                       jointAxis="1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])
    # Lower leg
    pyrosim.Send_Joint(name="FrontLeg_Lower", parent="FrontLeg", child="FrontLowerLeg", type="revolute",
                       position=[0, 1, 0], jointAxis="1 0 0")  # Rotates forward-backward
    pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

    # Back Leg
    # Upper
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1],
                       jointAxis="1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])
    # Lower
    pyrosim.Send_Joint(name="BackLeg_Lower", parent="BackLeg", child="BackLowerLeg", type="revolute",
                       position=[0, -1, 0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

    # Left Leg
    # Upper
    pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                       position=[-0.5, 0, 1], jointAxis="0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
    # Lower
    pyrosim.Send_Joint(name="LeftLeg_Lower", parent="LeftLeg", child="LeftLowerLeg", type="revolute",
                       position=[-1, 0, 0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

    # Right leg
    # Upper
    pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                       position=[0.5, 0, 1], jointAxis="0 1 0")  # Rotates forward-backward
    pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
    # Lower
    pyrosim.Send_Joint(name="RightLeg_Lower", parent="RightLeg", child="RightLowerLeg", type="revolute",
                       position=[1, 0, 0], jointAxis="1 0 0")
    pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

    # Finalize the URDF file
    pyrosim.End()


def Generate_Brain():
    # Start generating the URDF file
    pyrosim.Start_NeuralNetwork("brain.nndf")

    # Create sensor neurons
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
    pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
    pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
    pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
    pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
    pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
    pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")

    # Create motor neurons
    pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")
    pyrosim.Send_Motor_Neuron(name=13, jointName="FrontLeg_Lower")
    pyrosim.Send_Motor_Neuron(name=14, jointName="BackLeg_Lower")
    pyrosim.Send_Motor_Neuron(name=15, jointName="LeftLeg_Lower")
    pyrosim.Send_Motor_Neuron(name=16, jointName="RightLeg_Lower")

    # assign variables
    sensor_neurons = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # IDs of sensor neurons
    motor_neurons = [9, 10, 11, 12, 13, 14, 15]  # IDs of motor neurons

    # Generate synapses using nested loops
    for i in sensor_neurons:
        for j in motor_neurons:
            pyrosim.Send_Synapse(sourceNeuronName=i, targetNeuronName=j, weight=random.uniform(-1, 1))

    # End the URDF generation
    pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()