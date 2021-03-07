import random
import math
size_of_initial_population = 40
initial_population = []
room = [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
for a in range(size_of_initial_population):
    initial_population.append([])
    for b in range(28):
        m = random.randint(0, 3)
        if m == 0:
            initial_population[a].append('D')
        if m == 1:
            initial_population[a].append('L')
        if m == 2:
            initial_population[a].append('R')
        if m == 3:
            initial_population[a].append('F')


def fitness_function(population):
    fitness_array = []
    size_of_population = len(population)
    for i in range(size_of_population):
        row = 1
        column = 1
        fitness = 1
        robot_facing = 'East'
        visited = [[-1, -1, -1, -1, -1, -1, -1, -1],
                   [-1, 0, 0, 0, 0, 0, 0, -1],
                   [-1, 0, 0, 0, 0, 0, 0, -1],
                   [-1, 0, 0, 0, 0, 0, -1, -1],
                   [-1, 0, 0, 0, 0, 0, -1, -1],
                   [-1, 0, 0, 0, 0, 0, 0, -1],
                   [-1, 0, 0, 0, 0, 0, 0, -1],
                   [-1, -1, -1, -1, -1, -1, -1, -1]]
        for j in range(28):
            temp = population[i][j]
            if temp == 'R' and robot_facing == 'East':
                robot_facing = 'South'
                # print("hello")
            elif temp == 'L' and robot_facing == 'East':
                robot_facing = 'North'
            elif temp == 'F' and robot_facing == 'East':
                if visited[row][column+1] == 0:
                    visited[row][column] = 1
                    column += 1
                    if room[row-1][column] == 0 or room[row+1][column] == 0 or room[row][column+1] == 0 or room[row-1][column+1] == 0 or room[row+1][column+1] == 0:
                        fitness += 1
            elif temp == 'R' and robot_facing == 'West':
                robot_facing = 'North'
            elif temp == 'L' and robot_facing == 'West' :
                robot_facing = 'South'
            elif temp == 'F' and robot_facing == 'West':
                if visited[row][column-1] == 0:
                    visited[row][column-1] = 1
                    column -= 1
                    if room[row-1][column] == 0 or room[row+1][column] == 0 or room[row][column-1] == 0 or room[row+1][column-1] == 0 or room[row-1][column-1] == 0:
                        fitness += 1
            elif temp == 'D' and robot_facing == 'West':
                continue
            elif temp == 'R' and robot_facing == 'North':
                robot_facing = 'East'
            elif temp == 'L' and robot_facing == 'North':
                robot_facing = 'West'
            elif temp == 'F' and robot_facing == 'North':
                if visited[row-1][column] == 0:
                    visited[row][column] = 1
                    row -= 1
                    if room[row][column-1] == 0 or room[row][column+1] == 0 or room[row-1][column-1] == 0 or room[row-1][column] == 0 or room[row-1][column+1] == 0:
                        fitness += 1
            elif temp == 'D' and robot_facing == 'North':
                continue
            elif temp == 'R' and robot_facing == 'South':
                robot_facing = 'West'
            elif temp == 'L' and robot_facing == 'South':
                robot_facing = 'East'
            elif temp == 'F' and robot_facing == 'South':
                if visited[row+1][column] == 0:
                    visited[row][column] = 1
                    row +=1
                    if room[row][column-1] == 0 or room[row][column+1] == 0 or room[row+1][column-1] == 0 or room[row+1][column] == 0 or room[row+1][column+1] == 0:
                        fitness += 1
            elif temp == 'D' and robot_facing == 'South':
                continue
        fitness_array.append(fitness)
    return fitness_array


def mutation(child_1, child_2):
    prob = random.uniform(0, 1)
    children3 = []
    if prob > 0.90:
        point_of_mutation = random.randint(0, 27)
        point_of_mutation2 = random.randint(0, 27)
        temp4 = child_1[point_of_mutation]
        child_1[point_of_mutation] = child_1[point_of_mutation2]
        child_1[point_of_mutation2] = temp4
        children3.append(child_1)
        point_of_mutation3 = random.randint(0, 27)
        point_of_mutation4 = random.randint(0, 27)
        temp5 = child_2[point_of_mutation3]
        child_2[point_of_mutation3] = child_2[point_of_mutation4]
        child_2[point_of_mutation4] = temp5
        children3.append(child_2)
    else:
        children3.append(child_1)
        children3.append(child_2)
    return children3


def crossover(parent1, parent2):
    point_of_crossover = random.randint(1,26)
    probability_of_crossover = random.uniform(0,1)
    child1 = []
    child2 = []
    children = []
    if probability_of_crossover < 0.70:
        for i in range(point_of_crossover):
            child1.append(parent1[i])
            child2.append(parent2[i])
        for j in range(point_of_crossover, 28):
            child1.append(parent2[j])
            child2.append(parent1[j])
    else:
        child1 = parent_1
        child2 = parent_2
    children.append(child1)
    children.append(child2)
    return children


def generate_mating_pool(population):
    fitness_of_population = fitness_function(population)
    sum_of_fitness = sum(fitness_of_population)
    expected_number = []
    for k in range(len(fitness_of_population)):
        expected_value = ((fitness_of_population[k] / sum_of_fitness) * size_of_initial_population)
        expected_value1 = math.ceil(expected_value)
        expected_number.append(expected_value1)
    s = 0
    mating_pool = []
    size_of_mating_pool = 0
    while size_of_mating_pool < size_of_initial_population:
        temp2 = expected_number[s]
        if (size_of_mating_pool + temp2) <= size_of_initial_population:
            for g in range(temp2):
                mating_pool.append(population[s])
                size_of_mating_pool += 1
            s += 1
        else:
            leftover = size_of_initial_population - size_of_mating_pool
            for r in range(leftover):
                mating_pool.append(population[s])
                size_of_mating_pool += 1
    return mating_pool


mating_pool1 = generate_mating_pool(initial_population)
cycles = 0
while cycles != 30:
    half = (len(mating_pool1)/2)
    half2 = int(half)
    temp_mating_pool = []
    for i in range(half2):
        parent_1 = mating_pool1[i]
        parent_2 = mating_pool1[len(mating_pool1)-i-1]
        children1 = crossover(parent_1, parent_2)
        children = mutation(children1[0], children1[1])
        temp_mating_pool.append(children[0])
        temp_mating_pool.append(children[1])
    mating_pool1 = generate_mating_pool(temp_mating_pool)
    fitness_of_this_mating_pool = fitness_function(mating_pool1)
    print(fitness_of_this_mating_pool)
    cycles += 1
