import random
import numpy as np
np.random.seed(42)
from deap import base, creator, tools, algorithms

# Maximize fitness
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_int", random.randint, 0, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 5)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def fitness_function(individual):
    return (sum(individual),)

toolbox.register("evaluate", fitness_function)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=6)

algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=5, verbose=True)

best = tools.selBest(population, 1)[0]

print("\nBest Individual:", best)
print("Fitness:", fitness_function(best)[0])
