from user.models.User import User
from user.models.UserAccounts import UserAccounts
from user.models.Transactions import Transactions

def menu():
    login = input("Login: ")
    pincode = input("Pincode: ")

    user = User()
    user = user.login(login, pincode)

    if user:
        if(user.type == "Customer"):

            user_account = UserAccounts()
            user_account = user_account.get(user.id)

            if user_account:
                user_account.account_type
            else:
                print("Invalid user account")

            #transaction = Transactions(2, user_account.id, 2, 5000, user_account.account_type, 12, user_account.balance)
            #transaction.save()

            print("Customer Menu")

            print("1---Withdraw Cash.\n"
                  "2---Cash Transfer.\n"
                  "3---Deposit Cash.\n"
                  "4---Display Balance.\n"
                  "5---Exit.\n\n")

            x = int(input("Please select one of the above options: "))

            if x == 1:
                print("Withdraw Cash\n")

                print("1---Normal Cash.\n"
                      "2---Fast Cash.\n\n")

                x = int(input("Please select a mode of withdrawal: "))

                if x == 1:
                    print("Fast Cash\n")

                    print("1---500\n"
                          "2---1000\n"
                          "3---2000\n"
                          "4---5000\n"
                          "5---10000\n"
                          "6---15000\n"
                          "7---20000\n\n")

                    with_draw = int(input("Select one of the denominations of money: \n"))

                    y = input("Are you sure you want to withdraw ------ (Y/N)? ")

                    if y == 'Y' or y == 'y':
                        print("Cash Successfully withdrawn!\n")
                    elif y == 'N' or y == 'n':
                        print("Transaction is cancelled!\n")

                    z = input("Do you wish to print a receipt (Y/N)?")

                    if z == 'Y' or z == 'y':
                        print("Account # ", user_account.account_number)
                        print("Date: ", user.date)
                        print("Withdrawn: ", with_draw)
                        print("Balance: ", user_account.update(user_account.balance))
                    elif z == 'N' or z == 'n':
                        pass

                elif x == 2:
                    print("Normal Cash\n\n")

                    x = int(input("Enter the withdrawal amount: \n"))

                    print("Cash Successfully Withdrawn!")

                    print("Do you wish to print a receipt (Y/N)?")

                    z = input()

                    if z == 'Y' or z == 'y':
                        print("Account # ")
                        print("Date: ")
                        print("Withdrawn: ")
                        print("Balance: ")
                    elif z == 'N' or z == 'n':
                        pass

            elif x == 2:
                print("Cash Transfer")

                print("Enter amount in multiples of 500: ")

                x = int(input())

                print("Enter the account number to which you want to transfer: ")

                z = int(input())

                print("You wish to deposit Rs ", x, "in account held by Mr. "
                      , '''account holder name''',
                      "if this information is correct please re-enter the account number: ")

                p = int(input())

                print("Transaction confirmed.")

                print("Do you wish to print a receipt (Y/N)?")

                z = input()

                if z == 'Y' or z == 'y':
                    print("Account # ")
                    print("Date: ")
                    print("Transferred: ")
                    print("Balance: ")
                elif z == 'N' or z == 'n':
                    pass

            elif x == 3:
                print("Deposit Cash")

                print("Enter the cash amount to deposit: ")

                x = int(input())

                print("Cash deposited successfully!")

                print("Do you wish to print a receipt (Y/N)?")

                z = input()

                if z == 'Y' or z == 'y':
                    print("Account # ")
                    print("Date: ")
                    print("Deposited: ")
                    print("Balance: ")
                elif z == 'N' or z == 'n':
                    pass

            elif x == 4:
                print("Display Balance")

                print("Account # ")
                print("Date: ")
                print("Balance: ")

            elif x == 5:
                # exit
                pass

            else:
                print("Pleas Enter the right choice.")

        else:
                print("Administrator Menu\n\n")

                print("1---Create New Account.\n"
                      "2---Delete Exsiting Account.\n"
                      "3---Update Account Information.\n"
                      "4---Search for Account.\n"
                      "5---View Reports.\n"
                      "6---Exit.\n\n")

                print("Please Select one of the above options: ")

                p = int(input())

                if x == 1:
                    print("Creating New Account...\n\n")

                elif x == 2:
                    print("Deleting Existing account...\n\n")

                elif x == 3:
                    print("Updating account information...\n\n")

                elif x == 4:
                    print("Searching for account...\n\n")

                elif x == 5:
                    print("Reports")

                elif x == 6:
                    pass

                else:
                    print("Please enter the right choice.")

            else:
                print("please enter the right choice")


    else:
    print("invalid login")

