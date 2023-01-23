tomatoes = {"price": 0.87, "quantity": 6}
sponges = {"price": 0.29, "quantity": 10}
juice = {"price": 1.89, "quantity": 1500}
foil = {"price": 1.29, "quantity": 30}
sugar = {"price": 1.09, "quantity": 500}
'''
quantity = 2
sponge_cost = sponges["price"] * quantity
juice_cost = juice["price"] * quantity
tomato_cost = tomatoes["price"] * quantity
cost = sponge_cost + juice_cost + tomato_cost

print("1kg of sugar costs: £", sugar["price"] * 2)
print("20 sponges, 3l of juice and 2 packs of tomatoes costs: £", cost)
'''
customers = 5
tomato_cost = tomatoes["price"]
sponge_cost = sponges["price"] / sponges["quantity"] * 3
juice_cost = juice["price"] / juice["quantity"] * 1000
foil_cost = foil["price"] / foil["quantity"] * 20
sugar_cost = sugar["price"] / sugar["quantity"] * 180
total = (tomato_cost + sponge_cost + juice_cost + foil_cost + sugar_cost) * customers
#print("Total for 5 customers :£", total)
vat = total / 20
#print("Plus VAT :£", round(total + vat, 2))

recipe_book = {"Name": "Roasted Gnocchi", 
               "Servings": 3, 
               "Ingredients": {"Bell pepper": 600, 
                               "Gnocchi": 500, 
                                "Meatballs": 300, 
                                "Tomato": 300, 
                                "Soft Cheese": 60, 
                                "Parsley": 30, 
                                "Garlic": 2, 
                                "Nutritional yeast": "3tbsp", 
                                "Rosemary": "2tbsp", 
                                "Salt": "1tsp", 
                                "Black pepper": "0.5tsp", 
                                "Chili": 0.75}}

def price_per_gram(price, quantity):
    total = price / quantity
    return f"{total}g"

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

print(bell_pepper, garlic, chili)

# TO DO
# Use a data class
# Put recipes in a separate file and read it in
# Allow user to enter their own recipes
# Function that suggests ingredient swaps to reduce recipe price
# Ingredient price changes with the season (4 prices per item?)