import openai
import sys
import cupboard
from re import split as resplit
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:33:44 2022

@author: Charl
"""

#load in cupboard


#api key: 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

#openai.organization = "YOUR_ORG_ID"
def cupboardImporter():
    mycupboard = cupboard.Cupboard.loadCupboard("mycupboard.txt")
    print(mycupboard)
    return mycupboard

def ingredientReturner(cupboard):
    return ", ".join(cupboard.ingredientNames())



def perishableChecker(cupboard):    #load in 
    print("These perishable ingredients are saved:")
    #display perishable ingredients from cupbaord
    
    
    print("Enter any perishable ingredients that aren't available any more")
    
    while True: #Remove any ingredients from this list?
        removeIngredient = input("Remove ingredient number: ")
        if nextIngredient == "":
            break
        #remove ingredient from list
    
    #save updated list
    
def perishableAdder():
    #add perishable ingredients that could do with using to the cupboard
    while True:
        nextIngredient = input("Input an ingredient that needs using: ")
        if nextIngredient == "":
            break
        shelflife = input("About how many days is the shelf life?': ")
        #add to cupboard
    #save updated cupboard
    

def mustUsePrompt():
    #refactor to simply load in perishables from cupboard
    mustUse = ""
    while True:
        nextIngredient = input("Input an ingredient that needs using: ")
        if nextIngredient == "":
            break
        shelflife = input("About how many days is the shelf life?': ")
        mustUse += nextIngredient + ", "
    return mustUse[:-2]


def optionsPrompt(mustUse, canUse):
    myprompt = ("Provide a 1-2 sentence overview of 5 recipes sentences which"
                + " notes all it's key ingredients once. The recipe may only "
                + "use ingredients that are listed below:\n" + canUse
                + "\n\nThe suggestions must use at least one of these ingredients:\n"
                + mustUse +"\n\n")
    print(myprompt)
    return myprompt

def optionsPromptBroad(mustUse, canUse):
    myprompt = ("Provide a 1-2 sentence overview of 5 recipes sentences which"
                + " notes all it's key ingredients once. The recipe can use "
                + "ingredients that are listed below:\n" + canUse
                + "\n\nThe suggestions must use at least one of these ingredients:\n"
                + mustUse +"\n\nThe suggestions should also use one or two "
                + "ingredients that aren't listed here.")
    print(myprompt)
    return myprompt

def sendPrompt(myprompt):
    cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sys.exit()
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=myprompt,
      max_tokens=600,
      temperature=0.01
    )
    return response["choices"][0]["text"]

def optionChooser(options):
    options = resplit(r"1.|2.|3.|4.|5.",options)
    #ask user which suggestion they like the sound of
    optionChoice = int(input("Which of the suggestions sounded good? (eg \"1\") "))
    return options[optionChoice]

def recipePrompt(outline, mustUse, canUse):
    myprompt = ("Write a recipe for this dish: \n\n" + outline
                + "\nthe recipe can include any of these ingredients:\n"
                + canUse + mustUse)
    return myprompt
    

canUse = ingredientReturner(cupboardImporter())
mustUse = mustUsePrompt()
myprompt = optionsPromptBroad(mustUse,canUse)
options = sendPrompt(myprompt)
"""options = \n1. Penne with Olive Oil, Butter, White Pepper, and 
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
print(options)
option = optionChooser(options)
recipeRequest = recipePrompt(option, mustUse, canUse)
recipe = sendPrompt(recipeRequest)

print(recipe)
