# Imports
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset using numpy
backLegSensorValues = np.load("data/backLegSensorValues.npy")
# Load the second dataset using numpy
frontLegSensorValues = np.load("data/frontLegSensorValues.npy")
#Load sinusoidal motor data
backLegTargetAngles = np.load("data/backLegTargetAngles.npy")
frontLegTargetAngles = np.load("data/frontLegTargetAngles.npy")


""""# Print the loaded sensor values
print("Back Leg Sensor Values:", backLegSensorValues)
print("Front Leg Sensor Values", frontLegSensorValues)

# Plot the sensor values
plt.plot(backLegSensorValues, label="Back")
plt.plot(frontLegSensorValues, label="Front")
plt.title("Front and Back Leg Sensor Values")
plt.xlabel("Time Step")
plt.ylabel("Sensor Value")
plt.legend()"""

plt.plot(backLegTargetAngles, label="Back")
plt.plot(frontLegTargetAngles, label="Front")
plt.legend()

# Show the plot
plt.show()

