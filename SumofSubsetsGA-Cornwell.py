# import packages if necessary
import random
import math

# Create chromosome class
class Chromosome:

    # Initialize class
    def __init__(self, numList, k, child):

        # Underlying number set to compare bit-string to
        self.numList = numList
        # desired sum, k
        self.k = k
        # bit-string chromosome of same size as entered number set
        self.chromosome = []
        # this chromosomes raw fitness
        self.rawFit = 0
        # this chromosomes actual fitness
        self.fit = 0

        # randomly fill bit-string when initialized
        if (child == False):
            for i in range(0, len(self.numList)):
                self.chromosome.append(random.randint(0, 1))
        

    # determine sum representation of chromosome
    def chrSum(self):
        # indices represented by the chromosome
        chrRep = []
        for i in range(0, len(self.chromosome)):
            if (self.chromosome[i] == 1):
                chrRep.append(self.numList[i])

        # apply those indices (sum numbers in underlying number set)
        sigma = sum(chrRep)
        
        return sigma

    # determine feasibility of chromosome
    def feasibility(self):

        sigma = self.chrSum()

        # evaluate sum against k
        if (sigma <= self.k):
            return True
        else:
            return False

    # fitness Function
    def fitness(self):

        # determine feasibility
        feasibility = self.feasibility()

        # base fitness function (weigh accurate sum more than size of subset)
        fitness = (5 * (abs(self.chrSum() - self.k)) + (self.chromosome.count(1)))

        # calculate penalty if infeasible
        if (feasibility):
            penalty = 0
        else:
            penalty = 5*(abs(self.chrSum() - self.k) * (self.chromosome.count(1)))

        # return overall fitness of chromosome
        return fitness + penalty

    def bitFlip(self, index):
        if (self.chromosome[index] == 0):
            self.chromosome[index] = 1
        else:
            self.chromosome[index] = 0

    # setters
    def evaluateFitness(self):
        self.rawFit = self.fitness()

    def setFitness(self, fitness):
        self.fit = fitness

    def buildChromosome(self, n):
        self.chromosome.append(n)

    # getters
    def getChromosome(self):
        return self.chromosome
    
    def getRawFitness(self):
        return self.rawFit

    def getFitness(self):
        return self.fit

# tests for chromosome functionality
#ch = Chromosome([1, 2, 3, 4, 5], 10)

#print(ch.getChromosome())

#print(ch.feasibility())

#print(ch.sum())

#print(ch.fitness())


# Ask for user input
print('=======================================================')
print('PLEASE SELECT A SELECTION OPERATOR')
print('')
print('[Type "1" for Roulette  |  Type "2" for Tournament]')
selection = input('Enter 1 or 2: ')
print()
print('=======================================================')
print('PLEASE SELECT A CROSSOVER OPERATOR')
print('')
print('[Type "1" for Uniform  |  Type "2" for Single-Point]')
crossover = input('Enter 1 or 2: ')
print()
print('=======================================================')
print('PLEASE SELECT A MUTATION OPERATOR')
print('')
print('[Type "1" for N-Bit Flip  |  Type "2" for Random Single Bit Flip]')
mutation = input('Enter 1 or 2: ')
print()
print('=======================================================')
print('ENTER AN INTEGER FOR CROSSOVER RATE (EX: ENTER 80 FOR 80% RATE)')
print('')
print('[Type integer between 0 and 100]')
cPercent = input('Enter C%: ')
print()
print('=======================================================')
print('ENTER AN INTEGER FOR MUTATION RATE (EX: ENTER 80 FOR 80% RATE)')
print('')
print('[Type integer between 0 and 100]')
mPercent = input('Enter M%: ')
print()
print('=======================================================')
print('ENTER AN INTEGER FOR POPULATION SIZE')
print('')
print('[Type integer, recommend: 100]')
popSize = input('Enter integer: ')
print()
print('=======================================================')
print('ENTER AN INTEGER FOR RESULT PRINT FREQUENCY')
print('')
print('[Type integer; current best results display every (integer) generations]')
printFreq = input('Enter integer: ')
print('=======================================================')
print('ENTER AN INTEGER FOR DATASET TO OPERATE')
print('')
print('[Type "1" for Trivial "Toy" set | Type "2" for "Snake in the hay" set | Type "3" for Medium1 set | Type "4" for Medium2 set | Type "5" for large1 set | Type "6 for large2 set]')
setSelect = input('Enter integer: ')
print('=======================================================')


