from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    
    class Meta:
        managed = True
        db_table = 'customer'

class Account(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True)
    balance = models.FloatField(blank=True, null=True,default=None)
    
    class Meta:
        managed = True
        db_table = 'account'

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)
    amount = models.FloatField(blank=True, null=True,default=None)
    
    class Meta:
        managed = True
        db_table = 'transaction'
