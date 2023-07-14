# Calculates the price of each ingredient per gram
def price_per_gram(price, quantity):
    total = price / quantity
    return f"{round(total, 2)}g"

# Updates the quantity of a specific ingredient in the pantry
def quantity_check(pantry, ingredient):

    """
    Updates the quantity of a specific ingredient in the pantry.

    Args:
        pantry (list): A list of dictionaries representing the items available in the pantry.
        ingredient (dict): A dictionary representing the ingredient with its name, price, quantity, and stock status.

    Returns:
        None
    """

    ingredient_name = ingredient["Name"]
    quantity = input(f"How many grams of {ingredient_name} do you have?")

    for item in pantry:
        if item["Name"] == ingredient_name:
            item["Quantity"] = int(quantity)
            break

    return None

# Compares the availability of ingredients in the pantry to the amount needed in a recipe
def compare_pantry_to_recipe(pantry, recipe):

    """
    Compares the availability of ingredients in the pantry to the amount needed in a recipe.

    Args:
        pantry (list): A list of dictionaries representing the items available in the pantry.
        recipe (dict): A dictionary representing the recipe with its name, servings, and ingredients.

    Returns:
        list: A list containing a dictionary with the recipe name as the key and the ingredient comparison as the value.

    """

    ingredient_comparison = {}

    for ingredient, amount_needed in recipe["Ingredients"].items():
        for item in pantry:
            if item["Name"] == ingredient:
                ingredient_comparison[ingredient] = "In Stock"
                if item["Quantity"] < amount_needed:
                    ingredient_comparison[ingredient] = "Not Enough"
                break
            else:
                ingredient_comparison[ingredient] = "Not In Stock"

    return [{recipe["Name"]: ingredient_comparison}]

pantry = [
    {"Name": "Gnocchi", "Price": 2.00, "Quantity": 900, "In Stock": False},
    {"Name": "Udon Noodles", "Price": 2.00, "Quantity": 900, "In Stock": False},
    {"Name": "Meatballs", "Price": 1.75, "Quantity": 300, "In Stock": False},
    {"Name": "Bell Pepper", "Price": 1.35, "Quantity": 900, "In Stock": False},
    {"Name": "Mushroom", "Price": 1.35, "Quantity": 900, "In Stock": False},
    {"Name": "Tomato", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Scallions", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Edamame", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Cream Cheese", "Price": 3.00, "Quantity": 130, "In Stock": False},
    {"Name": "Butter", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Soy Sauce", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Parsley", "Price": 0.55, "Quantity": 30, "In Stock": False},
    {"Name": "Garlic", "Price": 1.25, "Quantity": 300, "In Stock": False},
    {"Name": "Rosemary", "Price": 0.60, "Quantity": 27, "In Stock": False},
    {"Name": "Salt", "Price": 1.25, "Quantity": 350, "In Stock": False},
    {"Name": "Black Pepper", "Price": 0.90, "Quantity": 25, "In Stock": False},
    {"Name": "Garlic Powder", "Price": 0.32, "Quantity": 400, "In Stock": False},
    {"Name": "Chili", "Price": 0.70, "Quantity": 32, "In Stock": False},
    {"Name": "Nutritional Yeast", "Price": 3.00, "Quantity": 100, "In Stock": False}
]

# Everything is in grams
recipe_book = [
    {
        "Name": "Roasted Gnocchi",
        "Servings": 3,
        "Ingredients": {
            "Bell pepper": 600,
            "Gnocchi": 500,
            "Meatballs": 300,
            "Tomato": 300,
            "Soft Cheese": 60,
            "Parsley": 30,
            "Garlic": 2,
            "Nutritional yeast": 15,
            "Rosemary": 10,
            "Salt": 5,
            "Black pepper": 7,
            "Chili": 3
        }
    },
    {
        "Name": "Shoyu Butter Udon Noodles",
        "Servings": 2,
        "Ingredients": {
            "Udon Noodles": 400,
            "Mushrooms": 200,
            "Edamame": 100,
            "Butter": 30,
            "Scallions": 20,
            "Soy Sauce": 15,
            "Garlic Powder": 3
        }
    }
]

# CURRENTLY WORKING ON THIS
# Need to remove the g
def price_per_quantity(quantity, price):
    total = quantity * price
    total = round(total, 2)
    #return f"£{total}"
    return total

def recipe_check(recipe):

    for i in recipe["Ingredients"]:
        ingredient = recipe["Ingredients"][i]
        print(ingredient)
        for j in pantry["Names"]:
            #index = pantry.index
        #quantity_check(i)
            pass
    return None

## TO DO ##
# Use a data class
# Ingredients inherit from a class?
# Put recipes in a separate file and read it in
# Use Pandas to store recipes

# Allow user to enter their own recipes
# Allows user to enter their shopping
# Asks the user how much of an ingredient they have in order to fulfill the top 3 recipes
# Suggests a list of the top 3 most common ingredients needed (based on ingredieant frequency) 

# Function that suggests ingredient swaps to reduce recipe price
# Ingredient price changes with the season (4 prices per item?)
# Takes the users climate zone into account