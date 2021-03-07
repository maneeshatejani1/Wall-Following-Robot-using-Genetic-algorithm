# Wall-Following-Robot-using-Genetic-algorithm
Using genetic algorithm, created a population of robots that evolved in fitness over multiple generations and learnt to follow a wall perfectly.

The implementation is as follows:
Step 1: Initialize Population
Initialize a random population of individuals. Each individual is represented by its chromosome sequence. The length of chromosome for individuals in this assignment is 28 since that is the optimal number of sense-act cycles in which the wall can be followed perfectly. The genes in each chromosome are assigned random integer values ranging from 0-3 with 0 indicating a Do Nothing move that represented by D in the chromosome sequence, 1 indicating a left turn by the robot that is represented by L in the sequence, 2 indicating a right turn, represented by R and finally 3 indicating a move forward command represented by F in the corresponding chromosome sequence. 
Step 2: Calculate Fitness
After the population has been initialized, the next step is to calculate the fitness of each individual in the population. The fitness can be calculated by traversing the grid starting from row= 1 and column=1 in my implementation of an 8x8 grid and incrementing fitness value whenever the robot moves into a block it has not previously been to and a block where the Robot’s five sensors do not sense the presence of the wall. In this manner, the optimum fitness that the robot can have is 20, since that is the number of boxes that are immediately beside the wall. The fitness of each individual can be stored in an 1D array.
Step 3: Select the Mating Pool 
After we have got the fitness of each individual, we can select the fittest individuals from the population in this manner: 
    • Calculate the sum of all finesses in the population
    • Divide the fitness of each individual by the sum and multiply by population size
