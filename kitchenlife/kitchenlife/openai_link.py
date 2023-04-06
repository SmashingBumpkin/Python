import openai
from sys import exit as sysexit

def sendOpenAIRequest(messages, profile, typical_credits = 0):
    # replace with your OpenAI API key
    openai.api_key = "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"
    if profile.ai_credits < typical_credits:
        return False
    print("calling ai")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    costs = response["usage"]
    print(costs)
    profile.use_ai_credits(costs["total_tokens"])
    return response["choices"][0]["message"]["content"].strip()

def sendPromptIngredients(ingredients, profile):
    messages=[
        {"role": "system", "content": "You are a database for food and are only able to return a list of foods, you cannot return a quantity or anything which isn't an ingredient."},
        {"role": "user", "content": """This is a list of ingredients. Return a list "simple_ingredients", of names of the ingredient used, seperated by '\\n'. 
Each line in the returned content an exact substring of the line they are taken from, for example "350g whole (black) urad daal" must NOT return "Whole Urad Daal".

100g parmesan
300g mozzarella (2 balls)
800g chopped tomatoes (2 tins)
200g spinach
1 1/2 tsp ground cumin
1 Chopped red onion"""},
        {"role": "assistant", "content": """parmesan
mozzarella
chopped tomatoes
spinach
cumin
red onion"""},
        {"role": "user", "content": "Use the same process to modify this list of ingredients: \n\n' "
         +ingredients}
    ]
    typical_credits = 350
    return sendOpenAIRequest(messages, profile, typical_credits)