# small datasets
trivial = [34, 65, 33, 3, 42, 77, 4, 57, 90, 7, 5, 89, 24, 65, 45, 87]
snake = [34, 65, 33, 3, 42, 77, 4, 20, 57, 90, 7, 5, 89, 46, 24, 65]

targetSmall = 19

# medium datasets
medium1 = [268, 443, 585, 8, 630, 61, 511, 526, 689, 920, 432, 744, 460, 351, 381, 849, 751, 240, 693, 803, 210, 161, 596, 331, 582, 
            912, 141, 187, 980, 106, 166, 93, 319, 911, 665, 890, 899, 800, 856, 158, 954, 641, 103, 960, 942, 358, 83, 1000, 752, 370]
medium2 = [467, 418, 383, 437, 371, 944, 194, 43, 302, 343, 787, 889, 440, 910, 713, 241, 853, 919, 89, 668, 707, 406, 643, 29, 184, 
            741, 204, 379, 249, 750, 579, 829, 239, 615, 63, 784, 242, 819, 862, 234, 846, 623, 858, 974, 573, 359, 312, 911, 672, 691]

targetMedium = 3608

# large datasets
large1 = [425, 476, 59, 509, 867, 167, 701, 483, 473, 327, 676, 462, 650, 530, 85, 215, 330, 893, 980, 747, 646, 308, 365, 685, 765, 
            26, 545, 368, 453, 787, 724, 374, 364, 271, 81, 765, 241, 880, 402, 96, 417, 922, 870, 426, 722, 491, 653, 510, 115, 984, 
            880, 544, 149, 303, 757, 584, 581, 411, 370, 65, 236, 229, 133, 243, 545, 760, 200, 847, 559, 611, 219, 724, 709, 46, 53, 
            47, 378, 579, 672, 984, 479, 141, 864, 53, 894, 460, 936, 493, 790, 153, 951, 296, 51, 174, 681, 909, 450, 577, 255, 630, 
            782, 825, 552, 846, 820, 998, 917, 970, 540, 724, 129, 84, 345, 529, 241, 22, 64, 666, 548, 129]

large2 = [31, 70, 946, 493, 371, 170, 965, 640, 471, 701, 78, 932, 686, 608, 280, 870, 895, 936, 472, 663, 236, 253, 154, 300, 986, 
            980, 430, 653, 449, 322, 31, 393, 504, 481, 843, 0, 445, 738, 705, 602, 683, 228, 717, 856, 386, 174, 737, 606, 633, 312, 
            641, 976, 591, 335, 101, 219, 364, 330, 297, 977, 750, 768, 983, 423, 629, 308, 139, 563, 682, 892, 936, 825, 489, 292, 
            232, 755, 21, 806, 203, 164, 940, 312, 576, 948, 694, 140, 674, 953, 375, 188, 879, 848, 301, 935, 193, 975, 906, 525, 294, 
            976, 162, 150, 944, 508, 966, 993, 673, 322, 490, 170, 871, 830, 201, 648, 400, 297, 999, 669, 684, 397]

targetLarge = 9067

# convert string input to usable integers
selection = int(selection)       # selection mechanism
crossover = int(crossover)       # crossover mechanism
mutation = int(mutation)         # mutation mechanism
cPercent = int(cPercent)         # crossover chance
mPercent = int(mPercent)         # mutation chance
popSize = int(popSize)           # population size
printFreq = int(printFreq)       # print best-so-far every n gens
setSelect = int(setSelect)       # determine dataset to use

# determine dataset from user input
if (setSelect == 1):
    dataset = trivial
    k = targetSmall
elif (setSelect == 2):
    dataset = snake
    k = targetSmall
