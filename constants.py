# File to store values as variables

# Imports
import numpy

#Double motor controls
AMPLITUDE = numpy.pi /4
FREQUENCY = 20
OFFSET = 0

# Motor control parameters for BackLeg
AMPLITUDE_BACK_LEG = numpy.pi / 4
FREQUENCY_BACK_LEG = 20
PHASE_OFFSET_BACK_LEG = 0

# Motor control parameters for FrontLeg  -- changed to 0 for better movement now
AMPLITUDE_FRONT_LEG = 0 #numpy.pi / 4
FREQUENCY_FRONT_LEG = 0 #10
PHASE_OFFSET_FRONT_LEG = 0 #numpy.pi  # Phase shifted by pi

# Simulation parameters
GRAVITY = -9.8
TIMESTEPS = 1000 # increased to 500 (gets better fitness but takes longer)
MAX_FORCE = 150   #50
FRAME_RATE = 1 / 10000  # 60 FPS (looking at increase this to see if it takes less time with same results)

# Parameter for spawn generations
numberOfGenerations = 10
populationSize = 10

motorJointRange = 0.3