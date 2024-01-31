from .models import Account

class AccountRepository:
    @staticmethod
    def save_account(account_data):
        account = Account(**account_data)
        account.save()

    @staticmethod
    def find_account_by_id(account_id):
        return Account.objects.get(id=account_id)

    @staticmethod
    def find_accounts_by_customer_id(customer_id):
        return Account.objects.get(customer_id=customer_id)
