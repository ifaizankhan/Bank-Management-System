from user.models.UserAccounts import UserAccounts


def prepare():
    with open("useraccount.txt", "r+") as f:
        f.write("")


def test_save():
    print("This will test save")
    u = UserAccounts(1, "faizan", 12345, 5000, "saving","active")
    u.save()

def test_update():
    print("This will test update")
    u = UserAccounts(1, "faizan khan", 12345, 5000, "saving", "active")
    u.update()



def run_tests():
    prepare()
    test_save()
    test_update()