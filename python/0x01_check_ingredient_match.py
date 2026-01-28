def check_ingredient_match(recipe, inventory):
  """Checks missing items in inventory

  Args:
    recipe: A list of recipes
    inventory: A list of inventories
    
  Returns:
    A float representing the percentage of required ingredients.
    A new list of ingredients the character is missing but that are required.
  """
  required_item = 0
  missing_ingredients = []
  for item in recipe:
      if item in inventory:
          required_item += 1
      else:
          missing_ingredients.append(item)
  percentage_required_ingredients = (required_item/len(recipe)) * 100
  return percentage_required_ingredients, missing_ingredients
