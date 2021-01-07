# przyjęte oznaczenia: [start1, stop1]
import random
from aggregates import *
from dominations import *

all_intervals = []

# losowanie przedzialow
for i in range(100000):
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




#domination_or(all_intervals)       # \/
#domination_Wor(all_intervals)      # \/ True - False!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  473 / 25 000

#domination_or_L(all_intervals)     # \/
#domination_Wor_L(all_intervals)    # \/

#domination_or_Lx1(all_intervals)   # \/
#domination_Wor_Lx1(all_intervals)  # \/    false 22 / 25 000

#domination_or_Lx2(all_intervals)   # \/
#domination_Wor_Lx2(all_intervals)  # \/    false 22 / 25 000

#domination_or_Pi(all_intervals)    # \/    fasle  1063 / 25 000
#domination_Wor_Pi(all_intervals)   # \/    true  

#domination_and(all_intervals)      # /\
#domination_Wand(all_intervals)     # /\

#domination_aP(all_intervals)       # true
#domination_WaP(all_intervals)  

#domination_aP_L(all_intervals)     # true - false 4/25 000
#domination_WaP_L(all_intervals)      

#domination_aP_Lx1(all_intervals)   # true - false  7/ 25 000
#domination_WaP_Lx1(all_intervals)  

#domination_aP_Lx2(all_intervals)   # true  0/ 25 000
#domination_WaP_Lx2(all_intervals) 

#domination_aP_Pi(all_intervals)    # true  0/ 25 000
#domination_WaP_Pi(all_intervals)   # fasle

#domination_aQ(all_intervals)       # false
#domination_WaQ(all_intervals)      # true 0/1 000 000

#domination_aQ_L(all_intervals)     # false
#domination_WaQ_L(all_intervals)    # false 3 / 25 000

#domination_aQ_Lx1(all_intervals)   # false
#domination_WaQ_Lx1(all_intervals)  # false   3/ 25 000

#domination_aQ_Lx2(all_intervals)   # false
#domination_WaQ_Lx2(all_intervals)  # true   0/ 25 000

#domination_aQ_Pi(all_intervals)   # false
#domination_WaQ_Pi(all_intervals)  # true   0/ 25 000


#domination_aMean(all_intervals)
#domination_WaMean(all_intervals)

#domination_aWMean(all_intervals)
#domination_WaWMean(all_intervals)

#domination_aG(all_intervals)
#domination_WaG(all_intervals)

#domination_aWG(all_intervals)      # false
#domination_WaWG(all_intervals)     # true - false!!!! 151 / 25 000

#domination_aWG_L(all_intervals)    # false
#domination_WaWG_L(all_intervals)   # true - false!!!!!! 553/ 25 000

#domination_aWG_Lx1(all_intervals)      
#domination_WaWG_Lx1(all_intervals) # false 550 / 25 000 

#domination_aWG_Lx2(all_intervals)      
#domination_WaWG_Lx2(all_intervals) # false  90 / 25 000 

#domination_aWG_Pi(all_intervals)      
#domination_WaWG_Pi(all_intervals)  # false   8 / 25 000 

#domination_a2(all_intervals)
#domination_Wa2(all_intervals)

#domination_a3(all_intervals)       # false
#domination_Wa3(all_intervals)      # true - FALSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! bardzo rzadko  21 / 25 000

#domination_a3_L(all_intervals)      
#domination_Wa3_L(all_intervals) 

#domination_a3_Lx1(all_intervals)      
#domination_Wa3_Lx1(all_intervals)      

#domination_a3_Lx2(all_intervals)      
#domination_Wa3_Lx2(all_intervals) 

#domination_a3_Pi(all_intervals)     # false 53 / 25 000    
#domination_Wa3_Pi(all_intervals)    # true

#domination_a5(all_intervals)  
#domination_Wa5(all_intervals)
  
#domination_a6(all_intervals)  
#domination_Wa6(all_intervals)      # true - FALSE

#domination_a6_L(all_intervals)  
#domination_Wa6_L(all_intervals)  

#domination_a6_Lx1(all_intervals)  
#domination_Wa6_Lx1(all_intervals) 

#domination_a6_Lx2(all_intervals)  
#domination_Wa6_Lx2(all_intervals)    

#domination_a6_Pi(all_intervals)  
#domination_Wa6_Pi(all_intervals)   #true

#domination_a7(all_intervals)
#domination_Wa7(all_intervals)

#domination_a8(all_intervals)
#domination_Wa8(all_intervals)

#domination_a9(all_intervals)       # false
#domination_Wa9(all_intervals)      # true - FALSE 20 / 25 000

#domination_a9_L(all_intervals)      
#domination_Wa9_L(all_intervals)      

#domination_a9_Lx1(all_intervals)      
#domination_Wa9_Lx1(all_intervals)  # 24 / 25 000 false

#domination_a9_Lx2(all_intervals)      
#domination_Wa9_Lx2(all_intervals)  

#domination_a9_Pi(all_intervals)      
#domination_Wa9_Pi(all_intervals)  # true

#domination_a10(all_intervals)
#domination_Wa10(all_intervals)

