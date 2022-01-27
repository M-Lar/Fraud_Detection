from random import random
import numpy as np


def generateAdjacentMatrix(size,
                           followChance, followBackChance,
                           fraudGroupSize,
                           fraudSpammerFollowChance, fraudSpammerFollowBackChance, fraudSpammerTargetNumber):
    matrix = np.zeros((size, size), np.int8)
    fraudSpammerCount = 0
    fraudGroupCount = 0
    groupIndexes = []

    for i in range(size):
        if(i % 100 == 0):
            print(f'i = {i}')
        # Case for spammer (following a lot of people without much followback)
        if(fraudSpammerCount < fraudSpammerTargetNumber and random() < fraudSpammerTargetNumber/float(size)):
            for j in range(size):
                if(i == j):
                    continue
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
                if(i >= j):
                    continue
                if(random() <= followChance):
                    matrix[i][j] = 1
                    if(random() <= followBackChance):
                        matrix[j][i] = 1

    # Link all members of fraud group together
    for i in groupIndexes:
        for j in groupIndexes:
            if(i == j):
                continue
            matrix[i][j] = 1

    return matrix


size = 10000
print(generateAdjacentMatrix(size, 0.05, 0.90, 200, 0.95, 0.02, 50))
