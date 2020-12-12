import math
import random

# [star1, stop1], [start2, stop2]

# AGREGACJE

#\/
def aOr(start1, stop1, start2, stop2):
    outcome_interval = []
    start = max(start1, start2)
    stop = max(stop1, stop2)
    outcome_interval = [start, stop]
    return outcome_interval

#/\
def aAnd(start1, stop1, start2, stop2):
    outcome_interval = []
    start = min(start1, start2)
    stop = min(stop1, stop2)
    outcome_interval = [start, stop]
    return outcome_interval

#Ap
def aP(start1, stop1, start2, stop2):
    outcome_interval = []
    start = start1 * start2
    stop = stop1 * stop2
    outcome_interval = [start, stop]
    return outcome_interval

#Aq
def aQ(start1, stop1, start2, stop2):
    outcome_interval = []
    start = start1 + start2 - (start1 * start2)
    stop = stop1 + stop2 - (stop1 * stop2)
    outcome_interval = [start, stop]
    return outcome_interval

# the representable arithmetic mean
def arithmeticMean(start1, stop1, start2, stop2):
    outcome_interval = []
    start = (start1 + start2) / 2
    stop = (stop1 + stop2) / 2
    outcome_interval = [start, stop]
    return outcome_interval

# the representable arithmetic weihgted mean
def arithmeticWeightedMean(start1, stop1, start2, stop2):
    w1 = random.random()
    w2 = 1 - w1
    outcome_interval = []
    start = (w1 * start1) + (w2 * start2)
    stop = (w1 * stop1) + (w2 * stop2)
    outcome_interval = [start, stop]
    return outcome_interval

# the representable arithmetic weihgted mean
def aG(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.sqrt((start1 * start2))
    stop = math.sqrt((stop1 * stop2))
    outcome_interval = [start, stop]
    return outcome_interval

# the representable arithmetic weihgted mean
def awG(start1, stop1, start2, stop2):
    w1 = random.random()
    w2 = 1 - w1
    outcome_interval = []
    start = math.sqrt(((start1 ** w1) * (start2 ** w2)))
    stop = math.sqrt(((stop1 ** w1) * (stop2 ** w2)))
    outcome_interval = [start, stop]
    return outcome_interval

# A2
def a2(start1, stop1, start2, stop2):
    outcome_interval = []
    start = (start1 + start2) / 2
    stop = max((start1 + stop2) / 2 , (stop1 + start2) / 2)
    outcome_interval = [start, stop]
    return outcome_interval

# A3
def a3(start1, stop1, start2, stop2):
    outcome_interval = []
    start = (start1 + start2) / 2
    stop = ((stop1 ** 2) + (stop2 ** 2)) / 2
    outcome_interval = [start, stop]
    return outcome_interval

# A5
def a5(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.sqrt(((start1 ** 2) + (start2 ** 2)) / 2)
    stop = math.pow(((stop1 ** 3) + (stop2 ** 3)) / 2 , 1 / 3)
    outcome_interval = [start, stop]
    return outcome_interval

# A6
def a6(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.pow(((start1 ** 3) + (start2 ** 3)) / 2 , 1 / 3)
    stop = math.pow(((stop1 ** 4) + (stop2 ** 4)) / 2 , 1 / 4)
    outcome_interval = [start, stop]
    return outcome_interval

# A7
def a7(start1, stop1, start2, stop2):
    outcome_interval = []
    start = min((stop1 + start2) / 2 , (start1 + stop2) / 2)
    stop = (stop1 + stop2) / 2
    outcome_interval = [start, stop]
    return outcome_interval

# A8
def a8(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.sqrt(start1 * start2) 
    stop = ((stop1 ** 2) + (stop2 ** 2)) / (stop1 + stop2)
    outcome_interval = [start, stop]
    return outcome_interval

# A9
def a9(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.sqrt(((start1 ** 2) + (start2 ** 2)) / 2) 
    stop = ((stop1 ** 3) + (stop2 ** 3)) / ((stop1 ** 2) + (stop2 ** 2))
    outcome_interval = [start, stop]
    return outcome_interval

# A10
def a10(start1, stop1, start2, stop2):
    outcome_interval = []
    start = math.sqrt(((start1 ** 2) + (start2 ** 2)) / 2)
    stop = math.sqrt(((stop1 ** 2) + (stop2 ** 2)) / 2)
    outcome_interval = [start, stop]
    return outcome_interval