import time

def exactChange(a, b, c, w):
    cfactor = w//c
    cRemainder = w % c
    bremPri = cRemainder - c
    for ic in range (cfactor+1):
        bremPri += c
        bremainder = bremPri
        while bremainder > 0:
            if bremainder % a == 0:
                return True
            bremainder -= b
            
            
    return False

def exactchange(coins, total):
    n = len(coins)
    table = [[False] * (total+1) for i in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    # print(table)
    for i in range(1, n+1):
        for j in range(1, total+1):
            if coins[i-1] <= j:
                table[i][j] = table[i-1][j] or table[i][j-coins[i-1]]
            else:
                table[i][j] = table[i-1][j]

    return table[n][total]

def exactchange2(coins, total):
    table = [False] * (total+1)
    table[0] = True
    for j in range(1,total+1):
        for i in range(0, len(coins)):
            if table[j-coins[i]] == True:
                table[j] = True
                break
    return table[-1]

def exactchange3(coins, total):
    reachableNumbers = [0]
    coins.sort()
    while reachableNumbers[-1] < total:
        reachableNumbers.sort()
        nextNum = reachableNumbers[0]
        reachableNumbers = reachableNumbers [1:]
        for i in range(len(coins)):
            reachableNumbers.append(nextNum + coins[0])

            
def exactchange4(coins, w: int) -> bool:
   
    for coin in coins:              # 3 times (O(1))
        buffer = w             # O(1)
        while buffer > 0:           # Depends on the subtraction, which occurs
                                    # buffer // coin times, so O(n)
            if any([buffer % x == 0 for x in coins]):  # inner comprehension runs 3 times, overall O(1)
                return True         # O(1)
            buffer -= coin          # O(1)
    return False                    # O(1)


start_time = time.time()
print(exactchange([2,4,500],2000001))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")

start_time = time.time()
print(exactchange2([11,13,17],41))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")

start_time = time.time()
print(exactchange4([11,13,17],41))
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")