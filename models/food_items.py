from db.database import create_connection

def add_food_item(food_name, quantity, expiry_date):
    connection = create_connection()
    cursor = connection.cursor()

    query = """INSERT INTO FoodItems (food_name, quantity, expiry_date)
               VALUES (%s, %s, %s)"""
    data = (food_name, quantity, expiry_date)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()

def view_food_items():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM FoodItems")
    food_items = cursor.fetchall()

    cursor.close()
    connection.close()

    return food_items
