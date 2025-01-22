from db.database import create_connection

def add_recipient(name, contact_info, address):
    connection = create_connection()
    cursor = connection.cursor()

    query = """INSERT INTO Recipients (recipient_name, contact_info, address)
               VALUES (%s, %s, %s)"""
    data = (name, contact_info, address)

    cursor.execute(query, data)
    connection.commit()

    cursor.close()
    connection.close()

def get_all_recipients():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Recipients")
    recipients = cursor.fetchall()

    cursor.close()
    connection.close()

    return recipients
