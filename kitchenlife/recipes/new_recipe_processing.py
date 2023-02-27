from re import split as resplit
from kitchenlife import openai_link
from .models import Recipe
from recipe_scrapers import scrape_me #https://github.com/hhursev/recipe-scrapers

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def url_to_recipe(url, owner):
    try:
        scraper = scrape_me(url, wild_mode=True)
        name = scraper.title()
        ingredients = scraper.ingredients()
        instructions = scraper.instructions()
        serves = scraper.yields()
        return Recipe(name = name, ingredients_string = '\n'.join(ingredients), 
                    method = instructions, url = url, serves = serves, owner = owner)
    except:
        name = "Enter details manually"
        return Recipe(name = name, owner = owner)

def image_to_string(img, active_user):
    text = pytesseract.image_to_string(img)
    myprompt = ("The following excerpt is a jumbled up recipe. Reformat this recipe with the headers"+
            " name, description, serves, ingredients and then the method. Correct the capitalization where applicable."#Modify prompt to check for "9s"
            + "\n\n" + text)
    text = openai_link.sendPrompt(myprompt, active_user=active_user)
    # text = temptext()
    return text

def text_to_recipe(text):
        [_,name,description, serves, ingredients, method] = textlist= resplit(r"Name:|Description:|Serves:|Ingredients:|Method:",text)
        method = method.replace('\n\n','\n')
        return Recipe(name = name.strip(), ingredients_string = ingredients.strip(), method = method.strip(), serves = serves.strip(),
                        description = description.strip())