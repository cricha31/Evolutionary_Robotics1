# Creating new file for class motor
# Imports
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName    # Store the joint name
        self.values = numpy.zeros(c.TIMESTEPS)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        """Prepare a vector to store motor values."""
        self.values = numpy.zeros(c.TIMESTEPS)  # Vector to store motor values

        # Movement properties
        self.amplitude = c.AMPLITUDE
        #self.frequency = c.FREQUENCY commented out to change frequency between motors
        self.offset = c.OFFSET

        # Conditional logic to set frequencies
        if self.jointName == "Torso_BackLeg":
            self.frequency = c.FREQUENCY / 2  # Half the frequency for BackLeg
        else:
            self.frequency = c.FREQUENCY  # Regular frequency for FrontLeg

        # Generate motor values using instance-specific properties
        for t in range(c.TIMESTEPS):
            self.values[t] = self.amplitude * numpy.sin(self.frequency * t + self.offset)

    def Set_Value(self, t, robot):
        """Apply motor control using precomputed values."""
        if t < len(self.values):  # Ensure we don't access out-of-bounds index
            targetLocation = self.values[t]  # Get precomputed motor value

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot.robotId,  # Access robot instance
            jointName=self.jointName,  # Convert string to bytes
            controlMode=p.POSITION_CONTROL,
            targetPosition=targetLocation, # use precomputed value
            maxForce=c.MAX_FORCE
        )

    def Save_Values(self):
        """Save motor values to a file."""
        numpy.save(f"data/motor_{self.jointName}.npy", self.values)