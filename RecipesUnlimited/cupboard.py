# -*- coding: utf-8 -*-
import time 
import re
import sqlite3


"""
Created on Sun Dec 25 22:37:12 2022

@author: Charl
"""
def firstCupboard(filename = "mycupboard.txt"):
    myCupboard = Cupboard([Ingredient("penne")])
    myCupboard.saveCupboard(filename)
    
def cupboardBuilder(filename = "mycupboard.txt"):
    myCupboard = Cupboard.loadCupboard(filename)
    
    contLoop = True
    while contLoop:
        nextIngredient = input("Please input name of ingredient: ")
        if nextIngredient == "":
            contLoop = False
            break
        myCupboard.addIngredient(Ingredient(nextIngredient))
    myCupboard.saveCupboard(filename)
    

def split_responses(response):
    response = """\n1. Penne with Olive Oil, Butter, White Pepper, and 
    Rosemary: A classic Italian dish with a twist, this recipe combines penne 
    pasta with olive oil, butter, white pepper, and rosemary for a delicious 
    and aromatic meal. \n2. Risotto Rice with Curry Powder, Ground Coriander, 
    and Eggs: A creamy and flavorful risotto dish, this recipe combines risotto 
    rice with curry powder, ground coriander, and eggs for a unique and delicious 
    meal. \n3. Buckwheat Tagliatelle with Garlic, Nutmeg, and Pine Nuts: A 
    delicious and hearty pasta dish, this recipe combines buckwheat tagliatelle 
    with garlic, nutmeg, and pine nuts for a flavorful and satisfying meal. \n4. 
    Polenta with Milk, Butter, and Jerk Seasoning: A savory and spicy dish, this 
    recipe combines polenta with milk, butter, and jerk seasoning for a unique 
    and flavorful meal. \n5. Urad Dal with Curry Leaves, Deggi Mirch, and Sesame 
    Seeds: A flavorful and aromatic Indian dish, this recipe combines urad dal 
    with curry leaves, deggi mirch, and sesame seeds for a delicious and 
    satisfying meal.
    """
    response = re.split(r"1.|2.|3.|4.|5.",response)
    
class Recipe:
    
    def __init__(self, name: str, ingredients: list, method: str, serves = 0,
                 prepTime = 0, cookTime = 0):
        self.name = name
        self.ingredients = ingredients
        self.method = method
        self.serves = serves
        self.prepTime = prepTime 
        self.cookTime = cookTime

class RecipeBook:
    #loads in recipes, adds recipes
    #saves recipes, removes recipes
    def __init__(self, recipe, filename):
        pass
    # def saveRecipes(self, file):
    #     #TODO: refactor to include column titles
    #     filecontents = self.cupboardToTxtLst()
    #     with open(file,'w',encoding = 'utf8') as fileref:
    #         #loop through each ingredient in cupboard
    #         #add to txt file containing all data
    #         fileref.write("name;shelflife;alwaysAvailable;created;expiry\n")
    #         for line in filecontents:
    #             fileref.write(line + "\n") if "\n" not in line else fileref.write(line)
        



class Ingredient:
    
    def __init__(self, name, shelflifeDays = -1, alwaysAvailable = 1, created = time.time(),
                 expiry = 0.0):
        self.name = name
        self.shelflifeDays = shelflifeDays
        self.alwaysAvailable = alwaysAvailable
        self.created = created
        if shelflifeDays != -1:
            shelflifeSecs = shelflifeDays*24*60*60
            self.expiry = created + shelflifeSecs
        else:
            self.expiry = expiry
    
    def __repr__(self):
        return (self.name + "\t\t\tShelflife: " + str(self.shelflifeDays) 
                + "\tAvailable: " + str(self.alwaysAvailable))
    
    def __str__(self):
        return (self.name + "\t\t\tShelflife: " + str(self.shelflifeDays) 
                + "\tAvailable: " + str(self.alwaysAvailable))
    
    def calcExpiry(created, shelflifeDays):
        if shelflifeDays != -1:
            shelflifeSecs = shelflifeDays*24*60*60
            return created + shelflifeSecs
        else:
            return 0.0
    
    def infolist(self):
        return [self.name, self.shelflifeDays, self.alwaysAvailable]
    
    def infotuple(self):
        return (self.name, self.shelflifeDays, self.alwaysAvailable, 
                self.created, self.expiry)
    
    def strOut(self):
        return (self.name + ";" + str(self.shelflifeDays) + ";" 
                + str(self.alwaysAvailable) + ";" + str(self.created)
                + ";" + str(self.expiry))
    
    def strIn(headers,s):
        #TODO: refactor to receive 2 strings, use strings to make dictionary
        #return Ingredient built with dictionary
        
        s = s.split(';')
        s = dict(zip(headers,s))
        return Ingredient(s["name"],int(s["shelflife"]),
                          int(s["alwaysAvailable"]),float(s["created"]),
                          float(s["expiry"]))
        # s = s.split(';')
        # return Ingredient(s[0],int(s[1]),int(s[2]),float(s[3]))
    
    def getName(self):
        return self.name
    
    def getExpiry(self):
        return self.expiry
        

