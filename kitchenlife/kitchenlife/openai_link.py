import openai
from sys import exit as sysexit

def sendOpenAIRequest(messages, profile):
    # replace with your OpenAI API key
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    profile.ai_credits_used += response["usage"]["total_tokens"]
    profile.save()
    return response["choices"][0]["message"]["content"].strip()

def sendPromptIngredients(ingredients, profile):
    messages=[
        {"role": "user", "content": """This is a list of ingredients. Return a list "simple_ingredients", of names of the ingredient used, seperated by '\\n'. 
Each line in the returned content an exact substring of the line they are taken from, for example "350g whole (black) urad daal" must NOT return "Whole Urad Daal".

100g parmesan
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
        {"role": "user", "content": "Use the same process to modify this list of ingredients: \n\n' "
         +ingredients}
    ]
    return sendOpenAIRequest(messages, profile)

def sendPromptJumbled(jumbled_recipe, profile):
    messages = [
        {"role": "user", "content": """The following excerpt is a jumbled up recipe. Reformat this recipe with the headers
name, description, serves, ingredients and then the method. Correct the capitalization where applicable:
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
        {"role": "user", "content": """The following excerpt is a jumbled up recipe. Reformat this recipe with the headers
name, description, serves, ingredients and then the method. Correct the capitalization where applicable:

Millie's Cookies recipe
By

    alice1211 (GoodFood Community)

A star rating of 4.8 out of 5.470 ratingsRate
418 comments
Magazine subscription – your first 5 issues for only £5!

    Preparation and cooking time
        Total time15 mins
    More effort
    Makes Cookies

These delicious cookies are easy to cook and taste as good as the real Millies cookies, with a crisp outer layer and a gooey centre these treats are best eaten warm but last well...if they last that long!!!
Ingredients

    125g butter, softened
    100g light brown soft sugar
    125g caster sugar
    1 egg, lightly beaten
    1 tsp vanilla extract
    225g self-raising flour
    ½ tsp salt
    200g chocolate chips

Method

    STEP 1
    Preheat the oven to 180°C, gas mark 4
    STEP 2
    Cream butter and sugars, once creamed, combine in the egg and vanilla.
    STEP 3
    Sift in the flour and salt, then the chocolate chips.
    STEP 4
    Roll into walnut size balls, for a more homemade look, or roll into a long, thick sausage shape and slice to make neater looking cookies.
    STEP 5
    Place on ungreased baking paper. If you want to have the real Millies experience then bake for just 7 minutes, till the cookies are just setting - the cookies will be really doughy and delicious. Otherwise cook for 10 minutes until just golden round the edges.
    STEP 6
    Take out of the oven and leave to harden for a minute before transferring to a wire cooling rack. These are great warm, and they also store well, if they don't all get eaten straight away!"""},
        {"role": "assistant", "content": """Name: Millie's Cookies recipe
Description: These delicious cookies are easy to cook and taste as good as the real Millies cookies, with a crisp outer layer and a gooey centre these treats are best eaten warm but last well...if they last that long!!!
Serves:
Ingredients:
125g butter, softened
100g light brown soft sugar
125g caster sugar
1 egg, lightly beaten
1 tsp vanilla extract
225g self-raising flour
½ tsp salt
200g chocolate chips

Method:
1: Preheat the oven to 180°C, gas mark 4
2: Cream butter and sugars, once creamed, combine in the egg and vanilla.
3: Sift in the flour and salt, then the chocolate chips.
4: Roll into walnut size balls, for a more homemade look, or roll into a long, thick sausage shape and slice to make neater looking cookies.
5: Place on ungreased baking paper. If you want to have the real Millies experience then bake for just 7 minutes, till the cookies are just setting - the cookies will be really doughy and delicious. Otherwise cook for 10 minutes until just golden round the edges.
6: Take out of the oven and leave to harden for a minute before transferring to a wire cooling rack. These are great warm, and they also store well, if they don't all get eaten straight away!"""},
        {"role": "user", "content": "Using the same headings, correct this jumbled up recipe:"
         + jumbled_recipe}
    ]
    return sendOpenAIRequest(messages, profile)

def sendPromptIngredientDetails(ingredient, profile):
    messages = [
        {"role": "user", "content": """Provide details of a typical example of this ingredient: Onion
Provide details in a precise format under the headings: substitutes, long life, typical shelf life (this should be how 
long many days the item can be expected to last if stored appropriately at home), Category, typical weight 
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
        {"role": "user", "content": "Using the same headings, provide details of a typical example of this ingredient: "
         + ingredient}
    ]
    return sendOpenAIRequest(messages, profile)

def sendPromptForgottenDetails(myprompt, profile):
    messages = [
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Onion"""},
        {"role": "assistant", "content": """Vegetable"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Milk"""},
        {"role": "assistant", "content": """Dairy"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Cumin"""},
        {"role": "assistant", "content": """Spice"""},
        {"role": "user", "content": "Categorize this ingredient into a typical food category: "+ingredient}
    ]
    return sendOpenAIRequest(messages, profile)
