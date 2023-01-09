# -*- coding: utf-8 -*-
import time 
from re import split as resplit
import sqlite3


"""
Created on Sun Dec 25 22:37:12 2022

@author: Charl
"""
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
    responseDEL = """\n1. Penne with Olive Oil, Butter, White Pepper, and 
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
    response = resplit(r"1.|2.|3.|4.|5.",response)
    
class Recipe:
    
    def __init__(self, name: str, ingredients,method, description = None,
                 favourite = 0, score = None):
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.method = method
        self.favourite = favourite
        self.score = score
        
    def __repr__(self):
        return ("\n__________________________________\n\n" 
                + "\n\n".join([self.name, self.ingredients, self.method]))
    
    def textToRecipe(text):
        [name, ingredients] = text.strip().split("\n\n",1)
        [_, ingredients, method] = resplit(r"Ingredients:|Instructions:",ingredients)
        return Recipe(name = name.strip(), ingredients = ingredients.strip(), method = method.strip())
    
    def infotuple(self):
        return (self.name, self.ingredients, self.method, self.description, 
                self.favourite, self.score)
        

class RecipeBook:
    #loads in recipes, adds recipes
    #saves recipes, removes recipes
    def __init__(self, name = "cupboardContents.db", firstUse = 0):
        self.dbname = name
        if firstUse:
            self.createDb()
        self.connectDb()
        self.con.close()
    
    def __repr__(self):
        #TODO Refactor to display recipe book
        recipes = self.returnRecipes()
        output = ""
        for item in recipes:
            output += str(item) + "\n\n_______________\n\n"
        return output
        
    def connectDb(self):
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()
    
    def createDb(self):
        self.connectDb()
        #Creates a new database
        self.cur.execute("CREATE TABLE recipe(name, ingredients, method, description, favourite, score)")
        self.con.commit()
        self.con.close()
    
    def addRecipe(self, recipe):
        #adds the ingredient to the mysql database
        self.connectDb()
        #TODO check for duplicates
        self.cur.execute("INSERT INTO recipe VALUES(?, ?, ?, ?, ?,?)", 
                             recipe.infotuple())
        self.con.commit()
        self.con.close()
        
    def removeRecipe(self, recipe: str):
        #Removes ingredient from mysql database
        self.connectDb()
        self.cur.execute(f"DELETE FROM recipe WHERE name=?", (recipe,))
        self.con.commit()
        self.con.close()
    
    def returnRecipes(self):
        self.connectDb()
        output = [Recipe(name = row[0], ingredients = row[1],method = row[2],
                         description = row[3],favourite = row[4], score = row[5]) 
                  for row in self.cur.execute(
                          "SELECT * FROM recipe")]
        self.con.close()
        return output
    
    def returnFavourites(self):
        self.connectDb()
        output = [Ingredient(row[0],row[1],row[2],row[3],row[4]) 
                  for row in self.cur.execute(
                          "SELECT * FROM recipe WHERE favourite=1")]
        self.con.close()
        return output
        
        


class Ingredient:
    #a class with information about the ingredient
    #name, amount, unlimited (ie always available) or frequently available,
    #
    
    def __init__(self, name, shelflifeDays = -1, alwaysAvailable = 1, created = time.time(),
                 expiry = 0.0):
        self.name = name
        self.shelflifeDays = int(shelflifeDays)
        self.alwaysAvailable = alwaysAvailable
        self.created = created
        if shelflifeDays != -1:
            shelflifeSecs = int(shelflifeDays)*24*60*60
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
    
    def getAvailability(self):
        #returns if the ingredient is long life and always available
        return self.alwaysAvailable
    
        

class Cupboard:
    def __init__(self, name = "kitchenContents.db"):
        self.dbname = name
    
    def __repr__(self):
        ingredients = self.returnAllIngredients()
        output = ""
        for item in ingredients:
            output += str(item) + "\n"
        return output
        
    def connectDb(self):
        self.con = sqlite3.connect(self.dbname)
        self.cur = self.con.cursor()
    
    def createDb(self):
        #Creates a new database
        self.cur.execute("CREATE TABLE ingredient(name, shelflife, availability, created, expiry)")
        self.con.close()
    
    def addIngredient(self, ingredient):
        #adds the ingredient to the mysql database
        self.connectDb()
        #TODO check for duplicates
        self.cur.execute("INSERT INTO ingredient VALUES(?, ?, ?, ?, ?)", 
                             ingredient.infotuple())
        self.con.commit()
        self.con.close()
        
    def removeIngredient(self, ingredient: str):
        #Removes ingredient from mysql database
        self.connectDb()
        self.cur.execute(f"DELETE FROM ingredient WHERE name=?", (ingredient,))
        self.con.commit()
        self.con.close()
        
    def returnLongLife(self):
        self.connectDb()
        output = [Ingredient(row[0],row[1],row[2],row[3],row[4]) 
                  for row in self.cur.execute(
                          "SELECT * FROM ingredient WHERE availability=1")]
        self.con.close()
        return output
    
    def returnLongLifeNames(self):
        ingredients = self.returnLongLife()
        return [ingredient.getName() for ingredient in ingredients]
    
    def perishableChecker(self):
        #Checks the dates of all perishable items in cupboard, and removes any
        #that are expired
        perishables = self.returnPerishable()
        currentTime = time.time()
        expired = [item.getName() for item in perishables
                   if item.getExpiry() < currentTime]
        for item in expired:
            self.removeIngredient(item)
        print("These items are expired and have been removed:\n")
        print(", ".join(expired))
        
        
    
    def returnPerishable(self):
        self.connectDb()
        output = [Ingredient(row[0],row[1],row[2],row[3],row[4]) 
                  for row in self.cur.execute(
                          "SELECT * FROM ingredient WHERE availability=0")]
        self.con.close()
        return output
    
    def returnPerishableNames(self):
        ingredients = self.returnPerishable()
        return [ingredient.getName() for ingredient in ingredients]
    
    def returnPerishablesNumbered(self):
        return [(index, ingredient) for index, ingredient in enumerate(self.returnPerishableNames())]
    
    def printPerishablesNumbered(self):
        numberedPerishables = self.returnPerishablesNumbered()
        for (index, ingredient) in numberedPerishables:
            print(str(index) + ": " + ingredient)
        
        
    def returnAllIngredients(self):
        self.connectDb()
        output = [Ingredient(row[0],row[1],row[2],row[3],row[4]) 
                  for row in self.cur.execute("SELECT * FROM ingredient")]
        self.con.close()
        return output
    
    def cupboardToTxtLst(self):
        return [item.strOut() for item in self.ingredients]

            
#Handles everything about what's in the cupboard
#loads list of ingredients into program
#saves ingredients to file
#returns list of indgredients and metadata about them
#return only ingredients always available
#returns list of ingredients that may be available but not definitely
#add ingredients to the list
#remove ingredients from the list
#
