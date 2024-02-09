CREATE TABLE User(
    user_id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);
CREATE TABLE Profile(
    Profile_id INT NOT NULL AUTO_INCREMENT,     
    user_id INT NOT NULL,git a
    Bio VARCHAR(255) NOT NULL,
    ProfilePicture VARCHAR(255) NOT NULL,
      
    PRIMARY KEY (Profile_id)
);
CREATE TABLE Items(
    item_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    item_name VARCHAR(255) NOT NULL,
    item_price INT NOT NULL,
    item_description VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL,
    availability VARCHAR(255) NOT NULL,
    PRIMARY KEY (item_id),
    Foreign Key (category) references Categories(category),
    Foreign Key (user_id) references User(user_id)
);
CREATE TABLE Categories(
    category VARCHAR(255) NOT NULL,
    category_description VARCHAR(255) NOT NULL,
    PRIMARY KEY (category)
);
CREATE TABLE Orders(
    order_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    item_id INT NOT NULL,
    PRIMARY KEY (order_id),
    Foreign Key (user_id) references User(user_id)
   
);
create table orederItems(
    order_items_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    PRIMARY KEY (order_items_id),
    foreign key (order_id) references Orders(order_id),
    foreign key (item_id) references Items(item_id)
);
CREATE TABLE Reviews(
    review_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    item_id INT NOT NULL,
    review VARCHAR(255) NOT NULL,
    rating INT NOT NULL,
    date DATE NOT NULL,
    comment VARCHAR(255) NOT NULL,
    PRIMARY KEY (review_id),
    Foreign Key (user_id) references User(user_id)
);
CREATE TABLE Transactions(
    transaction_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    RentalDate DATE NOT NULL,
    ReturnDate DATE NOT NULL,
    TotalPrice INT NOT NULL,
    PRIMARY KEY (transaction_id),
    foreign key (order_id) references Orders(order_id)
);
CREATE TABLE Payment(
    payment_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    PaymentMethod VARCHAR(255) NOT NULL,
    PaymentDate DATE NOT NULL,
    PaymentAmount INT NOT NULL,
    PRIMARY KEY (payment_id),
    foreign key (order_id) references Orders(order_id)
);