from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # Delete all nndf files
        if os.name == "nt":  # Windows
            os.system("del brain*.nndf")  # Delete all brain*.nndf files
        else:  # Mac/Linux
            os.system("rm brain*.nndf")  # Delete all brain*.nndf files
        # Delete all fitness files
        if os.name == "nt":  # Windows
            os.system("del fitness*.txt")  # Delete all fitness*.txt files
        else:  # Mac/Linux
            os.system("rm fitness*.txt")  # Delete all fitness*.txt files

        self.nextAvailableID = 0
        self.parents = {}

        for i in range(c.populationSize):  # Iterate from 0 to populationSize - 1
            self.parents[i] = SOLUTION(self.nextAvailableID) # Use loop variable as key, store new SOLUTION() as value
            self.nextAvailableID += 1


    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
        #for key in self.parents:  # Iterate through each parent-child pair
         #   if self.children[key].fitness < self.parents[key].fitness:
          #      self.parents[key] = self.children[key]

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Select()
        self.Print()
    def Spawn(self):
        self.children = {}  # Create an empty dictionary to store children

        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])  # Copy parent
            self.children[key].Set_ID(self.nextAvailableID)  # Assign new unique ID
            self.nextAvailableID += 1  # Increment for the next one

    def Mutate(self):
        for child in self.children.keys():
            self.children[child].Mutate()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()  # Print an empty line at the beginning
        for key in self.parents:
            print(f"Parent Fitness: {self.parents[key].fitness:.4f} | Child Fitness: {self.children[key].fitness:.4f}")
        print()  # Print an empty line at the end

    def Show_Best(self):
        # print("\nRe-evaluating the best solution with GUI...")
        # self.parent.Evaluate("GUI")  # show the best evolved solution

        bestParent = None
        bestFitness = float('inf')

        for key in self.parents:
            if self.parents[key].fitness < bestFitness:
                bestFitness = self.parents[key].fitness
                bestParent = self.parents[key]


        print(f"\nBest Fitness: {bestFitness} (Showing best parent in GUI mode...)")
        bestParent.Start_Simulation("GUI")
        '''
    def Show_Best(self):
        best_key = min(self.parents, key=lambda k: self.parents[k].fitness) #find parent with lowest fitness
        self.parents[best_key].Start_Simulation("GUI") #print simulation in GUI for the best'''

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")

        # Wait for all simulations to complete and read fitness
        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()
            # print(f"Parent {key} fitness: {solutions[key].fitness}")
            # print("Fitness:", solutions[key].fitness)  # Optional: debugging