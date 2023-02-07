from re import split as resplit
from kitchenlife import openai_link
from .models import Recipe

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def image_to_string(img):
    text = pytesseract.image_to_string(img)
    myprompt = ("The following excerpt is a jumbled up recipe. Reformat this recipe "+
            "to be the name, the description, how many it serves, the ingredients and then the method."
            + "\n\n" + text)
    text = openai_link.sendPrompt(myprompt)
    return text

def image_to_string(img):
    text = pytesseract.image_to_string(img)
    myprompt = ("The following excerpt is a jumbled up recipe. Reformat this recipe with the headers"+
            " name, description, serves, ingredients and then the method."
            + "\n\n" + text)
    #text = openai_link.sendPrompt(myprompt)
    text = temptext()
    return text

def text_to_recipe(text):
        [_,name,description, serves, ingredients, method] = textlist= resplit(r"Name:|Description:|Serves:|Ingredients:|Method:",text)
        return Recipe(name = name.strip(), ingredients_string = ingredients.strip(), method = method.strip(), serves = serves.strip(),
                        description = description.strip())

def temptext():
    return """'Name: Bean and Veg-Loaded Broths\n\nDescription: This is a bit like a minestrone but with a heat from the ’nduja. We love the ditalini, but small macaroni would also work well with whatever ingredients you’ve got.\n\nServes: 4\n\nIngredients:\n- 1 onion\n- 1 carrot\n- 1 celery stick\n- 2 tbsp olive oil\n- 1 sprig of rosemary\n- 60g (24/402) ’nduja\n- 1 tsp tomato purée\n- 200g (7oz) cherry tomatoes\n- 1 litre (1% pints) chicken stock\n- 1 x 400 (1402) tin of cannellini beans\n- 250g (90z) ditalini or macaroni\n- 200g (7oz) cavolo nero\n- 20g (940z) Parmesan\n- Salt and black pepper\n\nMethod:\n1. Very finely dice the onion, carrot and celery.\n2. Heat the olive oil in a large saucepan. Add the diced veg and sprig of rosemary and cook over a medium heat for 15 minutes until softened, adding a splash of water if they start to stick.\n3. Add the ‘nduja to the pan along with the tomato purée. Cook, stirring, for 2 minutes until the ’nduja has released its oil and the mixture has darkened.\n4. Halve the cherry tomatoes and add to the pan: cook for 5 minutes, squishing them up with the back of your spoon to break them down.\n5. Add the chicken stock, then top it up with another 500ml (171 oz) of water. Bring it to a simmer, then season to taste with salt.\n6. Drain the cannellini beans, then tip these into the pan along with your pasta. Simmer for 5 minutes.\n7. Meanwhile, tear the stalks away from the cavolo nero leaves and discard them. Tear the leaves into rough pieces. Once the 5 minutes are up, add the cavolo nero leaves to the pan. Simmer for another 3 minutes.\n8. Check that your pasta is tender, then adjust the seasoning with salt and pepper. Spoon into bowls then grate over the Parmesan to serve. Enjoy!'
    """

