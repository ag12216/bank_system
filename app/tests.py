from django.test import TestCase
from app.use_caes import CreateAccountUseCase, TransactionUseCase, StatementUseCase
from .infrastructure import AccountRepository

class BankingSystemTestCase(TestCase):
    def test_banking_system(self):
        # Create a new account
        customer_id = 1
        name = "Python"
        email = "python@tech.com"
        phone_number = "1234567890"
        account = CreateAccountUseCase.create_account(customer_id, name, email, phone_number)
        
        # Make a deposit
        amount = 100.0
        TransactionUseCase.make_transaction(account.id, amount, 'deposit')
        
        # Make a withdrawal
        amount = 50.0
        TransactionUseCase.make_transaction(account.id, amount, 'withdraw')
        
        account = AccountRepository.find_account_by_id(account.id)
        # Generate account statement
        statement = StatementUseCase.generate_account_statement(account.id)
        customer_account = AccountRepository.find_accounts_by_customer_id(account.customer_id)
        print('##############################################')
        print(f"Customer Name: {customer_account.customer.name}")
        print(f'Account No {customer_account.account_number}')
        print('##############################################')
        print(f'{statement}')
        print('##############################################')
        
        # Ensure the balance and statement are as expected
        self.assertEqual(float(account.balance), 50.0)
        self.assertIn("Deposit: 100.0", statement)
        self.assertIn("Withdraw: 50.0", statement)