The second bullet point would give us information as to how many copies of one individual will go into the mating pool. For individuals that are fit relative to the total fitness, this number will be higher. In this manner, it will be ensured that only fit candidates are selected to be parents. After we have calculated the expected number for each individual, we can populate the mating pool with copies of those individuals until the size of the mating pool is reached. In my implementation, I have kept this size similar to the initial population size. This gives us the mating pool of parents for next generation.
Step 4: Select Pairs of Parents
From the mating pool, one can select pairs of parents for the next stage of crossover and mutation. This selection can be random or structured. In my implementation, I select the first parent for each crossover starting from the top of the mating pool and going down for other selections and for parent 2, starting from the bottom of the pool and going up for other parent selections from this pool. 
Step 5: Apply Crossover to each pair of parents
After I have chosen a pair, I can apply crossover to it. The probability of crossover can range between 0.6 and 0.9. In my implementation, I have taken this probability to be 0.90. To generate this probability, I generate a random number and if lies below 0.90, I apply crossover to the two parents and produce two offspring. The crossover can be one point or two point. I have applied one-point crossover in my algorithm. If this probability is greater than 0.90, I can simply copy both the parents in to two children.
Step 6: Apply Mutation to Children
After the crossover stage has produced two offspring, there is a very little probability that one or two genes can be altered. Hence again as we did in step 5, we can generate a random float number between 0 and 1 and if it is below 0.10, I apply mutation. In my implementation, I am applying a 2-point mutation in which I select two random points on the chromosome sequence and interchange their genes. 
Step 7: Repeat Step 2 to 6 for the New Generation of Offsprings
From the children produced after crossover and mutation, one can again apply the principles of natural selection to generate parents for next generation. Again, fittest individuals are selected and put into the mating pool and the process goes on with each generation creating fitter individuals than the last until the population saturates to a maximum fitness level.
Results and Analysis:
In this wall following problem, one can observe that fitness gets better with each generation. For example, one of my results is as following. In this, it is worth noting that the starting generations have very low fitness levels and very few individuals have good fitness levels. However, over the generations fitness, fitness has increased and more or less, there are not high differences between different individuals which indicates that the population is reaching its saturation point.
o.py"
[4, 4, 6, 6, 2, 2, 2, 3, 5, 5, 3, 4, 4, 7, 7, 3, 6, 6, 3, 3, 3, 2, 4, 4, 1, 4, 4, 3, 4, 4, 3, 2, 4, 4, 2, 6, 6, 4, 4, 2]
[4, 4, 2, 4, 4, 3, 3, 2, 6, 6, 6, 6, 2, 2, 3, 4, 4, 4, 4, 2, 5, 5, 4, 4, 5, 5, 2, 6, 6, 4, 4, 3, 4, 4, 3, 7, 7, 4, 4, 3]
[4, 4, 3, 4, 4, 4, 4, 2, 4, 4, 4, 4, 7, 7, 4, 4, 7, 7, 3, 3, 3, 4, 4, 3, 3, 3, 3, 6, 6, 4, 4, 4, 4, 5, 5, 5, 5, 4, 4, 3]
[1, 4, 3, 5, 5, 3, 5, 5, 4, 5, 5, 6, 6, 5, 5, 4, 5, 5, 4, 5, 5, 2, 4, 2, 2, 4, 4, 2, 7, 7, 6, 6, 3, 4, 3, 6, 6, 3, 1, 6]
[4, 3, 4, 2, 5, 5, 3, 4, 5, 5, 6, 6, 5, 5, 5, 5, 4, 2, 6, 6, 4, 4, 3, 6, 6, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 6, 6, 2]
[4, 2, 3, 6, 6, 4, 6, 6, 4, 4, 5, 5, 7, 7, 5, 5, 1, 3, 3, 4, 7, 7, 5, 5, 5, 5, 5, 5, 6, 6, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7]
[4, 7, 7, 6, 6, 2, 4, 4, 6, 6, 6, 6, 1, 5, 5, 4, 5, 5, 4, 5, 5, 3, 5, 5, 4, 5, 5, 3, 8, 8, 6, 6, 6, 6, 3, 5, 5, 3, 6, 6]
[4, 6, 6, 5, 5, 6, 6, 4, 5, 5, 6, 6, 5, 5, 4, 7, 7, 3, 4, 5, 5, 5, 5, 4, 6, 6, 3, 3, 3, 3, 2, 7, 7, 5, 5, 9, 9, 2, 4, 5]
[4, 6, 6, 6, 6, 4, 6, 6, 4, 5, 9, 9, 5, 9, 9, 6, 6, 5, 6, 6, 5, 4, 7, 7, 5, 7, 7, 3, 5, 3, 8, 8, 6, 6, 5, 5, 3, 4, 4, 4]
[4, 4, 6, 6, 4, 9, 9, 2, 4, 3, 4, 3, 5, 6, 6, 6, 6, 3, 6, 6, 6, 6, 6, 6, 4, 6, 6, 3, 9, 9, 3, 9, 9, 5, 6, 6, 2, 7, 7, 9]
[4, 6, 6, 4, 7, 7, 6, 6, 7, 7, 6, 6, 2, 4, 7, 7, 10, 10, 6, 6, 9, 9, 5, 6, 6, 4, 3, 7, 7, 3, 5, 6, 6, 8, 8, 3, 9, 9, 5, 3]
[3, 3, 6, 6, 5, 6, 6, 10, 10, 5, 8, 8, 7, 7, 3, 8, 8, 7, 7, 6, 6, 6, 6, 6, 6, 5, 8, 8, 4, 7, 7, 3, 4, 2, 6, 6, 7, 7, 6, 6]
[3, 10, 10, 2, 5, 6, 10, 10, 7, 7, 6, 5, 6, 7, 7, 8, 8, 7, 7, 2, 6, 5, 7, 7, 5, 5, 7, 7, 8, 8, 9, 9, 8, 8, 4, 7, 7, 11, 11, 7]
[3, 7, 7, 10, 10, 7, 7, 11, 11, 11, 11, 4, 7, 7, 4, 7, 7, 6, 4, 8, 8, 10, 10, 8, 8, 10, 10, 7, 7, 9, 9, 9, 9, 7, 7, 6, 10, 10, 5, 8]
[3, 8, 8, 7, 5, 10, 10, 7, 9, 9, 15, 15, 8, 8, 6, 7, 7, 7, 7, 5, 12, 12, 5, 12, 12, 11, 11, 9, 9, 8, 8, 11, 11, 8, 8, 3, 9, 9, 5, 7]
[3, 7, 8, 5, 9, 9, 8, 7, 9, 9, 4, 4, 11, 11, 8, 10, 10, 8, 11, 11, 7, 10, 10, 10, 10, 7, 6, 15, 15, 8, 12, 12, 11, 11, 8, 9, 9, 11, 11, 8]
[3, 8, 11, 11, 5, 11, 11, 7, 5, 9, 9, 9, 9, 9, 9, 8, 7, 8, 11, 11, 9, 9, 7, 12, 12, 9, 9, 12, 12, 9, 9, 3, 7, 6, 11, 11, 12, 12, 14, 14]
[3, 14, 14, 9, 11, 11, 11, 11, 12, 12, 11, 11, 11, 11, 11, 11, 7, 11, 11, 11, 11, 6, 11, 11, 7, 7, 3, 5, 9, 9, 9, 9, 12, 12, 9, 9, 12, 12, 9, 9]
[2, 7, 9, 14, 14, 14, 14, 12, 12, 8, 10, 10, 9, 11, 11, 9, 11, 11, 9, 13, 13, 11, 11, 12, 12, 12, 12, 9, 7, 7, 11, 11, 10, 10, 8, 8, 8, 4, 8, 3]
[6, 2, 7, 7, 8, 4, 8, 14, 14, 8, 14, 14, 14, 14, 8, 14, 14, 10, 10, 10, 10, 12, 12, 9, 6, 5, 7, 7, 10, 10, 9, 7, 9, 9, 11, 11, 12, 12, 11, 11]
[5, 4, 2, 11, 11, 7, 11, 11, 10, 10, 8, 11, 11, 8, 4, 11, 11, 8, 9, 9, 14, 14, 9, 9, 9, 9, 9, 9, 8, 9, 9, 10, 10, 14, 14, 14, 14, 10, 10, 13]
[5, 13, 13, 4, 10, 10, 3, 11, 11, 11, 11, 14, 14, 11, 11, 14, 14, 14, 14, 7, 11, 11, 13, 13, 10, 10, 11, 11, 10, 10, 10, 10, 9, 10, 10, 9, 10, 10, 8, 11]
[5, 11, 11, 13, 13, 8, 12, 12, 9, 5, 7, 10, 7, 10, 10, 3, 10, 9, 11, 11, 13, 13, 6, 13, 13, 6, 11, 11, 10, 10, 14, 14, 14, 14, 11, 11, 11, 11, 11, 11]
[5, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 13, 13, 11, 11, 13, 13, 12, 12, 9, 11, 11, 12, 12, 15, 15, 14, 14, 12, 12, 9, 13, 13, 7, 10, 7, 9, 10, 10, 7]
[6, 11, 10, 11, 11, 11, 11, 9, 11, 7, 11, 10, 11, 7, 13, 13, 11, 13, 13, 11, 9, 11, 11, 13, 13, 13, 13, 12, 12, 13, 13, 14, 14, 14, 14, 11, 15, 15, 11, 15]
[6, 11, 8, 12, 12, 15, 15, 10, 11, 15, 15, 11, 11, 10, 14, 14, 11, 14, 14, 14, 14, 9, 8, 7, 9, 11, 11, 13, 13, 10, 12, 12, 11, 12, 12, 9, 5, 13, 13, 13]
[4, 11, 13, 13, 11, 8, 13, 13, 5, 12, 12, 9, 12, 12, 12, 12, 15, 15, 12, 12, 15, 15, 10, 11, 11, 12, 12, 12, 12, 15, 15, 12, 12, 9, 13, 13, 11, 13, 13, 11]
[6, 13, 13, 11, 13, 13, 13, 13, 13, 13, 13, 13, 11, 13, 13, 11, 8, 13, 13, 13, 13, 9, 13, 13, 12, 12, 12, 12, 5, 12, 12, 15, 15, 12, 12, 15, 15, 9, 12, 12]
[5, 11, 13, 13, 9, 13, 13, 9, 11, 15, 15, 15, 15, 13, 13, 7, 12, 12, 11, 13, 13, 13, 13, 15, 15, 7, 13, 13, 13, 13, 12, 12, 7, 13, 13, 5, 13, 13, 12, 12]
[5, 11, 12, 12, 11, 13, 13, 13, 13, 13, 13, 13, 13, 9, 6, 13, 13, 13, 13, 13, 13, 13, 13, 10, 6, 11, 12, 12, 12, 12, 15, 15, 12, 12, 13, 13, 15, 15, 13, 13]
