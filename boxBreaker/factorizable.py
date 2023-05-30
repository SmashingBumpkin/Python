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


n = 3**9
A = [7,2,3]
print(factorizable(n,A))