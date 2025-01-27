# Import pyrosim
import pyrosim.pyrosim as pyrosim

# Tell pyrosim the name of the file where the world will be stored
# Now called 5x5_towers (was originially box, then boxes, then tower)
pyrosim.Start_SDF("5x5_towers.sdf")

# Create variables for box parameters
length = 1
width = 1
height = 1

# Create variables for position(start first block with height 0.5)
base_x = 0
base_y = 0
base_z = 0.5

# Loop through the rows and columns to create the grid
for row in range(5):  # 5 rows
    for col in range(5):  # 5 columns
        # Set the base position for each tower in the grid
        x = base_x + col * (length * 1.1)  # Offset x position for each column
        y = base_y + row * (width * 1.1)   # Offset y position for each row
        z = base_z  # Reset z for each tower

        # Create the blocks in the current tower
        for i in range(10):  # 10 blocks per tower
            pyrosim.Send_Cube(name=f"Block_{row}_{col}_{i}", pos=[x, y, z], size=[length, width, height])

            # Move the next block upwards
            z += height

            # Decrease the size for the next block (90% of previous size)
            length *= 0.9
            width *= 0.9
            height *= 0.9

        # Reset the block size for the next tower
        length = 1
        width = 1
        height = 1

# End the SDF generation
pyrosim.End()