elif (setSelect == 3):
    dataset = medium1
    k = targetMedium
elif (setSelect == 4):
    dataset = medium2
    k = targetMedium
elif (setSelect == 5):
    dataset = large1
    k = targetLarge
elif (setSelect == 6):
    dataset = large2
    k = targetLarge

# Construct the initial populaton (randomly)
pop = []
for i in range(0, popSize):
    pop.append(Chromosome(dataset, k, child=False))

# keep track of best-so-far
alpha = 0

# Let population be N, and mutation and crossover rate be M% and C% respectively

# Repeat until done:
for i in range(0, 1000):

    #if (i != 0):
        #print()
        #print('Now again:')
        #print(str(alpha.getFitness()))

    # instantiate next generation
    mutatedChildren = []

    # Evaluate fitness for chromosome in population
    totalRawFitness = 0
    # evaluate raw fitness
    for chr in pop:
        chr.evaluateFitness()
        totalRawFitness += chr.getRawFitness()
    # calculate reverse fitness for minimization
    totalFitness = 0
    for chr in pop:
        chr.setFitness(totalRawFitness/chr.getRawFitness())
        totalFitness += chr.getFitness()

    #print()
    #print('Total raw fitness = ' + str(totalRawFitness))
    #print('Total fitness = ' + str(totalFitness))
    #print()

    #for chr in pop:
        #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    # bubblesort chromosomes by fitness (better fitness -> beginning of list)
    for c in range(0, popSize-1):
        for x in range(0, popSize-c-1):
            if pop[x].getFitness() < pop[x+1].getFitness():
                pop[x], pop[x+1] = pop[x+1], pop[x]

                #print()
                #for chr in pop:
                    #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    #print()
    #print('iteration: ' + str(i))
    #print('After Sorted: ')
    #print()

    #if (i != 0):
        #print()
        #print(str(pop[0].getFitness()))
        #print('Now again again:')
        #print(str(alpha.getFitness()))
        #print()

    #for chr in pop:
        #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    # after sorting, check if we have a new best-so-far
    if (i == 0):
        #print('initially assigned alpha')
        alpha = pop[0]
        #print('alpha: ' + str(alpha.getFitness()))
    else:
        #print('current genertation best: ' + str(pop[0].getFitness()))
        #print('alpha: ' + str(alpha.getFitness()))
        if (pop[0].getFitness() > alpha.getFitness()):
            #print('alpha has changed')
            alpha = pop[0]
            #print('new alpha ' + str(alpha.getFitness()))
    
    # print current results as frequently as user specifies
    if ((i % printFreq == 0)):
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print('After iteration: %d' %(i))
        print('---------------------------------')
        print('Current Population:')
        for chr in pop:
            print('(' + str(chr.chrSum()) + ', ' + str(chr.getFitness()) + ')')
        print()
        print('Best-so-far : ' + '(' + str(alpha.getChromosome()) + ', ' + str(alpha.getFitness()) + ')')
        print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

    # Send top two parents directly to the mutated-children pool (Elitism)
    mutatedChildren.append(pop[0])
    mutatedChildren.append(pop[1])

    # Use selection to build parent pool:
    parentPool = []

    # check which selection operator to use (1 -> Roulette, 2 -> Tournament)
    if (selection == 1):
        
        # calculate roulette wheel divisions
        wheel = []
        for index in range(0, popSize):

            # if wheel is initially empty, fill first segment
            if (len(wheel) == 0):
                wheel.append(pop[index].getFitness()/totalFitness)
            
            # otherwise, add to the wheel based on what's already there
            else:
                wheel.append(wheel[index-1] + (pop[index].getFitness()/totalFitness))

        #print()
        #print('wheel length: ' + str(len(wheel)))
        #print('Wheel divisions:')
        #for segment in wheel:
            #print(segment)

        # spin the wheel and build the pool
        while (len(parentPool) < popSize):
            rand = random.uniform(0.0, 1.0)
            #print('Random Generated: ' + str(rand))

            for index in range(0, len(wheel)):

                # check beginning of wheel
                if (rand <= wheel[0]):
                    parentPool.append(pop[0])
                    break

                # continue with rest of wheel
                elif (rand <= wheel[index] and rand > wheel[index-1]):
                    parentPool.append(pop[index])
                    break

        for c in range(0, popSize-1):
            for x in range(0, popSize-c-1):
                if parentPool[x].getFitness() < parentPool[x+1].getFitness():
                    parentPool[x], parentPool[x+1] = parentPool[x+1], parentPool[x]

        #print()
        #print('Parent Pool size: ' + str(len(parentPool)))
        #print('Parent Pool:')
        #for chr in parentPool:
            #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')
                

    elif (selection == 2):
        # chance to select more fit chromosome (75%)
        r = 75

        while (len(parentPool) < popSize):

            c1 = pop[random.randint(0, len(pop) - 1)]
            c2 = pop[random.randint(0, len(pop) - 1)]

            # r% of the time, the chromosome with higher fitness is allowed to continue
            if (random.randint(1, 100) <= r):
                if (c1.getFitness() > c2.getFitness()):
                    parentPool.append(c1)
                else:
                    parentPool.append(c2)
            else:
                if (c1.getFitness() > c2.getFitness()):
                    parentPool.append(c2)
                else:
                    parentPool.append(c1)

    #print()
    #print('Parent Pool size: ' + str(len(parentPool)))
    #print('Parent Pool:')
    #for chr in parentPool:
        #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    # Use user-selected crossover to build children pool
    childrenPool = []

    # check which crossover operator to use (1 -> Uniform, 2 -> Single-Point)
    if (crossover == 1):
        
        # repeat N/2 times (or until a child pool of size N-2 is created to save room for the elitists we saved)
        while (len(childrenPool) < popSize-2):

            # randomly select two parents
            p1 = parentPool[random.randint(0, popSize-1)]
            p2 = parentPool[random.randint(0, popSize-1)]

            #print ()
            #print('Parents: ')
            #print('P1: ' + str(p1.getChromosome()))
            #print('P2: ' + str(p2.getChromosome()))

            # if a random number is generated within C%, do crossover
            if (random.randint(1, 100) <= cPercent):

                # randomly fill bit-string according to size of chromosomes
                refString = []
                for num in range(0, len(p1.getChromosome())):
                    refString.append(random.randint(0, 1))

                #print ()
                #print('Reference String: ' + str(refString))

                # build child 1
                c1 = Chromosome(dataset, k, child=True)
                for index in range(0, len(refString)):
                    #print(str(index))
                    #print('refString value: ' + str(refString[index]))
                    if (refString[index] == 0):
                        #print('Going to p1 for ' + str(p1.getChromosome()[index]))
                        c1.buildChromosome(p1.getChromosome()[index])
                    else:
                        #print('Going to p2 for ' + str(p2.getChromosome()[index]))
                        c1.buildChromosome(p2.getChromosome()[index])
                    
                    #print(str(c1.getChromosome()))
                
                # build child 2
                c2 = Chromosome(dataset, k, child=True)
                for index in range(0, len(refString)):
                    if (refString[index] == 0):
                        c2.buildChromosome(p2.getChromosome()[index])
                    else:
                        c2.buildChromosome(p1.getChromosome()[index])
                
                #print ()
                #print('Children: ')
                #print('C1: ' + str(c1.getChromosome()))
                #print('C2: ' + str(c2.getChromosome()))

                # add the created children to the children pool
                childrenPool.append(c1)
                childrenPool.append(c2)

        #print()
        #print(str(len(childrenPool)))
        #print('Children Pool: ')
        #for chr in parentPool:
            #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    elif (crossover == 2) :

        while (len(childrenPool) < popSize-2): 
            # randomly select two parents
            p1 = parentPool[random.randint(0, popSize-1)]
            p2 = parentPool[random.randint(0, popSize-1)]

            #print('(' + str(p2.getChromosome()) + ', ' + str(p2.getFitness()) + ')')

            # if a random number is generated within C%, do crossover
            if (random.randint(1, 100) <= cPercent):
                
                # generate a random slice point
                slicePoint = random.randint(1, len(p1.getChromosome())-2)
                #print ("slicePoint is " + str(slicePoint))

                # build child 1
                c1 = Chromosome(dataset, k, child=True)
                for index in range(0, slicePoint):
                    c1.buildChromosome(p1.getChromosome()[index])
                for index in range(slicePoint, len(p1.getChromosome())):
                    #print(index)
                    #print("size of p2 is " + str(len(p2.getChromosome())))
                    c1.buildChromosome(p2.getChromosome()[index])

                # build child 2
                c2 = Chromosome(dataset, k, child=True)
                for index in range(0, slicePoint):
                    c2.buildChromosome(p2.getChromosome()[index])
                for index in range(slicePoint, len(p1.getChromosome())):
                    c2.buildChromosome(p1.getChromosome()[index])

                # add the created children to the children pool
                childrenPool.append(c1)
                childrenPool.append(c2)

    # Use mutation to build mutated children pool

    # check which mutation operator to use (1 -> n-bit flip, 2 -> random single bit flip)
    if (mutation == 1):
        for child in childrenPool:

            # if a random number is generated within M%, mutate the child
            if (random.randint(0, 100) < mPercent):
                #print("We gonna zap 'em")

                # generate how many bits to flip based on size of chromosome
                numToFlip = math.ceil((len(child.getChromosome())/25))
    
                # randomly pick where to flip the above number of times
                whereToFlip = random.sample(range(0, len(child.getChromosome())), k=numToFlip)

                # flip bits in those locations
                for index in whereToFlip:
                    child.bitFlip(index)
            
            mutatedChildren.append(child)
        
        #print()
        #print(str(len(mutatedChildren)))
        #print('mutated chldren: ')
        #for chr in mutatedChildren:
            #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

    elif (mutation == 2):
        for child in childrenPool:

            # if a random number is generated within M%, mutate the child
            if (random.randint(0, 100) < mPercent):
                #print("We gonna zap 'em")
    
                # randomly pick where to flip the above number of times
                whereToFlip = random.randint(0, len(child.getChromosome())-1)

                # flip bits in those locations
                child.bitFlip(whereToFlip)
            
            mutatedChildren.append(child)

    # Make mutated-children pool the next generation
    pop = mutatedChildren

    #print()
    #print('WOOOOOOOOOOOOOOOOO')
    #print(str(alpha.getFitness()))
    #print('END OF ITERATION')

    #print()
    #print(str(len(pop)))
    #print('new population: ')
    #for chr in pop:
        #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')
