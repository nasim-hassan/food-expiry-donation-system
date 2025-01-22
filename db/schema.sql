CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,  -- Store hashed passwords for security
    role ENUM('admin', 'donor') NOT NULL,  -- Only admin and donor roles
    email VARCHAR(255),
    contact_info VARCHAR(255),
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE FoodItems (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,  -- Quantity available for donation
    expiry_date DATE,  -- Expiry date for each food item
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp when food was received
);


CREATE TABLE Donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT NOT NULL,  -- Foreign key linking to Users (Donor)
    food_id INT NOT NULL,  -- Foreign key linking to FoodItems
    quantity_donated INT NOT NULL,  -- Quantity of food donated
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donor_id) REFERENCES Users(user_id)
        ON DELETE CASCADE,
    FOREIGN KEY (food_id) REFERENCES FoodItems(food_id)
        ON DELETE CASCADE
);


CREATE TABLE Recipients (
    recipient_id INT AUTO_INCREMENT PRIMARY KEY,
    recipient_name VARCHAR(255) NOT NULL,
    contact_info VARCHAR(255),
    address VARCHAR(255)
);


CREATE TABLE Distributions (
    distribution_id INT AUTO_INCREMENT PRIMARY KEY,
    donation_id INT NOT NULL,  -- Link to donation
    recipient_id INT NOT NULL,  -- Link to recipient (optional)
    quantity_distributed INT NOT NULL,  -- Quantity distributed
    distributed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donation_id) REFERENCES Donations(donation_id)
        ON DELETE CASCADE,
    FOREIGN KEY (recipient_id) REFERENCES Recipients(recipient_id)
        ON DELETE CASCADE
);


CREATE TABLE ExpiredFoodRemoval (
    removal_id INT AUTO_INCREMENT PRIMARY KEY,
    food_id INT NOT NULL,  -- Foreign key linking to FoodItems
    expiry_date DATE NOT NULL,
    removed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (food_id) REFERENCES FoodItems(food_id)
        ON DELETE CASCADE
);
