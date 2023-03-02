from re import split as resplit, sub as resub
from kitchenlife import openai_link
from .models import Recipe
from recipe_scrapers import scrape_me #https://github.com/hhursev/recipe-scrapers

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def url_to_recipe(url, owner):
    try:
        scraper = scrape_me(url, wild_mode=True)
        name = scraper.title()
        ingredients = list_cleaner(scraper.ingredients())
        instructions = scraper.instructions()
        serves = scraper.yields()
        return Recipe(name = name, ingredients_string = '\n'.join(ingredients), 
                    method = instructions, url = url, serves = serves, owner = owner)
    except:
        name = "Enter details manually"
        return Recipe(name = name, owner = owner)

# def image_to_string(img, active_user):
#     text = pytesseract.image_to_string(img)
#     print(text)
#     return openai_link.sendPromptJumbled(text, active_user)
    

def image_to_recipe(img, user):
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        #
        #
        #
        #TODO: THIS IS NOT AT ALL ROBUST!!!!!!!!!!!!!!!!
        #
        #
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        text = pytesseract.image_to_string(img)
        text = openai_link.sendPromptJumbled(text, user.profile)
        [_,name,description, serves, ingredients, method] = textlist= resplit(r"Name:|Description:|Serves:|Ingredients:|Method:",text)
        # method = method.replace('\n\n','\n')
        ingredients_string = list_cleaner(ingredients).strip()
        method = list_cleaner(method.replace('\n\n','\n')).strip()
        return Recipe(name = name.strip(), ingredients_string = ingredients_string , method = method, serves = serves.strip(),
                        description = description.strip(), owner = user, from_photo = True)

def list_cleaner(ingredients): #Removes any dashes or weird formatting from the start of each item
    return "\n".join([resub(r'^\W+', '', ingedient_line) for ingedient_line in ingredients.split('\n')])