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
# Import constants and simulation file
import constants as c
from simulation import SIMULATION

simulation = SIMULATION()  # Create an instance of the SIMULATION class
simulation.Run()  # Call the Run method to start the simulation