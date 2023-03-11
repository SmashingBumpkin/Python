from django import template
register = template.Library()

@register.filter
def scaled_string_with_arg(recipe_ingredient, scale):
    return recipe_ingredient.scaled_string(scale)