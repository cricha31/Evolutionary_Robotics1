# Import pyrosim
import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file where the world will be stored
# Currently called box because it will only contain a box
pyrosim.Start_SDF("box.sdf")

# Store box position and parameters
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])

# Appending
pyrosim.End()