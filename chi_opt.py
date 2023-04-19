import pandas as pd
import random
from itertools import repeat

rng = random.Random(0)

TEAM_NAMES = ['Studienleiter', 'Auswerter', 'Flutter']

# Define the data
data = pd.DataFrame({'Name': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
                     'Team1': [3,   2,   2,   3,   3,   3,   1,   3,   3,   3,   2],
                     'Team2': [2,   3,   2,   2,   2,   1,   3,   1,   1,   1,   1],
                     'Team3': [1,   1,   3,   3,   1,   2,   2,   2,   1,   2,   3]})

# Define constants
TEAM_SIZE_MIN = 3
TEAM_SIZE_MAX = 4
pop_size = 5000
no_of_gen = 50

weights = data[['Team1', 'Team2', 'Team3']].values.tolist()
population = [[0 for _ in range(len(weights))] for _ in range(pop_size)]

# Define fitness function
def fitness_function(solution):
    values = [data.iloc[i, solution[i]+1] for i in range(len(solution))]
    team_counts = [solution.count(0), solution.count(1), solution.count(2)]
    if any([count < TEAM_SIZE_MIN or count > TEAM_SIZE_MAX for count in team_counts]):
        return 0
    return sum(values)

# Define mutation function
def mutate(solution):
    new_solution = solution
    row_index = random.randrange(len(solution))
    new_solution[row_index] = random.randrange(3)
    return new_solution

# Define crossover function
def crossover(solution1, solution2):
    new_solution = solution1
    for j in range(len(solution1)):
        if random.random() < 0.5:
            new_solution[j] = solution2[j]
    return new_solution

# Define evolutionary algorithm
def evolutionary_algorithm(pop, fitness_function, num_generations=100, mutation_rate=1.5, crossover_rate=0.0):
    combinations = []
    fitnesses = []
    for generation in range(num_generations):
        # Evaluate fitness of population
        fitness_values = [fitness_function(solution) for solution in pop]
        #
        max_fitness = max(fitness_values)
        best_solution_index = fitness_values.index(max_fitness)
        best_solution = pop[best_solution_index]
        fitness_values.remove(max_fitness)
        #
        scd_fitness = max(fitness_values)
        snd_solution_index = fitness_values.index(scd_fitness)
        snd_solution = pop[snd_solution_index]
        fitness_values.remove(scd_fitness)
        #
        trd_fitness = max(fitness_values)
        trd_solution_index = fitness_values.index(trd_fitness)
        trd_solution = pop[trd_solution_index]
        #
        print(f"{best_solution} Generation {generation}: Best fitness = {max_fitness}")
        combinations.append(best_solution.copy())
        fitnesses.append(max_fitness)
        # Create new population
        new_population = [best_solution, snd_solution, trd_solution]
        repeated_indices = []
        for i, count in enumerate(fitness_values):
            count=count+1
            repeated_indices.extend([i]*count)
        if (repeated_indices == []):
            print(f"empty! {fitness_values}")
        while len(new_population) < len(pop):
            if random.random() < crossover_rate:
                parent1 = pop[random.choice(repeated_indices)]
                parent2 = pop[random.choice(repeated_indices)]
                child = crossover(parent1, parent2)
            else:
                child = pop[random.choice(repeated_indices)]
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child.copy())
        pop = new_population
    return combinations[fitnesses.index(max(fitnesses))]

def print_members(solution):
    teams = [[] for _ in range(3)]
    for t in range(3):
        for i in range(len(solution)):
            if solution[i] == t:
                teams[t].append(data.iloc[i]['Name'])
    # Print results
    for i, team in enumerate(teams):
        print(f"{TEAM_NAMES[i]}: {', '.join(team)}")

def main():
    # Run evolutionary algorithm
    best_solution = evolutionary_algorithm(population, fitness_function, no_of_gen)
    # Group names by team
    print(best_solution)
    print(fitness_function(best_solution))
    print_members(best_solution)

main()
