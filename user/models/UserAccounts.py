from user.utils import db


class UserAccounts():

    file_name = "useraccount.txt"

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

    def save(self):
        useraccounts = []
        try:
            useraccounts = db.get(self.file_name)
        except Exception as e:
            pass

        data = "%d,%s,%d,%d,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

    def update(self):
        useraccounts = []
        try:
            useraccounts = db.read(self.file_name)
        except Exception as e:
            pass

        for index, user in useraccounts:
            attributes = user.split(",")
            if self.id == attributes[0]:
                useraccounts.pop(index)

        data = "%d,%s,%d,%d,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

