from db.database import create_connection

def distribute_food(donation_id, recipient_id, quantity):
    connection = create_connection()
    cursor = connection.cursor()

    query = """INSERT INTO Distributions (donation_id, recipient_id, quantity_distributed)
               VALUES (%s, %s, %s)"""
    data = (donation_id, recipient_id, quantity)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()
