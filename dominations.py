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

# sprawdzanie dominacji dla arithmetic mean
def domination_aritmetic_mean(all_intervals):
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

# sprawdzanie dominacji dla A2
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

# sprawdzanie dominacji dla A3
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

# sprawdzanie dominacji dla A5
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

# sprawdzanie dominacji dla A6
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

# sprawdzanie dominacji dla A7
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

# sprawdzanie dominacji dla A8
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

# sprawdzanie dominacji dla A9
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

# sprawdzanie dominacji dla A10
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