class UserAccounts():

    def __init__(self, id, user_id, account_number, balance, account_type, status):
        self.id = id
        self.user_id = user_id
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.status = status

    def show_balance(self):
        return self.balance

    def get_status(self):
        return self.status

    def get_account_type(self):
        return self.account_type

    def get_account_number(self):
        return self.account_number

    def get_user_id(self):
        return self.user_id

