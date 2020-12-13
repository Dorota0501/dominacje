# przyjęte oznaczenia: [start1, stop1]
import random
from aggregates import *
from dominations import *

all_intervals = []

# losowanie przedzialow
for i in range(100):
    start1 = random.randrange(0,1001,1) / 1000      # dokładność częsci dziesiętnej
    stop1 = random.randrange(0,1001,1) / 1000
    
    if start1 > stop1:
        start1, stop1 = stop1, start1               # nie generuje zbiorów pustych
        print("swap")

    print("start1: ",start1, " ,stop1: ",stop1)
    all_intervals.append([start1,stop1])


print("All intervals: ")    
for i in all_intervals:
    print(i)
print("---------------- \n")

#domination_or(all_intervals)       #\/
#domination_and(all_intervals)      #\/
#domination_aP(all_intervals)       # true
#domination_aQ(all_intervals)       # false
#domination_aMean(all_intervals)
#domination_aWMean(all_intervals)
#domination_aG(all_intervals)
#domination_aWG(all_intervals)      # false
#domination_a2(all_intervals)
#domination_a3(all_intervals)       # false
#domination_a5(all_intervals)  
#domination_a6(all_intervals)  
#domination_a7(all_intervals)
#domination_a8(all_intervals)
#domination_a9(all_intervals)       # false
#domination_a10(all_intervals)

