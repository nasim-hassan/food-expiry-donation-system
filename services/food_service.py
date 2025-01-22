from models.food_items import add_food_item, view_food_items

def add_food(food_name, quantity, expiry_date):
    add_food_item(food_name, quantity, expiry_date)

def list_food_items():
    return view_food_items()
