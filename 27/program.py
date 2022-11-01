

'''
    A common way to store tables is as lists of dictionaries.  Each
    row of the table corresponds to a dictionary whose keys are the
    names of the table columns.  This dictionary collection is then
    stored in a list.  For example the table
    
    name  | year | tel
  --------|------|---------
   Sophie | 1973 | 5553546 
   Bruno  | 1981 | 5558432

can be stored as 
[{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},{'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]

'''

def es27(table, column, value):
    '''Implement the function es27(table, col, val) that takes as an input

    - a table table represented by a list of dictionaries
    - a string col with the name of one of the columns of the table
    - a value val

    and modifies the table removing the column col and deleting all
    the rows with a value different from val in column col.  The
    function returns the number of deleted rows.

    For example
    - if table = [{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},
                 {'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]

    - the function call es27(table, 'year', 1981) returns the number 1
    and the table is modified in [{'name': 'Bruno','tel': 5558432}]
    '''
    count = 0
    for j in table[:]: #table[:] makes sure nothing gets skipped
        if j[column] == value: #deletes column from table
            del j[column]
        else: #or deletes row from table
            table.remove(j)
            count += 1
    return count
    
tabl = [{'name': 'Sophie', 'year': 1973 ,'tel': 5553546},
             {'name': 'Bruno', 'year': 1981 ,'tel': 5558432}]
tabl2 = es27(tabl, 'year', 1981)

#print(tabl2)