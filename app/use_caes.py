from django.db import transaction

from app.infrastructure import AccountRepository
from .models import *

import random
import string

def generate_account_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class CreateAccountUseCase:
    @staticmethod
    def create_account(customer_id, name, email, phone_number):
        customer = Customer.objects.create(
            id=customer_id,
            name=name,
            email=email,
            phone_number=phone_number
        )
        
        account = Account.objects.create(
            customer=customer,
            account_number=generate_account_number(),
            balance=0.0
        )
        return account
    
    @staticmethod
    def get_account(account_id):
        account = Account.objects.get(id = account_id)
        return account

class TransactionUseCase:
    @staticmethod
    def make_transaction(account_id, amount, transaction_type):
        account = AccountRepository.find_account_by_id(account_id)
        if transaction_type == 'deposit':
            account.balance = float(account.balance or 0) + amount
        elif transaction_type == 'withdraw':
            account.balance = float(account.balance or 0) - float(amount)
        account.save()
        Transaction.objects.create(
            account=account,
            transaction_type=transaction_type.capitalize(),
            amount=amount
        )

class StatementUseCase:
    @staticmethod
    def generate_account_statement(account_id):
        account = Account.objects.get(id=account_id)
        transactions = Transaction.objects.filter(account=account)
        statement = f"Account Statement for Account {account.account_number}:\n"
        for transaction in transactions:
            statement += f"{transaction.transaction_type}: {transaction.amount}\n"
        statement += f"Current Balance: {account.balance}\n"
        return statement
