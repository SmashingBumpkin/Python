import os

def ex9(pathDir):
    '''Define a function ex9(pathDir) such that:
    - it is recursive or uses recursive functions(s)/method(s);
    - it receives the pathname 'pathDir'of a directory as argument;
    - it returns a list of pairs (tuple with two elements). Each tuple
      contains the name of a subdirectory that can be reached from
      'pathDir' and the total amount of bytes of all the files with
      extension .txt is that subdirectory.
    The list are sorted in descending order with respect to their
    second component (the amount of bytes of the .txt files) and, in
    case of tie, in alphabetical order with respect to the first
    component (the name of the subdirectory).  Files and directories
    whose name begins with the '.'  character should not be
    considered.

    For the purposes of the exercise, the following may be useful the
    following functions in the os module: os.listdir(),
    os.path.isfile(), os.path.isdir(), os.path.basename(),
    os.path.getsize()

    Example: with es9('Informatica/Software') it is returned the list:
    [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

    '''
    lDir = os.listdir(pathDir)
    output = []
    size = 0
    for el in lDir:
        if el[-4:] == '.txt':
            size += os.path.getsize(pathDir + '/' + el)
        elif os.path.isdir(pathDir + '/' + el,):
            otherDirs = ex9(pathDir + '/' + el)
            for el2 in otherDirs:
                output.append(el2)
    
    try:
        currDir = pathDir[-pathDir[::-1].index('/'):]
    except ValueError:
        currDir = pathDir
    output.append((currDir,size))
    output.sort()
    return output
                
    

# print('inf/sof:',ex9('Informatica/Software'))
# listt = [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]
# listt.sort()
# print(listt)
# print('inf/hrd:',ex9('Informatica/Hardware'))
# listt = [('Architetture', 12), ('RISC', 5), ('Hardware', 0), ('Processori', 0)]
# listt.sort()
# print(listt)
# print('informa:',ex9('Informatica'))
# listt = [('SistemiOperativi', 287), ('Informatica', 23), ('Architetture', 12), ('Software', 10), ('RISC', 5), ('BasiDati', 0), ('Hardware', 0), ('Processori', 0)]
# listt.sort()
# print(listt)
