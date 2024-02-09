from os import name
from django.db import models 
class Categories(models.Model):
    category = models.CharField(primary_key=True, max_length=255)
    category_description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Categories'
    def __str__(self):
        return f'{self.category}'

class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    item_price = models.IntegerField()
    item_description = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, models.DO_NOTHING, db_column='category')
    availability = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Items'
    def __str__(self):
        return f'{self.item_name}'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    item_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Orders'
    def __str__(self):
        return f'{self.order_id}'

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    paymentmethod = models.CharField(db_column='PaymentMethod', max_length=255)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate')  # Field name made lowercase.
    paymentamount = models.IntegerField(db_column='PaymentAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payment'
    def __str__(self):
        return f'{self.payment_id}'

class Profile(models.Model):
    profile_id = models.AutoField(db_column='Profile_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    bio = models.CharField(db_column='Bio', max_length=255)  # Field name made lowercase.
    profilepicture = models.CharField(db_column='ProfilePicture', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profile'
    def __str__(self):
        return f'{self.profile_id}'

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    item_id = models.IntegerField()
    review = models.CharField(max_length=255)
    rating = models.IntegerField()
    date = models.DateField()
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Reviews'
    def __str__(self):
        return f'{self.review_id}'

class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    rentaldate = models.DateField(db_column='RentalDate')  # Field name made lowercase.
    returndate = models.DateField(db_column='ReturnDate')  # Field name made lowercase.
    totalprice = models.IntegerField(db_column='TotalPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'
    def __str__(self):
        return f'{self.transaction_id}'

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
    def __str__(self):
    #return first name and last name
        return f'{self.firstname} {self.lastname}'