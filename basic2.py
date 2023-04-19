import pandas as pd

TEAM_NAMES = ['Studienleiter', 'Auswerter', 'App']

# Define the data
data = pd.DataFrame({'Name': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
                     'Team1': [3,   2,   2,   3,   3,   3,   1,   3,   3,   3,   2],
                     'Team2': [2,   3,   2,   2,   2,   1,   3,   1,   1,   1,   1],
                     'Team3': [1,   1,   3,   3,   1,   2,   2,   2,   1,   2,   3]})

# Define constants
TEAM_SIZE_MIN = 3
TEAM_SIZE_MAX = 4
NUMBER_SYSTEM = 3

ns = NUMBER_SYSTEM - 1

# Define fitness function
def fitness_function(solution):
    values = [data.iloc[i, solution[i]+1] for i in range(len(solution))]
    #team_counts = [solution.count(0), solution.count(1), solution.count(2)]
    if (solution.count(0) < 3 or solution.count(0) > 3): # Studienleiter
        return 0
    if (solution.count(1) < 3 or solution.count(1) > 4): # Auswerter
        return 0
    if (solution.count(2) < 3 or solution.count(2) > 3): # App
        return 0
    #if any([count < TEAM_SIZE_MIN or count > TEAM_SIZE_MAX for count in team_counts]):
    #    return 0
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

def quaternary_add(configuration):
    last = len(configuration)-1
    configuration[last] = configuration[last] + 1
    if configuration[last] > ns:
        configuration[last] = 0
        i = 1
        do = True
        while do:
            configuration[len(configuration)-1-i] = configuration[len(configuration)-1-i] + 1
            if configuration[len(configuration)-1-i] > ns:
                configuration[len(configuration)-1-i] = 0
                i = i + 1
            else:
                do = False
    return [int(digit) for digit in configuration]

def search():
    best_fitness = 0
    best_solution = []
    configuration = [0 for _ in range(len(data))]
    while configuration != [ns for _ in range(len(data))]:
        confL = quaternary_add(configuration)
        #print(confL)
        if fitness_function(confL) > best_fitness:
            best_fitness = fitness_function(confL)
            best_solution = confL
    return best_solution, best_fitness

def more(best_fitness):
    configuration = [0 for _ in range(len(data))]
    while configuration != [ns for _ in range(len(data))]:
        confL = quaternary_add(configuration)
        if fitness_function(confL) == best_fitness:
            print(confL)

def main():
    best_solution, best_fitness = search()
    print(f"List configuration with the same best fitness: ({best_fitness})")
    more(best_fitness)
    # Group names by team
    print(f"Print first best solution: ({best_fitness})")
    print(best_solution)
    print_members(best_solution)

main()