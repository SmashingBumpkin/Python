import math
import time


def factorizable(n, A):
    if n % 1 != 0:
        return False
    if n == 0:
        return True
    if n < 1:
        return False
    multiplicationArray = [[] for i in range(len(A))]
    for i in range(len(A)):
        j = 1
        prod = A[i]
        while prod <= n:
            if prod < n/2:
                multiplicationArray[i].append(prod)
            elif prod == n:
                return True
            prod = prod*A[i]

    return factorizableHelper(n, multiplicationArray)
    
    
def factorizableHelper(n,array):
    for i in range(len(array)-1):
        pairedColumns = array[i+1].copy()
        for j in range(len(array[i])):
            for k in range(len(array[i+1])):
                prod = array[i][j]*array[i+1][k]
                if prod < n/2:
                    pairedColumns.append(prod)
                elif prod == n:
                    return True
                elif prod > n:
                    break
        
        modifiedArray = [pairedColumns]
        modifiedArray.extend(array[i+2:])
        if (factorizableHelper(n,modifiedArray)):
            return True
    return False

def factorizable3(n,X):
    numbers = set()
    numbers.add(1)
    for x in X:
        if x <= 1:
            pass
        nextNumbers = set()
        nextNumbers.add(1)
        for number in numbers:
            prod = number*x
            while prod <= n:
                nextNumbers.add(prod)
                if prod == n:
                    return True
                prod = prod*x
        numbers = nextNumbers
    return False

def factorizable4(n,A):
    dp = [False]*(n+1)
    dp[1] = True
    for a in A:
        for i in range(a,n+1):
            if dp[i%a ==0]:
                dp[i] = True
    return dp[n]

baseline = 14502624550.15917
t = 2.440364122390747





n= 4**34*6**30*5**18+1
A = [4,6,3]
A = [6, 4, 7]
n= 4**39*6**30*7**310+1


ix = len(A)
difficulty = ix*math.log(n,min(A))**ix
diffRatio = difficulty/baseline
print(difficulty)
print(n)
start_time = time.time()
print(factorizable3(n,A))
end_time = time.time()
timeRatio = (end_time - start_time)/t
print(f"Time taken: {end_time - start_time} seconds")
print(f"tRatio: {timeRatio} \ndiffRatio: {diffRatio}")

start_time = time.time()
# print(factorizable4(n,A))
end_time = time.time()
# print(f"Time taken: {end_time - start_time} seconds")