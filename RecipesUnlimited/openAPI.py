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
myprompt = ("Provide an easy to cook recipe that may use some of these ingredients:\n"
            + canUse 
            + "\n\nAnd must be at least one of these ingredients:\n\n" + mustUse
            + "\n\nThis recipe doesn't need to be influenced by other suggestions"
            + "you have made")
myprompt = ("Provide a 1-2 sentence overview of 5 recipes sentences which"
            + " notes all it's key ingredients once. The recipe may only "
            + "use ingredients that are listed below:\n" + canUse
            + "\n\nThe suggestions must use at least one of these ingredients:\n"
            + mustUse +"\n\n")
print(myprompt)

    
cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
if cont != "1":
    sys.exit()
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=myprompt,
  max_tokens=600,
  temperature=0.01
)

print(response)