import openai
import sys
import cupboard
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:33:44 2022

@author: Charl
"""

#api key: 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

#openai.organization = "YOUR_ORG_ID"
openai.api_key = "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"

def cupboardImporter():
    mycupboard = cupboard.Cupboard.loadCupboard("mycupboard.txt")
    print(mycupboard)
    return mycupboard

mycupboard = cupboardImporter()
canUse = mycupboard.ingredientNames()
canUse = ", ".join(canUse)

mustUse = ""
while True:
    nextIngredient = input("Input an ingredient that needs using: ")
    if nextIngredient == "":
        break
    mustUse += nextIngredient + ", "

mustUse = mustUse[:-2]
print("Here are some ingredients that may be used in a recipe: \n\n" + canUse 
      + "\n\n\nHere is another list of ingredients. At least one of these must be used:\n\n" + mustUse
      +"\n\n\nProvide an easy to cook recipe that uses only the ingredients listed above")
    
cont = input("\n\n\n\nPlease type 1 to continue (will spend openai credits) ")
if cont != "1":
    sys.exit()
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt=myprompt,
#   max_tokens=7,
#   temperature=0
# )
# print(response)