# End repeat (User termination or some other criteria)

# Evaluate final results
# Evaluate fitness for chromosome in population
totalRawFitness = 0
# evaluate raw fitness
for chr in pop:
    chr.evaluateFitness()
    totalRawFitness += chr.getRawFitness()
# calculate reverse fitness for minimization
totalFitness = 0
for chr in pop:
    chr.setFitness(totalRawFitness/chr.getRawFitness())
    totalFitness += chr.getFitness()

#print()
#print('Total raw fitness = ' + str(totalRawFitness))
#print('Total fitness = ' + str(totalFitness))
#print()

#for chr in pop:
    #print('(' + str(chr.getChromosome()) + ', ' + str(chr.getFitness()) + ')')

# bubblesort chromosomes by fitness (better fitness -> beginning of list)
for c in range(0, popSize):
    for x in range(0, popSize-c-1):
        if pop[x].getFitness() < pop[x+1].getFitness():
            pop[x], pop[x+1] = pop[x+1], pop[x]

print()
print('*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*')
print('Final Result of GA: ' + '(' + str(alpha.getChromosome()) + ', ' + str(alpha.getFitness()) + ')')
print('Sum of Result = ' + str(alpha.chrSum()))
print('Size of Result = ' + str(alpha.getChromosome().count(1)))
print('*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*')
print()
print("dataset = " + str(dataset))
print("k = " + str(k))

# Reminder: Keep track of best-so-far
# Reminder: Print intermediate results inside loop every so often [user-submitted])
# Produce results (The final chromosome and fitness result of the GA)
