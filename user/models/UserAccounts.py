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

    def _get(self, key, value):
        user_accounts = db.get(self.file_name)

        for account in user_accounts:
            attributes = account.split(',')

            if str(attributes[key]) == str(value):
                return UserAccounts(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])

        return None

    def get(self, user_id):
        return self._get(1, user_id)

    def get_by_aacount(self, acc_no):
        return self._get(2, acc_no)

    def update_type(self, value):
        self.account_type = value
        self.update()

    def save(self):
        useraccounts = []
        try:
            useraccounts = db.get(self.file_name)
        except Exception as e:
            pass

        data = "%s,%s,%s,%s,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

        return self

    def update(self):
        useraccounts = []
        try:
            useraccounts = db.get(self.file_name)
        except Exception as e:
            pass
        import pdb;
        pdb.set_trace()
        for index, user in enumerate(useraccounts):
            attributes = user.split(",")
            if self.id == attributes[0]:
                useraccounts.pop(index)

        data = "%s,%s,%s,%s,%s,%s" % (self.id, self.user_id, self.account_number, self.balance, self.account_type, self.status)
        useraccounts.append(data)
        db.save(self.file_name, useraccounts)

        return self
