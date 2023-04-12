my_arr = [(1,3),(1,4),(2,4),(3,5), (4,6), (3,9), (2,10), (10,11), (1,12), (12,13), (1,14), (14,15), (1,16)]
# my_arr = [(4,5), (5,6), (6,7),(1,8)]
# my_arr = [(3,4),(5,6),(2,7),(8,9),(1,10)]

last_j = 0
P = [None] * len(my_arr)
P[0] = -1
count = 0
for i in range(len(my_arr)-1):
    print("BIGGGLLOOOOOPPP")
    i += 1
    while my_arr[last_j][1] > my_arr[i][0] and last_j >= 1:
        print("adding")
        count += 1
        last_j -= 1
    while my_arr[last_j][1] <= my_arr[i][0]:
        print("subbing")
        count += 1
        last_j += 1
    P[i] = last_j - 1

print(P)

print(count)