from pyscript import display
# Restaurant Order System using Python Data Types

# 1. String data type
restaurant_name = "Capuchins' Cafe"  # string
owner_name = "Railey Amante"  # string

# 2. Integer data type
year_established = 2025  # integer

# 4. Boolean data type
Dine_in_Only = True  # boolean

# 5. List data type
product_names = ["Cappucino", "Espresso", "Banana Bread"]  # list

# 6. Tuple data type
business_hours = ("6:00 AM", "11:00 PM")  # tuple

# 7. Dictionary data type
menu_prices = {  # dictionary
    "Cappucino": 150.00,
    "Espresso": 100.00,
    "Banana Bread": 75.00,
    "Fruit Salad": 150.00,
    "Omelette": 50.00,
    "Iced Tea": 20.00
}


# ------------------- DISPLAY -------------------

# Display restaurant info
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_established}", target="since")
display("Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu_prices['Cappucino']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu_prices['Espresso']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu_prices['Banana Bread']:.2f}", target="price3")
display("Fruit Salad", target="prod4")
display(f"₱{menu_prices['Fruit Salad']:.2f}", target="price4")
display("Omelette", target="prod5")
display(f"₱{menu_prices['Omelette']:.2f}", target="price5")
display("Iced Tea", target="prod6")
display(f"₱{menu_prices['Iced Tea']:.2f}", target="price6")


# Display opening hours
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")

# Display delivery availability
if Dine_in_Only:
    display("Dine-in Only", target="orderType")
else:
    display("Dine-in Only", target="orderType")

