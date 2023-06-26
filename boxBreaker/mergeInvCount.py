def mergeCount(X):
    lng = len(X)
    if lng == 1:
        return (0, X)
    Xlh = X[:int(lng/2)]
    Xrh = X[int(lng/2):]
    counter = 0
    (count, Xlh) = mergeCount(Xlh)
    counter += count
    (count, Xrh) = mergeCount(Xrh)
    counter += count
    i, j = 0,0
    output = []
    print("count")
    print(counter)
    while i<len(Xlh) and j<len(Xrh):
        if Xlh[i] > Xrh[j]:
            output.append(Xrh[j])
            j += 1
            counter += 1
        else: 
            output.append(Xlh[i])
            i += 1
    print("count")
    print(counter)
    print("X")
    print(X)
    print(Xlh + Xrh)
    print("Xlh")
    print(Xlh)
    print("Xrh")
    print(Xrh)
    
    print(output)
    if len(Xlh) != i:
        counter += len(Xlh[i:])
        output = output + Xlh[i:]
    else:
        output = output + Xrh[j:]
    print(output)
    return (counter, output)

print(mergeCount([5,7,6]))

def count_inversions(sequence):
    def merge_sort(sequence):
        if len(sequence) <= 1:
            return sequence

        mid = len(sequence) // 2
        left_half = sequence[:mid]
        right_half = sequence[mid:]

        left_half = merge_sort(left_half)[0]
        right_half = merge_sort(right_half)[0]

        return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        inversions = 0
        i = j = 0
        print(left)
        print(right)
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged, inversions

    _, inversions = merge_sort(sequence)
    return inversions

sequence = [5, 7, 6]
inversions = count_inversions(sequence)
print(f"The sequence {sequence} has {inversions} inversion(s).")