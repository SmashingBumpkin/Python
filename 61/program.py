

def es61(ftext, op, sel):
    '''Design the function es61(ftext, op, sel) that reads a matrix of
    integers contained in the ftext text file and returns a list of
    integers.

    The matrix is stored line by line into the file. The integers are
    separated in each line by an arbitrary number of spaces.  The list
    to return contains the results of an operation to be performed on
    the rows, the columns or the diagonals of the matrix, as specified
    by the 'op' and 'sel' parameters, taken as input. The values of
    'op' specifies the type of operation, and it can assume three
    different values:
        'max' (for the calculation of the maximum),
        'min' (for the calculation of the minimum)
        'sum' (for the calculation of the sum).

    The values of the parameter 'sel' specify which elements of the
    matrix the operation must operate on. It can take the following
    values:
        'row' (for selecting the rows of the matrix, in ascending order),
        'col' (for selecting the columns of the matrix, in ascending order),
        'dp' (for selecting the the main diagonal of the matrix)
        'ds' (for selecting the secondary diagonal of the matrix).

    For example if the matrix contained in the text file is:
    2  0   -4
    5  10  20
    5  1   -1
    depending on the parameters you will have:

    es61(ftext, 'max','row')= [2, 20, 5]
    es61(ftext, 'min','row')= [-4, 5,-1]
    es61(ftext, 'sum','row')= [-2, 35, 5]
    es61(ftext, 'max','col')= [ 5,  10, 20]
    es61(ftext, 'min','col')= [ 2,  0, -4]
    es61(ftext, 'sum','col')= [ 12, 11, 15]
    es61(ftext, 'max','dp' )= [10]
    es61(ftext, 'min','dp' )= [-1]
    es61(ftext, 'sum','dp' )= [11]
    es61(ftext, 'max','ds' )= [10]
    es61(ftext, 'min','ds' )= [-4]
    es61(ftext, 'sum','ds' )= [11]

    '''
    # insert here your code
    with open(ftext, 'r', encoding = "utf8") as fileref:
        matrix = [[int(number) for number in line.split()] for line in fileref.readlines()]
    
    length = len(matrix)
    
    if sel == "col":
        newmatrix = [line.copy() for line in matrix]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                newmatrix[x][y] = matrix[y][x]
        matrix = newmatrix
    elif sel == "dp":
        newmatrix = [[matrix[index][index] for index in range(length)]]
        matrix = newmatrix
    elif sel == "ds":
        newmatrix = [[matrix[length-index-1][index] for index in range(length)]]
        matrix = newmatrix
    
    if op == "max":
        return [max(line) for line in matrix]
    elif op == "min":
        return [min(line) for line in matrix]
    elif op == "sum":
        return [sum(line) for line in matrix]
    
if __name__ == "__main__":
    print(es61("matrice4.txt","sum","row"))
        
