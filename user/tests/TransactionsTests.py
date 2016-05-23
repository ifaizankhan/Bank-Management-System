from user.models.Transactions import Transactions


def prepare():
    with open("transaction.txt", "r+") as f:
        f.write("")


def test_save():
    print("This will test save")
    u = Transactions(1, 2, 12345, 5000, "saving", 2, 5)
    u.save()

def test_update():
    print("This will test update")
    u = Transactions(1, 2, 12345, 5000, "saving", 2, 5)
    u.update()



def run_tests():
    prepare()
    test_save()
    test_update()