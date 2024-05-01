import pandas as pd # Modifying the recipe book
import tkinter as tk # User interface
import os # Creating the recipe book
#import ast # Accessing the pantry as a dictionary
import csv # For recipe book and pantry
import datetime # For finding seasonal ingredients/recipes

## PANTRY ###


pantry_data = [
    {"Name": "Gnocchi", "Price Per G": 0.04, "Quantity": 100, "In Stock": False},
    {"Name": "Udon Noodles", "Price Per G": 0.03, "Quantity": 900, "In Stock": False},
    {"Name": "Meatballs", "Price Per G": 0.02, "Quantity": 300, "In Stock": False},
    {"Name": "Bell Pepper", "Price Per G": 0.03, "Quantity": 900, "In Stock": False},
    {"Name": "Mushroom", "Price Per G": 0.04, "Quantity": 900, "In Stock": False},
    {"Name": "Tomato", "Price Per G": 0.2, "Quantity": 400, "In Stock": False},
    {"Name": "Scallions", "Price Per G": 0.02, "Quantity": 400, "In Stock": False},
    {"Name": "Edamame", "Price Per G": 0.02, "Quantity": 400, "In Stock": False},
    {"Name": "Cream Cheese", "Price Per G": 0.07, "Quantity": 130, "In Stock": False},
    {"Name": "Butter", "Price Per G": 0.05, "Quantity": 400, "In Stock": False},
    {"Name": "Soy Sauce", "Price Per G": 0.02, "Quantity": 400, "In Stock": False},
    {"Name": "Parsley", "Price Per G": 0.05, "Quantity": 30, "In Stock": False},
    {"Name": "Garlic", "Price Per G": 0.02, "Quantity": 300, "In Stock": False},
    {"Name": "Rosemary", "Price Per G": 0.04, "Quantity": 27, "In Stock": False},
    {"Name": "Salt", "Price Per G": 0.05, "Quantity": 350, "In Stock": False},
    {"Name": "Black Pepper", "Price Per G": 0.05, "Quantity": 25, "In Stock": False},
    {"Name": "Garlic Powder", "Price Per G": 0.01, "Quantity": 400, "In Stock": False},
    {"Name": "Chili", "Price Per G": 0.01, "Quantity": 32, "In Stock": False},
    {"Name": "Nutritional Yeast", "Price Per G": 0.03, "Quantity": 100, "In Stock": False},  
    {"Name": "Apple", "Season": ["January", "Febuary", "September", "October", "November", "December"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Apricot", "Season": ["May"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Bilberry", "Season": ["June", "July", "August", "September", "October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Blackberry", "Season": ["August", "September", "October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Blackcurrant", "Season": ["June", "July"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Blueberry", "Season": ["June", "July", "August"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Bramley Apple", "Season": ["March"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Cherry", "Season": ["June", "July", "August"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Crab Apple", "Season": ["August"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Cranberry", "Season": ["October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Elderberry", "Season": ["August", "September", "October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Gooseberry", "Season": ["June", "July", "August", "September"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Grapefruit", "Season": ["May"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Greengage", "Season": ["June", "July", "August"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Loganberry", "Season": ["August"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Medlar", "Season": ["September", "October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Nectarine", "Season": ["May"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Pear", "Season": ["January", "September", "October", "November", "December"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Plum", "Season": ["August", "September", "October"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Pomegranate", "Season": ["May", "November"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Quince", "Season": ["October", "November"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Raspberry", "Season": ["July", "August", "September"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Redcurrent", "Season": ["July", "August", "September"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Strawberry", "Season": ["June", "July", "August", "September"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False},
    {"Name": "Watermelon", "Season": ["July", "August", "September"], "Price Per G": 0.0, "Quantity": 0, "In Stock": False}]

def build_pantry(recipe_book) -> pd.DataFrame:

    # Using a set to avoid duplicates
    unique_ingredients = recipe_book['Ingredients'].apply(lambda x: list(x.keys()) if isinstance(x, dict) else []).explode().unique()

    # Create Pantry DataFrame
    pantry = pd.DataFrame({'Ingredient': list(unique_ingredients)})
    # Set index
    pantry.reset_index(drop=True, inplace=True)
    # Name the DataFrame
    pantry.name = 'Pantry'

    return pantry

def load_pantry(file_path) -> pd.DataFrame:
    
    pantry = pd.read_csv(file_path)

    return pantry

def save_pantry(pantry, file_path) -> None:
    
    pantry.to_csv(file_path, index=False)

    return None

def modify_pantry(file_path) -> pd.DataFrame:
    
    # Check if the file exists and isnt empty
    # If it does exist it loads it
    if os.path.exists(file_path):
        pantry = load_pantry(file_path)
    else:
        # If the file doesnt exist, create it
        pantry = build_pantry(recipe_book)

    new_ingredient = [
    {'Ingredient': "Apple",
     'Tags': ['Fruit'],
     'Quantity': 5,
     'Price': 1.00,
     'Season': "January, Febuary, September, October, November, December"
     }]

    # Append the new ingredient
    pantry = pantry._append(new_ingredient, ignore_index=True)

    # Save the pantry
    save_pantry(pantry, file_path)

    return pantry


####
## RECIPE BOOK ##

# A list of dictionaries | 1 dictionary per recipe
recipe_data = [
    {'Name': "Mango Peach Green Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 3,
     'Ingredients': {'Mango': 1, 'Banana': 2, 'Peach': '250g', 'Kale': '25g', 'Soy Milk': '480ml', 'Flax Seeds': '1 tsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},
    
    {'Name': "Blueberry and Vanilla Smoothie",
     'Tags': ['', '', ''],
     'Servings': 1,
     'Ingredients': {'Blueberries': '75g', 'Banana': 1, 'Soy Milk': '240ml', 'Almond Butter': '1 tbsp', 'Vanilla Extract': '1/2 tsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},
    
    {'Name': "Peanut Butter and Banana Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 1,
     'Ingredients': {'Spinach': '15g', 'Banana': 1, 'Soy Milk': '180ml', 'Peanut Butter': '1 tbsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},
    
    {'Name': "Orange Creamsicle Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 1,
     'Ingredients': {'Orange': 1, 'Banana': 1, 'Soy Milk': '180ml', 'Almond Butter': '1 tbsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},
    
    {'Name': "Ruby Red Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 4,
     'Ingredients': {'Spinach': '60g', 'Beetroot (small)': 2, 'Orange': 2, 'Banana': 3, 'Soy Milk': '480ml', 'Hemp Seeds': '2 tbsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},
    
    {'Name': "Cold Busting Green Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 2,
     'Ingredients': {'Spinach': '15g', 'Cucumber': '1/4', 'Orange': 1, 'Banana': 1, 'Apple': 2, 'Parsley (fresh)': '4 tbsp', 'Soy Milk': '240ml', 'Ginger': '1 tbsp', 'Chia Seeds': '1.5 tsp'},
     'Instructions': ",1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},

    {'Name': "Chocolate Hazelnut Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 2,
     'Ingredients': {'Cinnoman': '1/8 tsp', 'Vanilla Extract': '1/8 tsp', 'Cocoa Powder': '1 tbsp', 'Banana': 1, 'Dates': 2, 'Hazelnut Butter': '1 tbsp', 'Soy Milk': '180ml', 'Salt': '1 pinch'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},

    {'Name': "Strawberry, Pineapple and Mint Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 2,
     'Ingredients': {'Strawberries': '150g', 'Pineapple': '150g', 'Cucumber': '1/4', 'Orange': 1, 'Mint Leaves': 6, 'Coconut Water': '240ml'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},

    {'Name': "Peanut Butter Jelly Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 1,
     'Ingredients': {'Strawberries': '113g', 'Banana': 1, 'Peanut Butter': '1.5 tbsp', 'Soy Milk': '180ml'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},

    {'Name': "Blueberry Anti-Inflammatory Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 2,
     'Ingredients': {'Blueberries': '120g', 'Apple': 1, 'Ginger': '1 tbsp', 'Goji Berries': '2 tbsp', 'Nettle Leaf Powder': '1 tsp', 'Beetroot': 1, 'Flax Seeds': '2 tbsp', 'Pumpkin Seeds': '1 tbsp', 'Coconut Water': '360ml'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"},

    {'Name': "",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 0,
     'Ingredients': {'Item1': 0},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"}]

def build_recipe_book() -> pd.DataFrame:

    # Create recipe book
    recipe_book = pd.DataFrame(recipe_data)
    # Set index
    recipe_book.reset_index(drop=True, inplace=True)
    # Name the DataFrame
    recipe_book.name = 'Recipe Book'

    #print("Built recipe book: ", recipe_book)

    return recipe_book

def load_recipe_book(file_path) -> pd.DataFrame:

    recipe_book = pd.read_csv(file_path)

    #print("Loaded recipe book: ", recipe_book)

    return recipe_book

def save_recipe_book(recipe_book, file_path) -> None:

    recipe_book.to_csv(file_path, index=False)
    #print("Saved recipe book: ", recipe_book)

    return None

def modify_recipe_book(file_path) -> pd.DataFrame:
    
    # Check if the file exists and isnt empty
    # If it does exist it loads it
    if os.path.exists(file_path):
        recipe_book = load_recipe_book(file_path)
    else:
        # If the file doesnt exist, create it
        recipe_book = build_recipe_book()

    new_recipe = [
    {'Name': "Peanut Butter and Banana Smoothie",
     'Tags': ['Smoothie', 'Drink', 'Blender'],
     'Servings': 1,
     'Ingredients': {'Spinach': '15g', 'Banana': 1, 'Soy Milk': '180ml', 'Peanut Butter': '1 tbsp'},
     'Instructions': "1. Add all ingredients to a blender 2.Blend until smooth 3. Drink in a tall glass or add to a bowl with toppings"
     }]

    # Append the new recipe
    recipe_book = recipe_book._append(new_recipe, ignore_index=True)
    #print("Modified recipe book: ", recipe_book)
    # Save the recipe book
    save_recipe_book(recipe_book, file_path)

    return recipe_book

def recipe_exists(recipe_book, recipe_name) -> bool:

    return recipe_name in recipe_book['Name'].values

def add_recipe_to_book(recipe_book, new_recipe) -> pd.DataFrame:

    # Check if a recipe with the same name already exists
    new_recipe_name = new_recipe[0]['Name']

    if recipe_exists(recipe_book, new_recipe_name):
        print(f"Recipe '{new_recipe_name} is a duplicate so will not be added.")
    else:
        # Set new recipe as a row in the recipe book DataFrame
        recipe_book = recipe_book._append(new_recipe, ignore_index=True)
        print(f"Recipe '{new_recipe_name}' has been added.")

    return recipe_book

#####

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

# CURRENTLY WORKING ON THIS
# Calculates the price per gram based on the total price and quantity
def price_per_gram(item):
    
    price = item["Price Per G"]
    quantity = item["Quantity"]

    total = quantity / price

    return f"£{round(total, 2)}"

def recipe_check(recipe):

    for i in recipe["Ingredients"]:
        ingredient = recipe["Ingredients"][i]
        print(ingredient)
        for j in pantry["Names"]:
            #index = pantry.index
        #quantity_check(i)
            pass
    return None

# Catagorize recipes based on ingredient seasonality
def catagorize_recipies_by_season(recipe_book):
    current_month = datetime.dattime.now().strftime("%B")
    seasonal_recipes = []
    seasonal_ingredients = {pantry}

    for recipe in recipe_book:
        is_seasonal = False

        for ingredient, availability in recipe["Ingredients"].items():
            if current_month in seasonal_ingredients.get(ingredient, []):
                is_seasonal=True
                break


'''
def calculate_recipe_season(recipe_book, ingredient_seasons) -> None:

    for recipe in recipe_book:
        #recipe = ast.literal_eval(recipe)
        recipe_ingredients = recipe['Ingredients']
        common_seasons = None

        for ingredient in recipe_ingredients:
            ingredient_months = set(ingredient_seasons.get(ingredient, []))

            if common_seasons is None:
                # For the first ingredient, initialize common_seasons
                ingredient_season = ingredient_months.copy()
            else:
                # Find common seasons between all ingredients
                common_seasons = common_seasons.intersection(ingredient_months)

        # Update recipe with seasonal information
        recipe["Seasonality"] = list(common_seasons)

    for recipe in recipe_book:
        print(f"Recipie: {recipe['Name']}")
        if recipe["Seasonality"]:
            print(f"Best Months: {', '.join(map(str, recipe['Seasonality']))}")
        else:
            print("No specific season")
        print()

    return
'''
recipe_book = build_recipe_book()
recipe_book = modify_recipe_book('recipe_book.csv') # Modifies and saves
#recipe_book = load_recipe_book('recipe_book.csv')
pantry = build_pantry(recipe_book)
modify_pantry('pantry.csv') # Modifies and saves

#calculate_recipe_season(recipe_book, pantry)




## UI ##



'''def update_seasonal_ingredients() -> None:

    current_month = month_var.get()
    seasonal_list.delete(0, tk.END) # Clear the list

    for ingredient in pantry:
        if current_month in ingredient.get("Season", []):
            seasonal_list.insert(tk.END, f"{ingredient['Name']} is in season")

    return
'''
# Create main window
app = tk.Tk()
app.title("Seasonal Ingredients")

# Label and Dropdown for selecting the month
month_label = tk.Label(app, text="Select a Month:")
month_label.pack()

months = ["January", "February", "March",
          "April", "May", "June",
          "July", "August", "September",
          "October", "November", "December"]

month_var = tk.StringVar()
month_dropdown = tk.OptionMenu(app, month_var, *months)
month_dropdown.pack()

# Button to update the list of seasonal ingredients
update_button = tk.Button(app, text="Update Seasonal Ingredients", command=update_seasonal_ingredients)
update_button.pack()

# Listbox to display seasonal ingredients
seasonal_list = tk.Listbox(app)
seasonal_list.pack()

# Start the Tkinter main loop
app.mainloop()



## APP NAMES ##
# Kitchen Wizard
# SpoonSavvy
# SpoonSage
# FlavorFriend
# NomNom

## TO DO ##
# Use a data class
# Ingredients inherit from a class?
# Put recipes in a separate file and read it in
# Use Pandas to store recipes

# Asks the user how much of an ingredient they have in order to fulfill the top 3 recipes
# Suggests a list of the top 3 most common ingredients needed (based on ingredieant frequency) 

# Function that suggests ingredient swaps to reduce recipe price
# Ingredient price changes with the season (4 prices per item?)

## Blog ##
# How to meal prep smoothies

## Functionality ##
# Ability to swap ingredients
# Arrange ingredients by catagory (f+v, dairy, herbs+spices)
# Arrange ingredients by quantity
# Arrange ingredients by price
# Change number of servings, ingrediants change accordingly

## Ingredients ##
# Recipies contain ingredients rather than manually written in
# Each recipe has a price
# Each ingredient has nutritional info
# Each ingredient has season availability per climate zone
# Seasonal availability is web scraped

## Meal Prep ##
# Automatic timer
# Combines recipe instructions for quicker prep
# Each step is timed
# Asks user to time themself during specific tasks for improved timing

## Pantry ##
# Allows user to enter their shopping
# Allows user to enter ingredient prices
# Ingredients have a season/month
# Display pantry in UI

## Profile ##
# Ability to set the number of fruit/veg per day
# Ability to set macros
# Takes the users climate zone into account

## Recipe Book ##
# Recipes are catagorised by season/month based on inredient seasonality
# Nutritional Info
# Difficulty
# Number of fruit/veg
# Allow user to enter their own recipes
# Does not allow for duplicate recipes
# Recipies that are very simmilar should be merged
# Ingredients from merged recipies should be listed as optional or swaps
# Display the recipe book
# Allow for user to input new recipes within the UI


## Zero Waste ##
# Use leaves (carrot tops) in smoothies
# Use vegetable peel as salad topping