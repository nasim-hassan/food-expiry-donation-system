from db.database import create_connection

def add_donation(donor_id, food_id, quantity_donated):
    connection = create_connection()
    cursor = connection.cursor()

    query = """INSERT INTO Donations (donor_id, food_id, quantity_donated)
               VALUES (%s, %s, %s)"""
    data = (donor_id, food_id, quantity_donated)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()

def get_donations_by_user(donor_id):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Donations WHERE donor_id = %s", (donor_id,))
    donations = cursor.fetchall()

    cursor.close()
    connection.close()

    return donations
