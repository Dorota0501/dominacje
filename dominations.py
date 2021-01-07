from aggregates import *

# przyjete oznaczenia:
# A = [startA, stopA]
# B = [startB, stopB]

# definicja operatora w
def operatorW(start1, stop1, start2, stop2):
    outcome_interval = []
    start = start1 + start2 + (stop1 * (stop1 - start1)) + (stop2 * (stop2 - start2)) / (2 + (stop1 - start1) + (stop2 - start2))
    stop = stop1 + stop2 + (start1 * (stop1 - start1)) + (start2 * (stop2 - start2)) / (2 + (stop1 - start1) + (stop2 - start2))
    outcome_interval = [start, stop]
    return outcome_interval

#-----------------------------------------------------------

# sprawdzanie dominacji or \/, A >> W
def domination_or(all_intervals):
    print("Domination OR \/ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aOr(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aOr(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, W >> A
def domination_Wor(all_intervals):
    print("Operator_W >> Domination OR \/ ")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aOr(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aOr(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, A >> W, porzadek czesciowy
def domination_or_L(all_intervals):
    print("Domination OR \/ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aOr(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aOr(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, W >> A, porzadek czesciowy
def domination_Wor_L(all_intervals):
    print("Operator_W >> Domination OR \/ ")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aOr(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aOr(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa

        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, A >> W,  porzadek leksykograficzny typu I-szego
def domination_or_Lx1(all_intervals):
    print("Domination OR \/ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aOr(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aOr(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, W >> A,  porzadek leksykograficzny typu I-szego
def domination_Wor_Lx1(all_intervals):
    print("Operator_W >> Domination OR \/ ")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aOr(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aOr(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa

        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, A >> W,  porzadek leksykograficzny typu II
def domination_or_Lx2(all_intervals):
    print("Domination OR \/ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aOr(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aOr(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, W >> A,  porzadek leksykograficzny typu II
def domination_Wor_Lx2(all_intervals):
    print("Operator_W >> Domination OR \/ ")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aOr(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aOr(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa

        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, A >> W,  Pi
def domination_or_Pi(all_intervals):
    print("Domination OR \/ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aOr(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aOr(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji or \/, W >> A,  Pi
def domination_Wor_Pi(all_intervals):
    print("Operator_W >> Domination OR \/ ")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aOr(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aOr(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aOr(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa

        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji and /\, A >> W
def domination_and(all_intervals):
    print("Domination AND /\ >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aAnd(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aAnd(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aAnd(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji and /\, W >> A
def domination_Wand(all_intervals):
    print("Operator_W >> Domination AND /\ .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aAnd(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aAnd(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aAnd(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji Ap, A >> W
def domination_aP(all_intervals):
    print("Domination Ap >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aP(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aP(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ap, W >> A
def domination_WaP(all_intervals):
    print("Operator_W >> Domination Ap .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aP(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aP(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Ap, A >> W, porzadek czesciowy
def domination_aP_L(all_intervals):
    print("Domination Ap >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aP(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aP(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ap, W >> A, porzadek czesciowy
def domination_WaP_L(all_intervals):
    print("Operator_W >> Domination Ap .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aP(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aP(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Ap, A >> W,  porzadek leksykograficzny typu I-szego
def domination_aP_Lx1(all_intervals):
    print("Domination Ap >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aP(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aP(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ap, W >> A, porzadek leksykograficzny typu I-szego
def domination_WaP_Lx1(all_intervals):
    print("Operator_W >> Domination Ap .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aP(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aP(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Ap, A >> W,  porzadek leksykograficzny typu II
def domination_aP_Lx2(all_intervals):
    print("Domination Ap >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aP(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aP(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ap, W >> A, porzadek leksykograficzny typu II
def domination_WaP_Lx2(all_intervals):
    print("Operator_W >> Domination Ap .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aP(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aP(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Ap, A >> W,  Pi
def domination_aP_Pi(all_intervals):
    print("Domination Ap >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aP(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aP(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ap, W >> A, Pi
def domination_WaP_Pi(all_intervals):
    print("Operator_W >> Domination Ap .")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aP(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aP(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aP(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji Aq, A >> W
def domination_aQ(all_intervals):
    print("Domination Aq >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aQ(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aQ(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Aq, W >> A
def domination_WaQ(all_intervals):
    print("Operator_W >> Aq")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aQ(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aQ(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    

  
    for i in results:
        print(i)


# sprawdzanie dominacji Aq, A >> W, porzadek czesciowy
def domination_aQ_L(all_intervals):
    print("Domination Aq >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aQ(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aQ(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Aq, W >> A, porzadek czesciowy
def domination_WaQ_L(all_intervals):
    print("Operator_W >> Aq")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aQ(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aQ(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Aq, A >> W,  porzadek leksykograficzny typu I-szego
def domination_aQ_Lx1(all_intervals):
    print("Domination Aq >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aQ(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aQ(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Aq, W >> A,  porzadek leksykograficzny typu I-szego
def domination_WaQ_Lx1(all_intervals):
    print("Operator_W >> Aq")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aQ(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aQ(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Aq, A >> W,  porzadek leksykograficzny typu II
def domination_aQ_Lx2(all_intervals):
    print("Domination Aq >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aQ(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aQ(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Aq, W >> A,  porzadek leksykograficzny typu II
def domination_WaQ_Lx2(all_intervals):
    print("Operator_W >> Aq")
    results = []

    for i in range(0,100000,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aQ(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aQ(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Aq, A >> W,  Pi
def domination_aQ_Pi(all_intervals):
    print("Domination Aq >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aQ(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aQ(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Aq, W >> A,  Pi
def domination_WaQ_Pi(all_intervals):
    print("Operator_W >> Aq")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aQ(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aQ(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aQ(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji A_mean, A >> W
def domination_aMean(all_intervals):
    print("Domination Aritmetic_Mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = arithmeticMean(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = arithmeticMean(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = arithmeticMean(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A_mean, W >> A
def domination_WaMean(all_intervals):
    print("Operator_W >> A_mean.")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = arithmeticMean(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = arithmeticMean(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = arithmeticMean(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji A_Wmean, A >> W
def domination_aWMean(all_intervals):
    print("Domination Aritmetic_Weighted_Mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = arithmeticWeightedMean(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = arithmeticWeightedMean(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = arithmeticWeightedMean(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A_Wmean, W >> A
def domination_WaWMean(all_intervals):
    print("Operator_W >> Aritmetic_Weighted_Mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = arithmeticWeightedMean(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = arithmeticWeightedMean(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = arithmeticWeightedMean(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji Ag, A >> W
def domination_aG(all_intervals):
    print("Domination Geometric_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = aG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = aG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = aG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Ag, W >> A
def domination_WaG(all_intervals):
    print("Operator_W >> Geometric_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = aG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = aG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = aG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji Awg, A >> W
def domination_aWG(all_intervals):
    print("Domination Geometric_weighted_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = awG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = awG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Awg, W >> A
def domination_WaWG(all_intervals):
    print("Operator_W >> Geometric_weighted_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = awG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = awG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Awg, A >> W, porzadek czesciowy
def domination_aWG_L(all_intervals):
    print("Domination Geometric_weighted_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = awG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = awG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Awg, W >> A, porzadek czesciowy
def domination_WaWG_L(all_intervals):
    print("Operator_W >> Geometric_weighted_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = awG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = awG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji Awg, A >> W, porzadek leksykograficzny typu I-szego
def domination_aWG_Lx1(all_intervals):
    print("Domination Geometric_weighted_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = awG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = awG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Awg, W >> A, porzadek leksykograficzny typu I-szego
def domination_WaWG_Lx1(all_intervals):
    print("Operator_W >> Geometric_weighted_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = awG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = awG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    
    for i in results:
        print(i)


# sprawdzanie dominacji Awg, A >> W, porzadek leksykograficzny typu II
def domination_aWG_Lx2(all_intervals):
    print("Domination Geometric_weighted_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = awG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = awG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Awg, W >> A, porzadek leksykograficzny typu II
def domination_WaWG_Lx2(all_intervals):
    print("Operator_W >> Geometric_weighted_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = awG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = awG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)

    
    
    for i in results:
        print(i)


# sprawdzanie dominacji Awg, A >> W, Pi
def domination_aWG_Pi(all_intervals):
    print("Domination Geometric_weighted_mean >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = awG(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = awG(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji Awg, W >> A, Pi
def domination_WaWG_Pi(all_intervals):
    print("Operator_W >> Geometric_weighted_mean")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = awG(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = awG(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = awG(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)

    
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------


# sprawdzanie dominacji A2, A >> W
def domination_a2(all_intervals):
    print("Domination A2 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a2(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a2(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a2(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A2, W >> A
def domination_Wa2(all_intervals):
    print("Operator_W >> A2")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a2(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a2(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a2(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji A3, A >> W
def domination_a3(all_intervals):
    print("Domination A3 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a3(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a3(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A3, W >> A
def domination_Wa3(all_intervals):
    print("Operator_W >> A3")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a3(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a3(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A3, A >> W, porzadek czesciowy
def domination_a3_L(all_intervals):
    print("Domination A3 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a3(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a3(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A3, W >> A, porzadek czesciowy
def domination_Wa3_L(all_intervals):
    print("Operator_W >> A3")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a3(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a3(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A3, A >> W,  porzadek leksykograficzny typu I-sze
def domination_a3_Lx1(all_intervals):
    print("Domination A3 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a3(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a3(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A3, W >> A, porzadek leksykograficzny typu I-szego
def domination_Wa3_Lx1(all_intervals):
    print("Operator_W >> A3")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a3(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a3(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A3, A >> W,  porzadek leksykograficzny typu II
def domination_a3_Lx2(all_intervals):
    print("Domination A3 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a3(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a3(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A3, W >> A, porzadek leksykograficzny typu II
def domination_Wa3_Lx2(all_intervals):
    print("Operator_W >> A3")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a3(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a3(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A3, A >> W, Pi
def domination_a3_Pi(all_intervals):
    print("Domination A3 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a3(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a3(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A3, W >> A, Pi
def domination_Wa3_Pi(all_intervals):
    print("Operator_W >> A3")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a3(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a3(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a3(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji A5, A >> W
def domination_a5(all_intervals):
    print("Domination A5 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a5(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a5(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a5(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A5, W >> A
def domination_Wa5(all_intervals):
    print("Operator_W >> A5")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a5(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a5(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a5(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji A6, A >> W
def domination_a6(all_intervals):
    print("Domination A6 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a6(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a6(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A6, W >> A
def domination_Wa6(all_intervals):
    print("Operator_W >> A6")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a6(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a6(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A6, A >> W, porzadek czesciowy
def domination_a6_L(all_intervals):
    print("Domination A6 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a6(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a6(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A6, W >> A, porzadek czesciowy
def domination_Wa6_L(all_intervals):
    print("Operator_W >> A6")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a6(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a6(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A6, A >> W, porzadek leksykograficzny typu I-szego
def domination_a6_Lx1(all_intervals):
    print("Domination A6 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a6(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a6(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A6, W >> A, porzadek leksykograficzny typu I-szego
def domination_Wa6_Lx1(all_intervals):
    print("Operator_W >> A6")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a6(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a6(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A6, A >> W, porzadek leksykograficzny typu II
def domination_a6_Lx2(all_intervals):
    print("Domination A6 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a6(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a6(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A6, W >> A, porzadek leksykograficzny typu II
def domination_Wa6_Lx2(all_intervals):
    print("Operator_W >> A6")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a6(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a6(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A6, A >> W, Pi
def domination_a6_Pi(all_intervals):
    print("Domination A6 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a6(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a6(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A6, W >> A, Pi
def domination_Wa6_Pi(all_intervals):
    print("Operator_W >> A6")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a6(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a6(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a6(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji A7, A >> W
def domination_a7(all_intervals):
    print("Domination A7 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a7(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a7(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a7(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A7, W >> A
def domination_Wa7(all_intervals):
    print("Operator_W >> A7")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a7(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a7(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a7(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji A8, A >> W
def domination_a8(all_intervals):
    print("Domination A8 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a8(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a8(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a8(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A8, W >> A
def domination_Wa8(all_intervals):
    print("Operator_W >> A8")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a8(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a8(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a8(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------

# sprawdzanie dominacji A9, A >> W
def domination_a9(all_intervals):
    print("Domination A9 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a9(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a9(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
        
# sprawdzanie dominacji A9, W >> A
def domination_Wa9(all_intervals):
    print("Operator_W >> A9")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a9(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a9(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        if i == False:
           print(i)


# sprawdzanie dominacji A9, A >> W, porzadek czesciowy
def domination_a9_L(all_intervals):
    print("Domination A9 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a9(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a9(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if((interval_Baa[0] <= interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
        
# sprawdzanie dominacji A9, W >> A, porzadek czesciowy
def domination_Wa9_L(all_intervals):
    print("Operator_W >> A9")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a9(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a9(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if((interval_Abb[0] <= interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A9, A >> W, porzadek leksykograficzny typu I-szego
def domination_a9_Lx1(all_intervals):
    print("Domination A9 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a9(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a9(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] < interval_Abb[0]:
            results.append(True)
        elif ((interval_Baa[0] == interval_Abb[0]) and (interval_Baa[1] <= interval_Abb[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
        
# sprawdzanie dominacji A9, W >> A, porzadek leksykograficzny typu I-szego
def domination_Wa9_Lx1(all_intervals):
    print("Operator_W >> A9")
    results = []

    for i in range(0,100000,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a9(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a9(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] < interval_Baa[0]:
            results.append(True)
        elif ((interval_Abb[0] == interval_Baa[0]) and (interval_Abb[1] <= interval_Baa[1])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A9, A >> W, porzadek leksykograficzny typu II
def domination_a9_Lx2(all_intervals):
    print("Domination A9 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a9(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a9(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[1] < interval_Abb[1]:
            results.append(True)
        elif ((interval_Baa[1] == interval_Abb[1]) and (interval_Baa[0] <= interval_Abb[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
        
# sprawdzanie dominacji A9, W >> A, porzadek leksykograficzny typu II
def domination_Wa9_Lx2(all_intervals):
    print("Operator_W >> A9")
    results = []

    for i in range(0,100000,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a9(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a9(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[1] < interval_Baa[1]:
            results.append(True)
        elif ((interval_Abb[1] == interval_Baa[1]) and (interval_Abb[0] <= interval_Baa[0])): 
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)


# sprawdzanie dominacji A9, A >> W, Pi
def domination_a9_Pi(all_intervals):
    print("Domination A9 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a9(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a9(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if interval_Baa[0] <= interval_Abb[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
        
# sprawdzanie dominacji A9, W >> A, Pi
def domination_Wa9_Pi(all_intervals):
    print("Operator_W >> A9")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a9(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a9(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a9(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if interval_Abb[0] <= interval_Baa[1]:
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

#-----------------------------------------------------------
#-----------------------------------------------------------

# sprawdzanie dominacji A10, A >> W
def domination_a10(all_intervals):
    print("Domination A10 >> Operator_W")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam B(x,y)
        interval_Bxy = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Bxy: ", interval_Bxy)

        # wyznaczam B(z,t)
        interval_Bzt = operatorW(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Bzt: ", interval_Bzt)

        # wyznaczam A(x,z)
        interval_Axz = a10(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Axz: ", interval_Axz)


        # wyznaczam A(y,t)
        interval_Ayt = a10(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Ayt: ", interval_Ayt)


        # wyznaczam A(B(x,y), B(z,t))
        interval_Abb = a10(interval_Bxy[0],interval_Bxy[1],
                                      interval_Bzt[0],interval_Bzt[1])
        print("A(B(x,y), B(z,t)): ", interval_Abb)
        
        
        # wyznaczam B(A(x,z), A(y,t))
        interval_Baa = operatorW(interval_Axz[0],interval_Axz[1],
                                      interval_Ayt[0],interval_Ayt[1])
        print("B(A(x,z), A(y,t)): ", interval_Baa)


        # sprawdzam nierówność Abb >= Baa
        # czyli Baa <= Abb
        if (interval_Baa[0] + interval_Baa[1]) < (interval_Abb[0] + interval_Abb[1]):
            results.append(True)
        elif (interval_Baa[1] + interval_Baa[0]) == (interval_Abb[1] + interval_Abb[0]) and (interval_Baa[1] - interval_Baa[0]) <= (interval_Abb[1] - interval_Abb[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)

# sprawdzanie dominacji A10, W >> A
def domination_Wa10(all_intervals):
    print("Operator_W >> A10")
    results = []

    for i in range(0,100,4):
        print(i)
        x = i
        y = x + 1
        z = x + 2
        t = x + 3
        # wyznaczam A(x,y)
        interval_Axy = a10(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[y][0],all_intervals[y][1])
        print("Axy: ", interval_Axy)

        # wyznaczam A(z,t)
        interval_Azt = a10(all_intervals[z][0],all_intervals[z][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Azt: ", interval_Azt)

        # wyznaczam B(x,z)
        interval_Bxz = operatorW(all_intervals[x][0],all_intervals[x][1],
                           all_intervals[z][0],all_intervals[z][1])
        print("Bxz: ", interval_Bxz)


        # wyznaczam B(y,t)
        interval_Byt = operatorW(all_intervals[y][0],all_intervals[y][1],
                           all_intervals[t][0],all_intervals[t][1])
        print("Byt: ", interval_Byt)


        # wyznaczam B(A(x,y), A(z,t))
        interval_Baa = operatorW(interval_Axy[0],interval_Axy[1],
                                      interval_Azt[0],interval_Azt[1])
        print("B(A(x,y), A(z,t)): ", interval_Baa)
        
        
        # wyznaczam A(B(x,z), B(y,t))
        interval_Abb = a10(interval_Bxz[0],interval_Bxz[1],
                                      interval_Byt[0],interval_Byt[1])
        print("A(B(x,z), B(y,t)): ", interval_Abb)


        # sprawdzam nierówność Baa >= Abb
        # czyli Abb <= Baa
        if (interval_Abb[0] + interval_Abb[1]) < (interval_Baa[0] + interval_Baa[1]):
            results.append(True)
        elif (interval_Abb[1] + interval_Abb[0]) == (interval_Baa[1] + interval_Baa[0]) and (interval_Abb[1] - interval_Abb[0]) <= (interval_Baa[1] - interval_Baa[0]):
            results.append(True)
        else:
            results.append(False)
    
    for i in results:
        print(i)
