# https://en.wikipedia.org/wiki/Insertion_sort
# see also: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif

def InsertionSort(array : list) -> list:
    #Iterate through array with  index, value
    #subposn = from 0 to index:
        #compare value to each element
        #if the next element is lower than the value, swap it
    for index in range(1, len(array)):
        for bkIdx in range (index, 0, -1):
            if array[bkIdx - 1] > array[bkIdx]:
                array[bkIdx - 1], array[bkIdx] = array[bkIdx], array[bkIdx - 1]
            else: break
    return array

# if __name__ == "__main__":
#     L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2,5, 7, 78, 8, 8]
#     sortedL = InsertionSort(L)
#     print(sortedL)
    
    
# https://en.wikipedia.org/wiki/Bubble_sort
# see also: https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif

def BubbleSort(array : list) -> list:
    for end in range(len(array), 1, -1):
        isSorted = True
        for index in range(end-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
                isSorted = False
        if isSorted: return array
    return array


# if __name__ == "__main__":
#   L = [55, -1, 6, 32, 29, -10, 4, 2, 78, 7, 43, 2,5, 7, 8, 8]
#   sortedL = BubbleSort(L)
#   print(sortedL)
#   L = [9,8,7,6,5,4,3,2,1,0]
#   sortedL = BubbleSort(L)
#   print(sortedL)



# https://en.wikipedia.org/wiki/Selection_sort
# https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif

def SelectionSort(array : list) -> list:
    for i in range(len(array)):
        print(array)
        index = array.index(min(array[i:]))
        print(index, i, "min", min(array[i:]))
        array[i], array[index] = array[index], array[i]
    return array

if __name__ == "__main__":
  L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2,5, 7, 78, 8, 8]
  sortedL = SelectionSort(L)
  print(sortedL)