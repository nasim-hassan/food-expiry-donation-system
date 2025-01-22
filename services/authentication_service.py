from models.users import User
from getpass import getpass
from utils.hash_password import hash_password, verify_password

class AuthenticationService:
    def login(self):
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        # Use the class method to verify password
        user = User.verify_user_password(username, password)
        
        if user:
            print("Login successful!")
            return {"user_id": user.user_id, "username": user.username, "role": user.role}  # user_id, username, role
        
        print("Invalid credentials.")
        return None

    def register(self):
        username = input("Enter username: ")
        password = getpass("Enter password: ")
        role = input("Enter role (admin/donor): ").lower()
        
        if role not in ["admin", "donor"]:
            print("Invalid role. Registration failed.")
            return
        
        try:
            # Call the class method to register the user
            User.register_user(username, password, role, email=None, contact_info=None)
            print("Registration successful!")
        except Exception as e:
            print(f"Registration failed: {e}")
