from models.donations import add_donation, get_donations_by_user

def donate_food(donor_id, food_id, quantity):
    add_donation(donor_id, food_id, quantity)

def view_user_donations(donor_id):
    return get_donations_by_user(donor_id)
