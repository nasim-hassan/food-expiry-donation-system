from db.database import create_connection
from datetime import datetime

# Function to remove expired food items
def remove_expired_food():
    conn = create_connection()
    cursor = conn.cursor()

    # Get today's date
    today_date = datetime.today().date()

    # Find expired food items
    cursor.execute("""
        SELECT food_id, food_name, expiry_date
        FROM FoodItems
        WHERE expiry_date < %s;
    """, (today_date,))

    expired_foods = cursor.fetchall()

    if expired_foods:
        print(f"Found {len(expired_foods)} expired food items. Removing them...")
        # For each expired food, delete it from the FoodItems table
        for food in expired_foods:
            food_id = food[0]
            food_name = food[1]
            expiry_date = food[2]

            # Log the removal of the expired food
            cursor.execute("""
                INSERT INTO ExpiredFoodRemoval (food_id, expiry_date)
                VALUES (%s, %s);
            """, (food_id, expiry_date))

            # Delete expired food from FoodItems table
            cursor.execute("""
                DELETE FROM FoodItems
                WHERE food_id = %s;
            """, (food_id,))
            print(f"Expired food item '{food_name}' (ID: {food_id}, Expiry Date: {expiry_date}) removed.")

        # Commit changes to the database
        conn.commit()
    else:
        print("No expired food items found.")

    cursor.close()
    conn.close()
