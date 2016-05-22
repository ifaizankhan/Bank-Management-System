from user.models.User import User


def prepare():
    with open("user.txt", "r+") as f:
        f.write("")


def test_save():
    print("This will test save")
    u = User(1, "faizan", "ff", "g", "h")
    u.save()


def test_update():
    print("This will test update")
    u = User(1, "faizan khan", "ff", "g", "h")
    u.update()


def run_tests():
    prepare()
    test_save()
    test_update()