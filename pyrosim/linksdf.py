from pyrosim.inertialsdf     import INERTIAL_SDF

from pyrosim.geometrysdf     import GEOMETRY_SDF

from pyrosim.collisionsdf    import COLLISION_SDF

from pyrosim.visualsdf       import VISUAL_SDF

from pyrosim.commonFunctions import Save_Whitespace

class LINK_SDF:

    def __init__(self,name,pos,size,rpy):

        self.name = name
        self.pos = pos  # Store the position
        self.size = size  # Store the size
        self.rpy = rpy  # Store the roll, pitch, yaw

        self.depth = 2

        self.inertial  = INERTIAL_SDF()

        self.geometry = GEOMETRY_SDF(size)

        self.collision = COLLISION_SDF(self.geometry)

        self.visual    = VISUAL_SDF(self.geometry)

    def Save(self,f):

        self.Save_Start_Tag(f)

        # Write the position and rotation (roll, pitch, yaw)
        f.write(f'    <pose>{self.pos[0]} {self.pos[1]} {self.pos[2]} {self.rpy[0]} {self.rpy[1]} {self.rpy[2]}</pose>\n')

        self.inertial.Save(f)

        self.collision.Save(f)

        self.visual.Save(f)

        self.Save_End_Tag(f)

# ------------------- Private methods -----------------

    def Save_End_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('</link>\n')

    def Save_Start_Tag(self,f):

        Save_Whitespace(self.depth,f)

        f.write('<link name="' + self.name + '">\n')
