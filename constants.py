# File to store values as variables

# Imports
import numpy

#Double motor controls
AMPLITUDE = numpy.pi /4
FREQUENCY = 50
OFFSET = 0

# Motor control parameters for BackLeg
AMPLITUDE_BACK_LEG = numpy.pi / 4
FREQUENCY_BACK_LEG = 10
PHASE_OFFSET_BACK_LEG = 0

# Motor control parameters for FrontLeg
AMPLITUDE_FRONT_LEG = numpy.pi / 4
FREQUENCY_FRONT_LEG = 10
PHASE_OFFSET_FRONT_LEG = numpy.pi  # Phase shifted by pi

# Simulation parameters
GRAVITY = -9.8
TIMESTEPS = 500
MAX_FORCE = 50
FRAME_RATE = 1 / 100  # 60 FPS

# Parameter for spawn generations
numberOfGenerations = 10