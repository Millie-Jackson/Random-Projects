# Calculates the price of each ingredient per gram
def price_per_gram(price, quantity):
    total = price / quantity
    return f"{round(total, 2)}g"

bell_pepper = price_per_gram(1.35, 600)
gnocchi =  price_per_gram(2.00, 500)
meatballs = price_per_gram(1.75, 300)
tomato = price_per_gram(0.32, 400)
soft_cheese = price_per_gram(3.00, 130)
parsley = price_per_gram(0.55, 30)
garlic = price_per_gram(1.25, 300)
nutritional_yeast = price_per_gram(3.00, 100)
rosemary = price_per_gram(0.60, 27)
salt = price_per_gram(1.25, 350)
black_pepper = price_per_gram(0.90, 25)
chili = price_per_gram(0.70, 32)

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

# CURRENTLY WORKING ON THISE
# Need to remove the g
def price_per_quantity(quantity, price):
    total = quantity * price
    total = round(total, 2)
    #return f"£{total}"
    return total


#print(price_per_quantity(600, bell_pepper))
print(bell_pepper)
#price_per_quantity(600, bell_pepper)

# TO DO
# Use a data class
# Put recipes in a separate file and read it in
# Allow user to enter their own recipes
# Function that suggests ingredient swaps to reduce recipe price
# Ingredient price changes with the season (4 prices per item?)