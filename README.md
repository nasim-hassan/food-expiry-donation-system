# Food Expiry and Donation Management System (FEDMS)

## Purpose
The system is designed to manage food donations, track expiry dates, and distribute food to recipients in Dhaka, Bangladesh. It aims to reduce food waste and alleviate food insecurity by facilitating food donations.

## Features
- **User Management**: Admin and donor roles.
- **Food Management**: Add food items, view food inventory.
- **Donation Management**: Track food donations and their quantities.
- **Recipient Management**: Manage recipients who receive the donations.
- **Food Distribution**: Distribute donated food to recipients.
- **Expired Food Removal**: Automatically track and remove expired food.

## How to Run
1. **Install MySQL**:
   - Set up MySQL on your system and create the `fedms` database using `schema.sql`.

2. **Set Up Python**:
   - Install Python 3.x if not already installed.
   - Install the necessary dependencies:
     ```bash
     pip install mysql-connector-python
     ```

3. **Run the Project**:
   - Execute `main.py` to launch the system.

```bash
python main.py
