def convert_to_grams(quantity, unit):
    unit = unit.lower()
    if unit in ("g", "grams"):
        return quantity
    elif unit in ("tbsp", "tablespoon"):
        return quantity * 15
    elif unit in ("tsp", "teaspoon"):
        return quantity * 5
    elif unit in ("kg",):
        return quantity * 1000
    elif unit in ("l", "liters"):
        return quantity * 1000
    elif unit in ("ml", "milliliters"):
        return quantity
    elif unit in ("oz", "ounce", "ounces"):
        return quantity * 28.35
    elif unit in ("lb", "pound", "pounds"):
        return quantity * 453.59
    elif unit in ("cup", "cups"):
        return quantity * 236.59
    elif unit in ("pint",):
        return quantity * 473.18
    elif unit in ("quart",):
        return quantity * 946.35
    elif unit in ("floz",):
        return quantity * 29.57
    else:
        raise ValueError("Unknown unit: {}".format(unit))
    
def extract_number(string):
    """
    This function takes a string as input and returns a number contained within the string, if it exists.
    The number can be an integer or a float.
    """
    result = ''
    decimal_point_count = 0
    for char in string:
        if char.isdigit() or char == '.':
            if char == '.':
                decimal_point_count += 1
            if decimal_point_count > 1:
                return None
            result += char
        elif result != '':
            # print("number extracter returns: "+result)
            break
    if result:
        # print(result)
        return float(result)
    else:
        return 0