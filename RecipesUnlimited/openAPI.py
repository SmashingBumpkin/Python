import openai
import sys
import kitchenManager
from re import split as resplit
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:33:44 2022

@author: Charl
"""


#api key: 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

#openai.organization = "YOUR_ORG_ID"
def cupboardImporter():
    mycupboard = kitchenManager.Cupboard("kitchenContents.db")
    print(mycupboard)
    return mycupboard

def ingredientReturner(cupboard):
    return ", ".join(cupboard.returnLongLifeNames())
    
def perishableAdder(cupboard):
    #add perishable ingredients that could do with using to the cupboard
    cupboard.perishableChecker()
    perishables = cupboard.returnPerishableNames()
    if perishables:
        perishables = cupboard.returnPerishableNames()
        print("\n\nThese perishables remain from last time: \n")
        cupboard.printPerishablesNumbered()
        print("\nEnter any perishable ingredients that aren't available any more.")
        
        while True: #Remove any ingredients from this list?
            removeIngredient = input("Remove ingredient number: ")
            if removeIngredient == "":
                break
            cupboard.removeIngredient(perishables[int(removeIngredient)])
        perishables = cupboard.returnPerishableNames()
        mustUse = ", ".join(perishables)
    else:
        mustUse = ""
        print("There are no saved perishables")
    
    while True:
        nextIngredient = input("Input an ingredient that needs using: ")
        if nextIngredient == "":
            print("__________________________________\n\n\n")
            break
        shelflife = input("About how many days is the shelf life?: ")
        ingredient = kitchenManager.Ingredient(name = nextIngredient, 
                                         shelflifeDays = shelflife, alwaysAvailable = 0)
        cupboard.addIngredient(ingredient)
        mustUse += ", " + nextIngredient
    
    return mustUse

def recipebookImporter():
    myrecipes = kitchenManager.Cupboard("kitchenContents.db")
    print(myrecipes)
    return myrecipes


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
    
    print("\n_______________\n\n\n" + myprompt)
    return myprompt

def recipebookImporter():
    myrecipes = kitchenManager.RecipeBook("cupboardContents.db")
    return myrecipes

def recipeAdder(recipebook, recipe):
    #adds recipe to recipe book
    cont = int(input("\n\nType 1 to add the recipe to the recipe book: "))
    
    if cont:
        recipebook.addRecipe(Recipe.textToRecipe(recipe))
        print("Recipe added")
    else:
        print("\nRecipe not added.")
    
cupboard = cupboardImporter()
canUse = ingredientReturner(cupboard)
mustUse = perishableAdder(cupboard)
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
#recipe="\n\nPenne Alfredo with Black Mustard Seeds\n\nIngredients:\n\n- 1 package penne pasta\n- 2 tablespoons olive oil\n- 2 tablespoons vegetable oil\n- 2 tablespoons black mustard seeds\n- 2 cloves garlic, minced\n- 2 tablespoons ground cumin\n- 1 tablespoon dried basil\n- 1 tablespoon garam masala\n- 1 tablespoon paprika\n- 1 teaspoon turmeric\n- 1 teaspoon black pepper\n- 1 cup cooked basmati rice\n- 2 tablespoons pau bhaji\n- 1/4 cup pine nuts\n- 1/4 cup sesame seeds\n- 1/2 cup milk\n- 2 tablespoons butter\n- 2 eggs\n- 1 tablespoon rosemary, chopped\n\nInstructions:\n\n1. Bring a large pot of salted water to a boil and cook the penne according to package instructions. Drain and set aside.\n\n2. Heat the olive oil and vegetable oil in a large skillet over medium heat. Add the mustard seeds and cook until they start to pop, about 1 minute.\n\n3. Add the garlic, cumin, basil, garam masala, paprika, and turmeric and cook for another minute.\n\n4. Add the rice and pau bhaji and cook for 3-4 minutes, stirring occasionally.\n\n5. Add the pine nuts, sesame seeds, milk, butter, and eggs and cook until the eggs are cooked through, about 4 minutes.\n\n6. Add the penne and rosemary and toss to combine.\n\n7. Serve warm, topped with additional sesame seeds, if desired."

print(recipe)
recipebook = recipebookImporter()
recipeAdder(recipebook, recipe)
