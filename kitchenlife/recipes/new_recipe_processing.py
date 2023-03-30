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
        ingredients = scraper.ingredients()
        if type(ingredients) == list:
            ingredients = list_cleaner(ingredients)
        else:
            ingredients = string_cleaner(ingredients)
        instructions = scraper.instructions()
        serves = scraper.yields()
        return Recipe(name = name, ingredients_string = ingredients, 
                    method = instructions, url = url, serves = serves, owner = owner)
    except:
        name = "Enter details manually"
        return Recipe(name = name, owner = owner)

def image_to_recipe(img, user):
    text = pytesseract.image_to_string(img)
    return text_to_recipe(text, user)

def text_to_recipe(text, user):
    text = openai_link.sendPromptJumbled(text, user.profile)
    # Define a list of possible headings and their corresponding variable names
    headings = [("Name:", "name"),
                ("Description:", "description"),
                ("Serves:", "serves"),
                ("Ingredients:", "ingredients"),
                ("Method:", "method")]

    # Initialize a dictionary to store the extracted information
    info = {var_name: None for _, var_name in headings}

    # Split the text using regular expressions to find the headings
    parts = resplit(r"(" + "|".join([h for h, _ in headings]) + ")", text)

    # Iterate through each section of the text and match it to the appropriate heading
    for i, part in enumerate(parts):
        if part.strip() == "":
            continue
        for heading, var_name in headings:
            if part == heading:
                info[var_name] = parts[i+1].strip()
                break

    # Remove the headings from the extracted information
    for var_name in info:
        if info[var_name] is not None:
            info[var_name] = info[var_name].replace(var_name + " ", "", 1)

    # Extract the information from the dictionary
    name = info["name"] if info["name"] else ""
    description = info["description"] if info["description"] else ""
    serves = info["serves"] if info["serves"] else ""
    ingredients = info["ingredients"] if info["ingredients"] else ""
    method = info["method"] if info["method"] else ""
    ingredients_string = string_cleaner(ingredients).strip()
    method = string_cleaner(method.replace('\n\n','\n')).strip()
    return Recipe(name = name.strip(), ingredients_string = ingredients_string , method = method, serves = serves.strip(),
                    description = description.strip(), owner = user, from_photo = True)

def string_cleaner(ingredients): #Removes any dashes or weird formatting from the start of each item
    return "\n".join([resub(r'^\W+', '', ingedient_line) for ingedient_line in ingredients.split('\n')])

def list_cleaner(ingredients): #Removes any dashes or weird formatting from the start of each item
    return "\n".join([resub(r'^\W+', '', ingedient_line) for ingedient_line in ingredients])