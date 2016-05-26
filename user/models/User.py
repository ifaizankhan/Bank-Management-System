from user.utils import db


class User:

    file_name = "user.txt"

    def __init__(self, id=None, name=None, login_id=None, pincode=None, type=None, date=None):
        self.id = id
        self.name = name
        self.login_id = login_id
        self.pincode = pincode
        self.type = type
        self.date = date

    def get(self, id):
        users = db.get(self.file_name)

        for user in users:
            attributes = user.split(',')
            if attributes[0] == id:
                return User(attributes[0], attributes[1], attributes[2], attributes[3], attributes[4], attributes[5])

        return None

    def login(self, login_id, pincode):
        users = db.get(self.file_name)

        for user in users:
            attributes = user.split(',')
            if attributes[2] == login_id and attributes[3] == pincode:
                return self.get(attributes[0])

        return None

    def logout(self):
        pass

    def is_login(self):
        pass

    def save(self):
        users = []
        try:
            users = db.get(self.file_name)
        except Exception as e:
            pass

        data = "%d,%s,%s,%s,%s,%s" % (self.id, self.name, self.login_id, self.pincode, self.type, self.date)
        users.append(data)
        db.save(self.file_name, users)

    def update(self):
        users = []
        try:
            users = db.read(self.file_name)
        except Exception as e:
            pass

        for index, user in users:
            attributes = user.split(",")
            if self.id == attributes[0]:
                users.pop(index)

        data = "%d,%s,%s,%s,%s,%s" % (self.id, self.name, self.login_id, self.pincode, self.type, self.date)
        users.append(data)
        db.save(self.file_name, users)
