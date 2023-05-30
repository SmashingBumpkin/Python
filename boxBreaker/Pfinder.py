
def pFinder(I):
    P = [None] * len(I)
    i = 0
    for j in range(len(I)):
        if j == 0:
            pass
        while I[i+1][1] <= I[j][0]:
            i += 1
        if I[i][1] <= I[j][0]:
            P[j] = i

    print(P)


I = [(0,2),(1,2),(3,5),(6,10),(7,11),(10,11), (11,12)]

pFinder(I)