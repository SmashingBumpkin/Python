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

# if __name__ == "__main__":
#   L = [55, -1, 6, 32, 29, -10, 4, 2, 7, 43, 2,5, 7, 78, 8, 8]
#   sortedL = SelectionSort(L)
#   print(sortedL)
  
def stiiiiCazzi():
    dic = {"Mancini": ["Maurizio","Mancini","prog 1"],
           "Spognardi": ["Angelo","Spognardi","Prog 2"],
           "Desensi": []}
    for el in dic.items():
        print(el, end = " - \n")
    dic["Mancini"].append("YOOOO")
    print(dic["Mancini"])
    dic["Desensi"]=dic["Mancini"]
    dic["Desensi"].append("hffjgfjf")
    print(dic["Mancini"])
    
    
# if __name__ == "__main__":
    # stiiiiCazzi()
    
# A lottery works as follows. Each participant pays in €5 and chooses six numbers in the range [1,90]. The
# total amount of collected money is shared among the winner(s). To determine the winner(s), 1 number in
# that range is drawn at random; all lottery participants who chose that number share equally in the
# winnings.
# Write a function lottery_winners(participants, x) that takes a dictionary (containing the participants names
# and numbers) and the value of the randomly drawn number x and that prints out the name of the winner(s)
# and the amount won by each.
# The dictionary containing the participants names and numbers is organised as in the following example:
# D = { "Donald" : [23, 21, 20, 34, 15, 23], "Boris" : [17, 16, 3, 7,
# 26, 42], "Theresa" : [13, 90, 47, 17, 1, 11] }
# As you can see, the numbers chosen by each participant are stored in a list. So, given the participant's
# name you can retrieve his/her numbers as follows:
# numbers = D["Boris"]
# As a consequence, numbers[0], numbers[1], etc. are the numbers played by "Boris".
# You may assume that participants' names are unique but their chosen numbers can (of course) repeat (i.e.
# different particpants could choose the same number or numbers).
# Test your function by writing a program and passing to your function the dictionary above and number
# 17. Since there are 3 participants and 2 of them ("Boris" and "Theresa") have chosen number 17, your
# function should print:
# Winners are: Boris, Theresa
# They win 7.5 euro each

def lottery_winners(participants : dict, x : int) -> None:
    
    winners = [name for name, numbers in participants.items() if x in numbers]
    try:
        print(winners, "all win", len(participants)*5 / len(winners))
    except ZeroDivisionError:
        print("get good")

if __name__ == "__main__":
  lottery_winners({ "Donald" : [23, 21, 20, 34, 15, 23], "Boris" : [17, 16, 3, 7, 26, 42], "Theresa" : [13, 90, 47, 17, 1, 11] }, 2)