class Cupboard:
    def __init__(self, ingredientList: list):
        self.ingredients = ingredientList
        
    def connectDb(self, name = "cupboardContents.db"):
        self.con = sqlite3.connect(name)
        self.dbname = name
        self.cur = self.con.cursor()
        """
        The returned Connection object con represents the connection to the on-disk database.

        In order to execute SQL statements and fetch results from SQL queries, we will 
        need to use a database cursor. Call con.cursor() to create the Cursor:
        """
    
    def createDb(self):
        """
        Now that we’ve got a database connection and a cursor, we can create a database 
        table movie with columns for title, release year, and review score. For 
        simplicity, we can just use column names in the table declaration – thanks to 
        the flexible typing feature of SQLite, specifying the data types is optional. 
        Execute the CREATE TABLE statement by calling cur.execute(...):
        """
        self.cur.execute("CREATE TABLE ingredient(name, shelflife, availability, created, expiry)")
        self.con.close()
        
    def saveDb(self):
        #TODO: refactor to include column titles
        filecontents = [ingredient.infotuple() for ingredient in self.listView()]
        dbname = self.dbname
        self.connectDb(dbname)
        self.cur.executemany("INSERT INTO ingredient VALUES(?, ?, ?, ?, ?)", filecontents)
        self.con.commit()
        self.con.close()
        
    def loadDb(file = "cupboardContents.db"):
        Cupboard.connectDb(file)
        output = [Ingredient(row[0],row[1],row[2],row[3],row[4]) 
                  for row in self.cur.execute("SELECT * FROM ingredient")]
        return Cupboard(output)
        
        
    def __repr__(self):
        output = ""
        for item in self.ingredients:
            output += str(item) + "\n"
        return output
        
    def loadCupboard(file):
        #TODO: Handle column titles
        with open(file, 'r', encoding = 'utf8') as fileref:
            #load in cupboard data
            #loop through lines in cupboard file
                #use data from each line to create new ingredient
                #add ingredient to cupboard list
            headers = fileref.readline().split(";")
            headers[-1] = headers[-1][:-1]
            output = [Ingredient.strIn(headers,line) for line in fileref.readlines()]
        return Cupboard(output)
    
    def saveCupboard(self, file):
        #TODO: refactor to include column titles
        filecontents = self.cupboardToTxtLst()
        with open(file,'w',encoding = 'utf8') as fileref:
            #loop through each ingredient in cupboard
            #add to txt file containing all data
            fileref.write("name;shelflife;alwaysAvailable;created;expiry\n")
            for line in filecontents:
                fileref.write(line + "\n") if "\n" not in line else fileref.write(line)
        
    
    def cupboardToTxtLst(self):
        return [item.strOut() for item in self.ingredients]
    
    def listView(self):
        return self.ingredients
    
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    def ingredientNames(self):
        return [ingredient.getName() for ingredient in self.ingredients]
    
    #TODO return all long life ingredients
    
    #TODO return all perishable ingredients
    
    #TODO remove ingredient from list

            
#Handles everything about what's in the cupboard
#loads list of ingredients into program
#saves ingredients to file
#returns list of indgredients and metadata about them
#return only ingredients always available
#returns list of ingredients that may be available but not definitely
#add ingredients to the list
#remove ingredients from the list
#



#Class Ingredients:
#a class with information about the ingredient
#name, amount, unlimited (ie always available) or frequently available,
#

#Class Recipes:
#Handles everything client side with recipes, including saving them 
#Collect all information needed to call ai
#Save recipe returned from ai
#