import random
import numpy

def generateArmies(deadArmySize, livingArmySize):
    living = numpy.arange(0, livingArmySize).tolist()
    dead = numpy.arange(0, deadArmySize).tolist()
    return living, dead

def battle(livingArmy, deadArmy):

    while len(livingArmy) > 0 and len(deadArmy) > 0:
        livingSoldier = livingArmy.pop(0)
        deadSoldier = deadArmy.pop(0)

        # if random number is less than 0.5, the 
        # living wins. If random number is greater
        # than 0.5, the dead win

        number = random.random()

        if number > 0.5:
            deadArmy.append(livingSoldier) # Living joins the dead
            deadArmy.append(deadSoldier) # Dead Rejoins the dead
        
        else:
            livingArmy.append(livingSoldier)

def simulate(nsims, deadArmySize, livingArmySize):
    deadWins = 0
    livingWins = 0
    for i in range(nsims):
        armies = generateArmies(deadArmySize, livingArmySize)
        living = armies[0]
        dead = armies[1]

        battle(living, dead)

        if len(living) == 0:
            deadWins += 1
        else:
            livingWins += 1

    probabilityLivingWins = float(livingWins)/nsims
    probabilityDeadWins = float(deadWins)/nsims

    return probabilityLivingWins, probabilityDeadWins

def solve(deadArmySize):

    '''
    for i in range(1, deadArmySize):
        for j in range(1, livingArmySize):
            sims = simulate(10000, i, j)
            if sims[0] > 0.495 and sims[0] < 0.505:
                print("When the dead army has" , i, " soldiers, the living army needs :", j, "soldiers to have a 0.5 probability of winning")

    print("Done")
    '''

    for i in range(1, deadArmySize):

        j = 0

        finishFlag = False

        while finishFlag == False:

            sims = simulate(7000, i, j)

            if sims[0] > 0.5:
                print("When the dead army has" , i, " soldiers, the living army needs :", j, "soldiers to have a 0.5 probability of winning")
                
                finishFlag = True

            j += 1
        print("Done with " , i, " dead soldiers")

    print("Complete")



solve(10)


    

