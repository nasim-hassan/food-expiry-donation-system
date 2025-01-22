from db.database import create_connection
from utils.hash_password import hash_password, verify_password  # Make sure to import verify_password

class User:
    def __init__(self, user_id, username, password, role, email=None, contact_info=None, registered_at=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.email = email
        self.contact_info = contact_info
        self.registered_at = registered_at

    def __repr__(self):
        return f"User(user_id={self.user_id}, username='{self.username}', role='{self.role}')"

    @classmethod
    def from_db(cls, data):
        """Create a User instance from database row data"""
        return cls(
            user_id=data[0],
            username=data[1],
            password=data[2],
            role=data[3],
            email=data[4],
            contact_info=data[5],
            registered_at=data[6]
        )

    @classmethod
    def get_user_by_username(cls, username):
        """Fetch user by username from the database"""
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Users WHERE username = %s", (username,))
        user_data = cursor.fetchone()

        cursor.close()
        connection.close()

        if user_data:
            return cls.from_db(user_data)
        return None

    @classmethod
    def register_user(cls, username, password, role, email, contact_info):
        """Register a new user in the database"""
        connection = create_connection()
        cursor = connection.cursor()

        hashed_password = hash_password(password)  # Hash the password before storing it
        query = """INSERT INTO Users (username, password, role, email, contact_info)
                   VALUES (%s, %s, %s, %s, %s)"""
        data = (username, hashed_password, role, email, contact_info)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

    @classmethod
    def verify_user_password(cls, username, password):
        """Verify user password"""
        user = cls.get_user_by_username(username)
        if user and verify_password(user.password, password):
            return user
        return None
