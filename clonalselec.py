import random

# Initial antibodies (population)
population = [random.randint(0, 31) for _ in range(5)]

for generation in range(5):
    print(f"\nGeneration {generation+1}: {population}")

    # Fitness function: maximize x^2
    fitness = [x**2 for x in population]

    # Select best antibody
    best = population[fitness.index(max(fitness))]
    print("Best Antibody:", best)

    # Clone best antibody
    clones = [best for _ in range(3)]

    # Mutation of clones
    mutated_clones = [clone + random.randint(-2, 2) for clone in clones]

    # Replace worst antibodies with mutated clones
    population.sort()
    population[:3] = mutated_clones

best_solution = max(population, key=lambda x: x**2)

print("\nFinal Best Solution:", best_solution)
print("Fitness:", best_solution**2)

#CSA selects high-affinity antibodies, clones them proportionally, mutates clones to improve diversity, and replaces weaker antibodies iteratively