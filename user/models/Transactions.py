from user.utils import db


class Transactions:

    file_name = "transaction.txt"

    def __init__(self, id, account_number, transaction_id, amount, account_type, date, balance):
        self.id = id
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transaction_id = transaction_id
        self.amount = amount
        self.date = date

    def get_id(self):
        return self.id

    def get_account_number(self):
        return self.account_number

    def show_balance(self):
        return self.balance

    def get_account_type(self):
        return self.account_type

    def get_transaction_id(self):
        return self.transaction_id

    def get_amount(self):
        return self.amount

    def get_date(self):
        return self.date

    def withdraw(self):
        pass

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.save()

    def transfer(self):
        pass

    def save(self):
        transactions= []
        try:
            transactions= db.get(self.file_name)
        except Exception as e:
            pass

        data = "%s,%s,%s,%s,%s,%s,%s" % (self.id, self.account_number, self.transaction_id, self.amount, self.account_type, self.date, self.balance)
        transactions.append(data)
        db.save(self.file_name, transactions)

    def update(self):
        transactions= []
        try:
            transactions= db.read(self.file_name)
        except Exception as e:
            pass

        for index, user in transactions:
            attributes = user.split(",")
            if self.id == attributes[0]:
                transactions.pop(index)

        data = "%s,%s,%s,%s,%s,%s,%s" % (self.id, self.account_number, self.transaction_id, self.amount, self.account_type, self.date,self.balance)
        transactions.append(data)
        db.save(self.file_name, transactions)
