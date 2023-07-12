# Calculates the price of each ingredient per gram
def price_per_gram(price, quantity):
    total = price / quantity
    return f"{round(total, 2)}g"

# Asks how much of an ingredient the user has and updates the quantity in the pantry
def quantity_check(ingredient):

    '''Asks how much of an ingredient the user has
    Asks the user for input
    Changes the quantity in the pantry'''

    ingredient_name = ingredient["Name"]
    quantity = input(f"How much of {ingredient_name} have you got?")
    bell_pepper["Quantity"] = quantity

    return None

bell_pepper = {"Name": "Bell Pepper", "Price": 1.35, "Quantity": 900, "In Stock": False}
gnocchi = {"Name": "Gnocchi", "Price": 2.00, "Quantity": 900, "In Stock": False}
meatballs = {"Name": "Meatballs", "Price": 1.75, "Quantity": 300, "In Stock": False}
#bell_pepper = price_per_gram(1.35, 600)
#gnocchi =  price_per_gram(2.00, 500)
#meatballs = price_per_gram(1.75, 300)
tomato = price_per_gram(0.32, 400)
soft_cheese = price_per_gram(3.00, 130)
parsley = price_per_gram(0.55, 30)
garlic = price_per_gram(1.25, 300)
nutritional_yeast = price_per_gram(3.00, 100)
rosemary = price_per_gram(0.60, 27)
salt = price_per_gram(1.25, 350)
black_pepper = price_per_gram(0.90, 25)
chili = price_per_gram(0.70, 32)
pantry = [bell_pepper, gnocchi, meatballs]

recipe_book = {"Name": "Roasted Gnocchi", 
               "Servings": 3, 
               "Ingredients": {"Bell pepper": 600, 
                               "Gnocchi": 500, 
                                "Meatballs": 300, 
                                "Tomato": 300, 
                                "Soft Cheese": 60, 
                                "Parsley": 30, 
                                "Garlic": 2, 
                                "Nutritional yeast": f"{3}tbsp", 
                                "Rosemary": f"{2}tbsp", 
                                "Salt": f"{1}tsp", 
                                "Black pepper": f"{0.5}tsp", 
                                "Chili": f"{0.75}tsp"}}

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


def compare_pantry_to_recipe(recipe):
    for i in recipe.get("Ingredients"):
        print(i)
        for j in pantry:
            pass
                #if i >= j:
                #    i["In Stock"] = True
                #else:
                #    i["In Stock"] = False
    #print(i)
    #print(j)


 

compare_pantry_to_recipe(recipe_book)
## TO DO ##
# Use a data class
# Ingredients inherit from a class?
# Put recipes in a separate file and read it in
# Use Pandas to store recipes

# Allow user to enter their own recipes
# Allows user to enter their shopping
# Asks the user how much of an ingredient they have in order to fulfill the top 3 recipes

# Function that suggests ingredient swaps to reduce recipe price
# Ingredient price changes with the season (4 prices per item?)
# Takes the users climate zone into account