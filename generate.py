# Import pyrosim
import pyrosim.pyrosim as pyrosim

def Create_World():
    # Tell pyrosim the name of the file where the world will be stored
    pyrosim.Start_SDF("world.sdf")

    # Store box position and parameters
    pyrosim.Send_Cube(name="Box", pos=[-10,0,0.5], size=[1,1,1])

    # End the SDF generation
    pyrosim.End()

def Create_Robot():
    # Start creating the robot description in URDF format
    pyrosim.Start_URDF("body.urdf")

    # Block dimensions
    length = 1
    width = 1
    height = 1

    # Create the root cube (Torso)
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1.5], size=[length, width, height])

    # Create Joint between Torso and BackLeg
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, 0, 1])

    # Create BackLeg
    pyrosim.Send_Cube(name="BackLeg", pos=[1, 0, -0.5], size=[length, width, height])

    # Create joint between Torso and FrontLeg
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[1, 0, 1])

    # Create FrontLeg
    pyrosim.Send_Cube(name="FrontLeg", pos=[-2, 0, -0.5], size=[length, width, height])




    # End the URDF generation
    pyrosim.End()

Create_World()
Create_Robot()