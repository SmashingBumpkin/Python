import openai
from sys import exit as sysexit

def sendPrompt(myprompt, active_user, temperature = 0.01, model = "text-davinci-003"):
    cont = input("\n____\n\n\nPlease type 1 to continue (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.Completion.create(
      model=model,
      prompt=myprompt,
      max_tokens=600,
      temperature=temperature
    )
    active_user.ai_credits_used += response["usage"]["total_tokens"]
    active_user.save()
    return response["choices"][0]["text"]

def sendPromptIngredients(myprompt, active_user):
    #https://platform.openai.com/docs/guides/chat
    cont = input("\n____\n\n\nPlease type 1 to continue ingredient simplifier (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Modify this list to return each individual ingredient seperated by '\\n'
\n100g parmesan
300g mozzarella (2 balls)
800g chopped tomatoes (2 tins)
200g spinach
1 1/2 tsp ground cumin
Chopped red onion"""},
        {"role": "assistant", "content": """parmesan
mozzarella
chopped tomatoes
spinach
cumin
red onion"""},
        {"role": "user", "content": "Now repeat modify this list of ingredients, remove anything that isn't a basic ingredient, (if appropriate) make the ingredient singular, and seperate by '\\n' "+myprompt}
    ]
    )
    active_user.ai_credits_used += response["usage"]["total_tokens"]
    active_user.save()
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]


def sendPromptJumbled(myprompt, active_user):
    #https://platform.openai.com/docs/guides/chat
    cont = input("\n____\n\n\nPlease type 1 to continue de-jumbler (will spend openai credits) ")
    if cont != "1":
        print("\nYou have terminated the program, cheapskate.\n")
        sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """The following excerpt is a jumbled up recipe. Reformat this recipe with the headers
name, description, serves, ingredients and then the method. Correct the capitalization where applicable."'\\n'
Spaghetti Bolognese
ServesClassic spagghetti bolognese
4
400g spaghetti1. Boil the pasta for
1 Jar bolognese sauce12 minutes
2. Heat the sauce for 2 minutes then add the pasta."""},
        {"role": "assistant", "content": """Name:
Spaghetti Bolognese
Description:
Classic spagghetti bolognese
Serves:
4
Ingredients:
400g spaghetti
1 Jar bolognese sauce
Method:
1. Boil the pasta for 12 minutes
2. Heat the sauce for 2 minutes then add the pasta."""},
        {"role": "user", "content": "Using the same headings, correct this jumbled up recipe:"+myprompt}
    ]
    )
    active_user.ai_credits_used += response["usage"]["total_tokens"]
    active_user.save()
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]


def sendPromptIngredientDetails(ingredient, user):
    #https://platform.openai.com/docs/guides/chat
    #cont = input("\n____\n\n\nPlease type 1 to continue ingredient detailer (will spend openai credits) ")
    # if cont != "1":
    #     print("\nYou have terminated the program, cheapskate.\n")
    #     sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Provide details of a typical example of this ingredient: Onion
Provide details under the headings: substitutes, long life, typical shelf life (this should be how 
long the item can be expected to last if stored appropriately at home), Category, typical weight 
(this should be the typical weight of an individual unit of the item, if not applicable, return 0),
Nutritional information per 100g/ml (Calories, Carbohydrates, Sugar, Fat, Protein, Fibre)"""},
        {"role": "assistant", "content": """Substitutes: Shallots, red onion, leek, garlic, spring onion
Long life: No
Typical shelf life: 10
Category: Vegetable
Typical weight: 150g
Nutritional information:
Calories: 40
Carbohydrates: 9.3g
Sugar: 4.2g
Fat: 0.1g
Protein: 1.1g
Fibre: 1.7g"""},
        {"role": "user", "content": """Provide details of a typical example of this ingredient: Milk
Provide details under the headings: substitutes, long life, typical shelf life, Category, 
typical weight, Nutritional information per 100g/ml (Calories, Carbohydrates, Sugar, Fat, Protein, Fibre)"""},
        {"role": "assistant", "content": """Substitutes: Water, cream, butter
Long life: No
Typical shelf life: 7
Category: Dairy
Typical weight: N/A
Nutritional information:
Calories: 47
Carbohydrates: 4.8g
Sugar: 4.5g
Fat: 1.8g
Protein: 3.6g
Fibre: 0g"""},
        {"role": "user", "content": "Using the same headings, provide details of a typical example of this ingredient: "+ingredient}
    ]
    )
    user.profile.ai_credits_used += response["usage"]["total_tokens"]
    user.profile.save()
    print(ingredient.capitalize() + "\n\n")
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]

def sendPromptForgottenDetails(ingredient, user):
    #https://platform.openai.com/docs/guides/chat
    #cont = input("\n____\n\n\nPlease type 1 to continue ingredient detailer (will spend openai credits) ")
    # if cont != "1":
    #     print("\nYou have terminated the program, cheapskate.\n")
    #     sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Onion"""},
        {"role": "assistant", "content": """Vegetable"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Milk"""},
        {"role": "assistant", "content": """Dairy"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Cumin"""},
        {"role": "assistant", "content": """Spice"""},
        {"role": "user", "content": "Categorize this ingredient into a typical food category: "+ingredient}
    ]
    )
    user.profile.ai_credits_used += response["usage"]["total_tokens"]
    user.profile.save()
    print(ingredient.capitalize() + "\n\n")
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]

def sendPromptTypicalWeight(ingredient, user):
    #https://platform.openai.com/docs/guides/chat
    #cont = input("\n____\n\n\nPlease type 1 to continue ingredient detailer (will spend openai credits) ")
    # if cont != "1":
    #     print("\nYou have terminated the program, cheapskate.\n")
    #     sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Provide a typical weight in grams of an individual unit of garlic"""},
        {"role": "assistant", "content": """3"""},
        {"role": "user", "content": """Provide a typical weight in grams of an individual unit of apple"""},
        {"role": "assistant", "content": """120"""},
        {"role": "user", "content": """Provide a typical weight in grams of an individual unit of flour"""},
        {"role": "assistant", "content": """0"""},
        {"role": "user", "content": "Provide a typical weight in grams of an individual unit of "+ingredient
         + "\nIf this doesn't apply to the ingredient in question, reply with 0"}
    ]
    )
    user.profile.ai_credits_used += response["usage"]["total_tokens"]
    user.profile.save()
    print(ingredient.capitalize() + "\n\n")
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]

def sendPromptTypicalShelfLife(ingredient, user):
    #https://platform.openai.com/docs/guides/chat
    #cont = input("\n____\n\n\nPlease type 1 to continue ingredient detailer (will spend openai credits) ")
    # if cont != "1":
    #     print("\nYou have terminated the program, cheapskate.\n")
    #     sysexit()
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": """Provide the typical shelflife in days of garlic"""},
        {"role": "assistant", "content": """12"""},
        {"role": "user", "content": """Provide the typical shelflife in days of apple"""},
        {"role": "assistant", "content": """8"""},
        {"role": "user", "content": """Provide the typical shelflife in days of flour"""},
        {"role": "assistant", "content": """365"""},
        {"role": "user", "content": "Provide the typical shelflife in days of "+ingredient}
    ]
    )
    user.profile.ai_credits_used += response["usage"]["total_tokens"]
    user.profile.save()
    print(ingredient.capitalize() + "\n\n")
    print(response["choices"][0]["message"]["content"])
    return response["choices"][0]["message"]["content"]