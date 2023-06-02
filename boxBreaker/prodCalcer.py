import math
import time


global globMax


def prodCalc(n):
    array = [1] * n
    [globMax, bestArray] = prodCalcRic(1, array)
    return bestArray

def prodCalcRic(globMax, array):
    bestArray = []
    checkedNums = set()
    for numIndex in range(len(array)):
        if array[numIndex] not in checkedNums:
            checkedNums.add(array[numIndex])
            checkedCompanion = set()
            for companion in array[0:numIndex] + array[numIndex+1:]:
                if companion not in checkedCompanion:
                    array2 = array.copy()
                    checkedCompanion.add(companion)
                    array2.remove(companion)
                    array2.remove(array[numIndex])
                    array2.append(companion+array[numIndex])
                    sol = 1
                    for num in array2:
                        sol = sol*num
                    if sol > globMax:
                        globMax = sol
                        bestArray = array2.copy()
                    [thisSol, thisArray]  = prodCalcRic(globMax, array2)
                    if thisSol > globMax:
                        globMax = thisSol
                        bestArray = thisArray.copy()

    return [globMax, bestArray]

def prodCalc2(n):
    sum = 0
    threeCount = 0
    twoCount = 0
    while sum < n:
        sum +=3
        threeCount += 1
    if sum == n:
        return (threeCount, 0)
    sum -=3
    threeCount -= 1
    if  n % 2 != sum % 2:
        sum -= 3
        threeCount -= 1
    while sum < n:
        sum += 2
        twoCount += 1
    return (threeCount, twoCount)

def prodCalc3(n):
    threeCount = n // 3
    sum = 3 * threeCount
    if sum == n:
        return (threeCount, 0)
    elif n - sum == 1:
        return (threeCount-1,2)
    elif n - sum == 2:
        return (threeCount, 1)
    
def prodCalc4(n):
    array = [[0] * math.ceil(n/2)]
    array.extend([[1]*math.ceil(n/2) for i in range(n)])
    print(array)
    for x in range(1,math.ceil(n/2)):
        for y in range(1,math.ceil(n)+1):
            jeff = y-x
            if jeff < 0:
                array[y][x] = array[y][x-1]
            else:
                array[y][x] = max(array[y][x-1],array[jeff][x]*(x))
    print(array)
    result = array[-1][-1]
    y= n-1
    x= math.ceil(n/2)-1
    output = []
    while x > 0 and y > 0:
        print( str(y) +  " , " + str(x))
        print(array)
        if y-x > 0 and array[y][x] /(x + 1) == array[y-x-1][x]:
            print("adding!")
            output.append(x+1)
            y -= (x + 1)
        else:
            x -= 1
    print(array[-1][-1])
    return output

# start_time = time.time()
# checks = prodCalc3(25)
# print(checks[0]*3 + 2*checks[1])
# print(checks)
# end_time = time.time()

# print(f"Time taken: {end_time - start_time} seconds")
start_time = time.time()
checks = prodCalc3(7)
print(checks[0]*3 + 2*checks[1])
print(3**checks[0] + 2**checks[1] - (checks[1] == 0 or checks[0] == 0))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
print(prodCalc4(7))
# print(prodCalc2(124564576456))
# print(prodCalc3(124564576456))
# print(prodCalc(12))
