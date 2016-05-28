from user.utils import db


class Transactions:

    file_name = "../transaction.txt"

    def __init__(self, id, account_number, amount, account_type, transaction_type, date, balance):
        self.id = id
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date

    def save(self):
        transactions= []
        try:
            transactions= db.get(self.file_name)
        except Exception as e:
            pass

        data = "%s,%s,%s,%s,%s,%s,%s" % (self.id, self.account_number, self.amount, self.account_type, self.transaction_type, self.date, self.balance)
        transactions.append(data)
        db.save(self.file_name, transactions)

        return self
