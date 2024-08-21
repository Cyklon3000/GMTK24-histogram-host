import random
from sys import maxsize
import numpy as np

level = input("Enter level: ")

avgScore = float(input("Enter average score: "))
stdDeviation = float(input("Enter standard deviation: "))

limitMax = float(input("Enter limit max: "))

def generate_normal_float(mean, std_dev):
    """
    Generates a normal distributed float between 0 and 1 given the mean and standard deviation.
    
    Args:
        mean (float): The mean of the normal distribution.
        std_dev (float): The standard deviation of the normal distribution.
    
    Returns:
        float: A normal distributed float between 0 and 1.
    """
    # Generate a normal distributed random number
    random_number = np.random.normal(mean, std_dev)
    # Rescale the random number to be between 0 and 1
    scaled_number = (random_number - np.min([0, mean - 3 * std_dev])) / (np.max([1, mean + 3 * std_dev]) - np.min([0, mean - 3 * std_dev]))
    
    return scaled_number

def generate_score(mean, std_dev):
    deviationWeight = generate_normal_float(mean, 3)
    deviationWeight = deviationWeight * 2 - 1
    score = avgScore + deviationWeight * std_dev
    return score

i = 0
while i < 35:
    score = generate_score(avgScore, stdDeviation)
    if score > limitMax:
        continue
    i+=1
    
    randomPlayerID = random.randint(0, 684896138)
    print(f"{randomPlayerID} : " + '{' + f"\"level\" : {level}, \"score\" : {round(score, 3)}" + '}')