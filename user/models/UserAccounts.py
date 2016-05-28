from user.utils import db


class UserAccounts():

    file_name = "../user_accounts.txt"

    def __init__(self, id=None, user_id=None, account_number=None, balance=None, account_type=None, status=None):
        self.id = id
        self.user_id = user_id
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.status = status

    def get(self, user_id):
        user_accounts = db.get(self.file_name)

        for account in user_accounts:
            attributes = account.split(',')

            if attributes[1] == user_id:
                return UserAccounts(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])

        return None

    def update_type(self, value):
        self.account_type = value
        self.update()

    def save(self):
        useraccounts = []
        try:
            useraccounts = db.get(self.file_name)
        except Exception as e:
            pass

        data = "%d,%s,%d,%d,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

        return self

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

        data = "%s,%s,%s,%s,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

        return self
