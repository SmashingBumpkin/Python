import math 
n = 25**2 #number of floors
k = 2 #number of boxes
iStar = 50

def BoxBreaker(k, n, iStar):
    maxTests = round(2*(n**0.5))
    return BoxBreakerHelper(k, n, iStar, maxTests, 1, 0)



def BoxBreakerHelper(k, n, iStar, testHeight, safeHeight, attempts):
    attempts += 1
    print(str(k) + " " + str(n)+ " "  + str(iStar)+ " test: "  + str(testHeight)+ " safe: " + str(safeHeight))
    if k == 1:
        for floor in range(safeHeight + 1, n+1):
            attempts += 1
            if floor == iStar:
                return (floor, attempts)
    if testHeight < iStar:
        safeHeight = testHeight
        jeff = n-testHeight
        if jeff <=5:
            testHeight = safeHeight + math.floor(jeff*0.5)
        else:
            testHeight = safeHeight + 2*math.floor(jeff**0.5)
            
            if testHeight == safeHeight:
                testHeight += 1
        return BoxBreakerHelper(k, n, iStar, testHeight, safeHeight, attempts)
    else:
        return BoxBreakerHelper(k-1 , n, iStar, safeHeight + 1, safeHeight, attempts)



print(BoxBreaker(k, n, iStar))