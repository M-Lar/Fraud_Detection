from random import random
import numpy as np


def generateAdjacentMatrix(size,
                            followChance, followBackChance,
                            fraudGroupSize,
                            fraudSpammerFollowChance, fraudSpammerFollowBackChance, fraudSpammerTarget  ):
    matrix = np.zeros((size,size))
    fraudSpammerCount = 0
    fraudGroupCount = 0
    groupIndexes = []

    for i in range(size):
        # Case for spammer (following a lot of people without much followback)
        if(fraudSpammerCount < fraudSpammerTarget and random() < fraudSpammerTarget/float(size)):
            for j in range(size):
                if(i == j): continue
                if(random() <= fraudSpammerFollowChance):
                    matrix[i][j] = 1
                    if(random() <= fraudSpammerFollowBackChance):
                        matrix[j][i] = 1
        # Case for group frauders (A group of users with mostly connections to one another)
        elif(fraudGroupCount < fraudGroupSize and random() < fraudGroupSize/float(size)):
            groupIndexes.append(i)
            fraudGroupCount += 1
        else:
            for j in range(size):
                if(i == j): continue
                if(random() <= followChance):
                    matrix[i][j] = 1
                    if(random() <= followBackChance):
                        matrix[j][i] = 1

    # Link all members of fraud group together
    for i in groupIndexes:
        for j in groupIndexes:
            if(i == j): continue
            matrix[i][j] = 1

    print(groupIndexes)
    print(matrix[groupIndexes[0]])
    return matrix

# size = 1000
# print(generateAdjacentMatrix(size,0.05, 0.60, float(size)*0.05, 0.65, 0.02, float(size)*0.02))