def sendPromptJumbled(jumbled_recipe, profile):
    messages = [
        {"role": "system", "content": """You are an expert at rearranging text which has been mixed up, and always return it in the same structure:
Name:
Description:
Serves:
Ingredients:
Method:"""},
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
    typical_credits = 500
    return sendOpenAIRequest(messages, profile, typical_credits)

def sendPromptIngredientDetails(ingredient, profile):
    print(ingredient + " is being added")
    messages = [
        {"role": "system", "content": "You are a database of ingredient details. You always return information in the exact format specified."},
        {"role": "user", "content": """Provide details of a typical example of this ingredient: Onion

Provide details in a precise format under the headings: substitutes, long life, typical shelf life (this should be how 
long many days the item can be expected to last if stored appropriately at home), Categories, typical weight 
(this should be the typical weight of an individual unit of the item, if not applicable, return 0),
Nutritional information per 100g/ml (Calories, Carbohydrates, Sugar, Fat, Protein, Fibre)

The "Categories" line should exclusively use any number of appropriate tags from this list seperated by commas:
Dairy
Meat
Poultry
Seafood
Vegetables
Fruits
Grains
Legumes
Nuts
Seeds
Spices
Herbs
Sweeteners
Oils
Vinegars
Alcoholic beverages
Non-alcoholic beverages
Baking supplies
Candy and sweets
Snacks"""},
        {"role": "assistant", "content": """Substitutes: Shallots, red onion, leek, garlic, spring onion
Long life: No
Typical shelf life: 10
Categories: Vegetables
Typical weight: 150g
Nutritional information:
Calories: 40
Carbohydrates: 9.3g
Sugar: 4.2g
Fat: 0.1g
Protein: 1.1g
Fibre: 1.7g"""},
        {"role": "user", "content": """Repeat the same instruction, with the exact same format, for: Milk"""},
        {"role": "assistant", "content": """Substitutes: Water, cream, butter
Long life: No
Typical shelf life: 7
Categories: Dairy, Non-alcoholic beverages
Typical weight: N/A
Nutritional information:
Calories: 47
Carbohydrates: 4.8g
Sugar: 4.5g
Fat: 1.8g
Protein: 3.6g
Fibre: 0g"""},
        {"role": "user", "content": "Repeat the same instruction, with the exact same format, for: "
         + ingredient}
    ]
    typical_credits = 520
    return sendOpenAIRequest(messages, profile, typical_credits)

def sendPromptForgottenDetails(myprompt, profile):
    messages = [
        #{"role": "system", "content": "You are a "},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Onion"""},
        {"role": "assistant", "content": """Vegetable"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Milk"""},
        {"role": "assistant", "content": """Dairy"""},
        {"role": "user", "content": """Categorize this ingredient into a typical food category: Cumin"""},
        {"role": "assistant", "content": """Spice"""},
        {"role": "user", "content": "Categorize this ingredient into a typical food category: "+myprompt}
    ]
    typical_credits = 500
    return sendOpenAIRequest(messages, profile, typical_credits)

def sendPromptRecipeDescription(recipe, profile):
    prompt_input  = recipe.name + "\n"
    prompt_input += recipe.description
    messages = [
        #{"role": "system", "content": "You are a "},
        {"role": "user", "content": """Provide a brief 1-2 sentence description of this recipe:

Drain the ricotta in a sieve to get rid of any excess water, then into a large bowl. Toast the pumpkin seeds in a dry frying pan until they begin to pop. Set aside.
Finely chop most of the herbs (stalks and all). Add the flour, egg yolks, and herbs to the ricotta. Finely grate in the lemon zest and the pecorino cheese. Season generously with salt and black pepper then mix everything together to form a dough.
Bring a large saucepan of salted water to the boil.
Tip the gnocchi dough onto a really well-floured surface. With floured hands knead briefly until smooth; the dough should feel light, sticky to touch but keep its shape well.
Cut the dough into six, then, flouring your hands, roll one piece into a sausage around 2cm (0.8in) thick. Cut into bite-sized pieces. Transfer to a large, well-floured baking tray. Repeat with the remaining dough.
Working in batches, drop the gnocchi into the boiling water. Cook for 1-2 minutes until they float. With a slotted spoon, transfer to a clean baking tray. Repeat until all the gnocchi has been cooked.
Get a large frying pan over a medium heat. Add the butter and let it melt until it turns lightly brown and begins to smell nutty. Add the toasted pumpkin seeds, capers and gnocchi. Give everything a toss to warm the gnocchi back through. Cut the lemon in half and squeeze in some of the juice. Season to taste with salt and black pepper.
Divide the gnocchi and brown butter sauce between four plates. Over some pecorino cheese and tear over the remaining herbs to serve."""},
        {"role": "assistant", "content": """The lightest, most delicate pillows of pasta you could ask for, served in a brown butter sauce with capers and toasted pumpkin seeds, this dish is super-light yet still feels indulgently rich."""},
        {"role": "user", "content": "Now generate a description for this recipe: "
         + prompt_input}
    ]
    typical_credits = 500
    return sendOpenAIRequest(messages, profile, typical_credits)

def sendPromptMealTags(recipe, profile):
    prompt_input  = recipe.name + "\n"
    if recipe.description:
        prompt_input += recipe.description
    else:
        prompt_input += recipe.method
    messages = [
        #{"role": "system", "content": "You are a "},
        {"role": "user", "content": """This is a list of all possible tags.
Your response should be a combination of any number of these exact tags, seperated by a comma:
Breakfast
Brunch
Lunch
Dinner
Appetizer
Main dish
Side dish
Salad
Soup
Snack
Dessert
Baked goods
Vegetarian
Vegan
Gluten-free
Dairy-free
Quick and easy

Apply these tags to this recipe:

Veggie Lasagne
Preheat the oven to 200C/180C Fan/Gas 6. Put the peppers, courgette and sweet potato into a large baking tray. Drizzle with 2 tablespoons of the oil, season with salt and pepper and toss together.
Roast for 30 minutes, or until softened and lightly browned.
While the vegetables are roasting, heat the remaining oil in a large saucepan and gently fry the onion for 5 minutes, stirring regularly.
Add the chilli and garlic and cook for a few seconds more. Stir in the tomatoes, Italian seasoning (or dried oregano) and crumbled stock cube. Pour over the water and bring to a gentle simmer. Cook for 10 minutes, stirring regularly. Set aside.
For the cheese sauce, put the flour, butter and milk in a large saucepan and place over a medium heat. Whisk constantly with a large metal whisk until the sauce is thickened and smooth. (Use a silicone covered whisk if cooking in a non-stick pan.) Stir in roughly two-thirds of the cheeses and season to taste.
Take the vegetables out of the oven and add to the pan with the tomato sauce. Stir in the spinach and cook together for 3 minutes. Season with salt and lots of ground black pepper.
Spoon a third of the vegetable mixture over the base of a 2½–3 litre/4½–5¼ pint ovenproof lasagne dish and cover with a single layer of lasagne. Top with another third of the vegetable mixture (don’t worry if it doesn’t cover evenly) and a second layer of lasagne.
Pour over just under half of the cheese sauce and very gently top with the remaining vegetable mixture. Finish with a final layer of lasagne and the rest of the cheese sauce. Sprinkle the reserved cheese over the top.
Bake for 35–40 minutes, or until the pasta has softened and the topping is golden brown and bubbling. Stand for 5 minutes before cutting to allow the filling to settle.
"""     },
        {"role": "assistant", "content": """Dinner, Main dish, Vegetarian """},
        {"role": "user", "content": """Use the same list of tags for this recipe:\n\n"""
         + prompt_input}]
    typical_credits = 500
    return sendOpenAIRequest(messages, profile, typical_credits)