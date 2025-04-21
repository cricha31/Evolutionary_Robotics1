from solution import SOLUTION
import constants as c
import copy
import os
from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        # Delete all fitness files
        if os.name == "nt":
            os.system("del fitness*.txt")
        else:
            os.system("rm fitness*.txt")

        self.nextAvailableID = 0
        self.parents = {}
        self.fitnessHistory = []  # to store average fitness for each generation

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

        self.Plot_Fitness_History()  # show plot after evolution

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        self.Record_Average_Fitness()  # track average fitness

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Evaluate(self, solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness:
                self.parents[key] = self.children[key]

    def Print(self):
        print()
        for key in self.parents:
            print(f"Parent Fitness: {self.parents[key].fitness:.4f} | Child Fitness: {self.children[key].fitness:.4f}")
        print()

    def Show_Best(self):
        bestParent = None
        bestFitness = float('inf')

        for key in self.parents:
            if self.parents[key].fitness < bestFitness:
                bestFitness = self.parents[key].fitness
                bestParent = self.parents[key]

        print(f"\nBest Fitness: {bestFitness} (Showing best parent in GUI mode...)")
        bestParent.Start_Simulation("GUI")

    # record average fitness each generation
    def Record_Average_Fitness(self):
        totalFitness = sum([self.parents[key].fitness for key in self.parents])
        averageFitness = totalFitness / len(self.parents)
        self.fitnessHistory.append(averageFitness)

    # plot fitness graph at the end
    def Plot_Fitness_History(self):
        plt.plot(self.fitnessHistory)
        plt.title("Average Parent Fitness Over Generations")
        plt.xlabel("Generation")
        plt.ylabel("Average Fitness")
        plt.grid(True)
        plt.show()