from AmplitudeModifier import AmplitudeModifier
import pandas as pd
import numpy as np
import random


frequencies = ["20", "30", "40", "50", "60", "80", "100", "120", "150", "200", "300", "400", "500", "600", "800", "1000", "1200", "2000", "3000", "4000", "5000", "6000", "8000", "10000", "12000", "20000"]

resonances = [
    ["20", "40", "80"],
    ["30", "60", "120"],
    ["50", "100", "200", "400", "800"],
    ["150", "300", "600", "1200"],
    ["500", "1000", "2000", "4000", "8000"],
    ["3000", "6000", "12000"],
    ["5000", "10000", "20000"]
]

def getProbabilisticState(probability: float = 0.9544):
    tailSize = (1 - probability) / 2
    leftTail = tailSize
    rightTail = 1 - tailSize
    return leftTail, rightTail

def getCurrentProbabilisticState():
    seed = random.random()
    leftTail, rightTail = getProbabilisticState()
    if seed < leftTail:
        return "quiet"
    elif seed > rightTail:
        return "loud"
    else:
        return "normal"

def createRandomData():
    data = {}
    for frecuency in frequencies:
        data[frecuency] = AmplitudeModifier.normal()

    currentProbabilityState = getCurrentProbabilisticState()
    print("Creating data with state: ", currentProbabilityState)

    if currentProbabilityState == "normal":
        return data
    random_resonance = random.choice(resonances)


    if currentProbabilityState == "quiet":
        modifier = AmplitudeModifier.quiet
    elif currentProbabilityState == "loud":
        modifier = AmplitudeModifier.loud

    for affectedResonance in random_resonance:
        data[affectedResonance] = modifier()
    return data


if __name__ == '__main__':
    # for i in range(10):
    #     print(AmplitudeModifier.loud())
    # test = np.random.randint(-5, 5, 10)
    print(createRandomData())
