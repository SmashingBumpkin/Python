# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:10:27 2022

@author: Charl
"""

class Employee:
    name = ""
    age = 0
    address = ""
    def __init__(self, init_name): #constructor allows min inputs to be required
        self.name = init_name
    
    def change_address(self, newAdd):
        self.address = newAdd
    
    def Print(self):
        print(self.name, self.age, self.address, sep = '\n')
        
# E0 = Employee("jeff")
# E0.address = "123 defintiely real stret"
# E0.age = 95
# E0.Print()


# given the Matrix class:
class Matrix:
    
    # where "values" is a list of lists (a list of rows, every row
    # is a list) containing the values of the matrix
    # write the methods:
    width = 0
    height = 0
    values = []
    def zeros(self, w, h): 
        #TODO: resize the matrix to (w, h) and fills it with zeros
        self.values = [[0]* w for _ in range(h)]
        self.height = len(self.values)
        self.width = len(self.values[0])
        
    def transpose(self): #transposes the matrix
        temp = [[0]* self.height for _ in range(self.width)]
        for y in range(self.height):
            for x in range(self.width):
                temp[x][y] = self.values[y][x]
        self.values = temp
        self.height = len(self.values)
        self.width = len(self.values[0])
        
    def symmetric(self): 
        # returns True or False, whether or not the matrix is symmetric
        try:
            for y in range(self.height):
                for x in range(self.width):
                    if self.values[y][x] != self.values[x][y]:
                        return False
        except:
            return False
        return True
        
    def add(self, M): 
        #adds the matrix to another matrix M, and stores the result in the matrix
        Mh, Mw = min(self.height,len(M)), min(self.width, len(M[0]))
        for y in range(Mh):
            for x in range(Mw):
                self.values[y][x] += M[y][x]
        
    def __repr__(self): #returns a string representing the matrix values
        result = ""
        for row in self.values:
            for el in row:
                result += str(el) + " "
            result += "\n"
        return result
    

# steve = Matrix()
# steve.zeros(4,2)
# steve.values[0][1] = 1
# print(steve.values)
# print(steve.width,steve.height)
# steve.transpose()
# print(steve)
# print(steve.transpose())
# print(steve.symmetric())
# steve.zeros(3,3)
# print(steve.symmetric())
# paul = [[1,2,3,4,5],[1,2,3,4,5]]
# steve.add(paul)
# print(steve)


# write 2 classes, Book and Author:

# Author has the following attributes and methods:
# name : str, email : str
# getName()
# getEmail()
# setEmail(str)
# __repr__()

# Book has the following attributes and methods:
# isbn : str, title : str, authors : list[Author], price : float
# getISBN()
# getAuthorsNames()
# getPrice()
# setPrice(float)
# __repr__()

# read the list of books stored in the file books.txt, in which
# each book is stored as a sequence of comma-separated values:
# isbn, title, price, author1 name, author1 email, author2 name, author2 email, ...
# the function returns a list of Book objects

class Author:
    # Author has the following attributes and methods:
    name = "str"
    email = ""
    
    def __init__(self, nam, ema):
        self.name = nam
        self.email = ema
    
    def getName(self):
        return self.name
    
    def getEmail(self):
        return self.email
    
    def setEmail(self,newEmail):
        self.email = newEmail
    
    def __repr__(self):
        result = self.name + "\n" + self.email
        return result

class Book:
    isbn = ""
    title = ""
    authors = []
    price = 0.0
    def getISBN(self):
        return self.isbn
    def getAuthorsNames(self):
        return self.authors
    def getPrice(self):
        return self.price
    
    def setPrice(self, newPr):
        self.price = newPr
        
    def __repr__(self):
        output = self.title + "\n"
        for i in self.authors:
            output += "i"
        return output
    
with open('books.txt', 'r') as fileRef:
    books = []
    for i, line in enumerate(fileRef):
        line = line.split(', ')
        books.append(Book())
        books[i].isbn = line[0]
        books[i].title = line[1]
        books[i].price = float(line[2])
        theseAuthors = []
        for j, auth in enumerate(line[3::2]):
            
            theseAuthors.append(Author(auth, line[j+4]))
        print(theseAuthors)
        books[i].authors.extend(theseAuthors)
    
print(books[1].authors)
        
steve = Author("steve","aokf@{sdaf")
print(steve)

