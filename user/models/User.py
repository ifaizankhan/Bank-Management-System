from user.utils import db


class User:

    file_name = "user.txt"

    def __init__(self, id, name, login_id, pincode, type, date = None):
        self.id = id
        self.name = name
        self.login_id = login_id
        self.pincode = pincode
        self.type = type
        self.date = date

    def login(self):
        pass

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
