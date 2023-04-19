import pandas as pd

TEAM_NAMES = ['Studienleiter', 'Auswerter', 'Flutter']

# Define the data
data = pd.DataFrame({'Name': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
                     'Team1': [3,   2,   2,   3,   3,   3,   1,   3,   3,   3,   2],
                     'Team2': [2,   3,   2,   2,   2,   1,   3,   1,   1,   1,   1],
                     'Team3': [1,   1,   3,   3,   1,   2,   2,   2,   1,   2,   3]})

# Define constants
TEAM_SIZE_MIN = 3
TEAM_SIZE_MAX = 4

# Define fitness function
def fitness_function(solution):
    values = [data.iloc[i, solution[i]+1] for i in range(len(solution))]
    team_counts = [solution.count(0), solution.count(1), solution.count(2)]
    if any([count < TEAM_SIZE_MIN or count > TEAM_SIZE_MAX for count in team_counts]):
        return 0
    return sum(values)

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
    best_fitness = 0
    best_solution = []
    configuration = [0 for _ in range(len(data))]
    for i in range(len(data)):
        for j in range(3):
            configuration[i] = j
            for k in range(len(data)-1-i):
                for l in range(3):
                    configuration[k+1] = l
                    if fitness_function(configuration) > best_fitness:
                        best_fitness = fitness_function(configuration)
                        best_solution = configuration
    # Group names by team
    print(best_solution)
    print(fitness_function(best_solution))
    print_members(best_solution)

main()
