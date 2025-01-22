from services.donation_service import donate_food, view_user_donations
from services.food_service import add_food_item, view_food_items
from services.authentication_service import AuthenticationService
from models.expired_food_removal import remove_expired_food
from models.users import User

def main_menu():
    while True:
        print("\nFood Expiry and Donation Management System")
        print("1. Register User")
        print("2. Donate Food")
        print("3. View Donations")
        print("4. View Food Items")
        print("5. Remove Expired Food Items")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role (admin/donor): ")
            email = input("Enter email: ")
            contact_info = input("Enter contact info: ")
            User.register_user(username, password, role, email, contact_info)
            print("User registered successfully!")
        elif choice == "2":
            donor_id = int(input("Enter your user ID: "))
            food_id = int(input("Enter food ID: "))
            quantity = int(input("Enter quantity to donate: "))
            donate_food(donor_id, food_id, quantity)
            print("Donation made successfully!")
        elif choice == "3":
            donor_id = int(input("Enter your user ID to view donations: "))
            donations = view_user_donations(donor_id)
            for donation in donations:
                print(donation)
        elif choice == "4":
            food_items = view_food_items()
            for item in food_items:
                print(item)
        elif choice == "5":
            remove_expired_food()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
