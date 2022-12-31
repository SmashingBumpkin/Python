# -*- coding: utf-8 -*-
import time 
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