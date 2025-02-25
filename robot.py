# Creating new file for class robot

#Imports
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c  # Import constants

# Importing other files
from sensor import SENSOR
from motor import MOTOR

class ROBOT:

    def __init__(self):
        #self.sensor = SENSOR()
        #self.motor = MOTOR()

        # Loads the robot body and prepares it for simulation.
        self.robotId = p.loadURDF("body.urdf")  # Load robot URDF

        # Prepare robot for simulation
        pyrosim.Prepare_To_Simulate(self.robotId)

        # Prepare sensors for all links
        self.Prepare_To_Sense()

        # Prepare motors
        self.Prepare_To_Act()

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
        # iterate over all motors and set their values at time t
        for motor in self.motors.values():   # iterate of all MOTOR instances
            motor.Set_Value(t, self)    # call Set_Value() on each motor
