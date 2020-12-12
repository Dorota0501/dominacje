import math

# [star1, stop1], [start2, stop2]

# AGREGACJE


# the representable arithmetic mean
def arithmeticMean(start1, stop1, start2, stop2):
    outcome_interval = []
    start = (start1 + start2) / 2
    stop = (stop1 + stop2) / 2
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