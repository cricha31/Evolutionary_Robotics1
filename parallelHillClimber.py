from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        #self.parent = SOLUTION() # Create instance of SOLUTION
        self.parents = {}

        for i in range(c.populationSize):  # Iterate from 0 to populationSize - 1
            self.parents[i] = SOLUTION()  # Use loop variable as key, store new SOLUTION() as value

    def Evolve(self):
        ''''# Call the evaluate method from the parent solution
        self.parent.Evaluate("DIRECT") # run in blind

        # Loop through the number of generations
        for currentGeneration in range(c.numberOfGenerations):   # have -1 because it kept running 1 extra time
            # Evolve for one generation
            self.Evolve_For_One_Generation()
            # Update parent after selection
            self.parent = copy.deepcopy(self.next_parent)  # Ensure the parent updates for the next generation

        self.parent.Evaluate("GUI")'''
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()  # Generate a new solution (child)
        self.Mutate()  # Apply mutation to the child
        self.child.Evaluate("DIRECT")  # Evaluate the child
        self.Select()  # Select the best solution (parent or child)
        self.Print()
        """# Store the child if it's better but do NOT replace parent immediately
        if self.child.fitness < self.parent.fitness:
            self.next_parent = self.child  # Store as the next parent, but don't replace yet
        else:
            self.next_parent = self.parent  # Keep the same parent if the child isn't better"""


    def Spawn(self):
        self.child = copy.deepcopy(self.parent)  # Create a deep copy of self.parent and assign it to self.child

    def Mutate(self):

        self.child.Mutate()  # Call the mutate method of the child


    def Select(self):

        # If the child has better fitness, replace the parent with the child
        if self.child.fitness < self.parent.fitness:
            #print("Child has better fitness. Replacing parent with child.")
            self.next_parent = self.child  # Store child as the next parent
        else:
            self.next_parent = self.parent  # Keep the current parent if it's better
            #self.parent = copy.deepcopy(self.child)  # Replace the parent with the child

    def Print(self):
        # Print the fitness of self.parent and self.child on the same line
        print(f"Parent Fitness: {self.parent.fitness}, Child Fitness: {self.child.fitness}")

    def Show_Best(self):
        #self.parent.Evaluate("GUI")  # show the best evolved solution
        pass