from cmath import log
import dbinteractions as dbi
import getpass as gp

username = input("Please enter your username: ")
password = gp.getpass("Please enter your password: ")

login_success = dbi.attempt_login(username, password)
if(login_success == True):
    print("Authentication success!")
    dbi.show_items()
    item_name = input("Please type an item name to buy: ")
    dbi.buy_item(item_name)
    print("Thank you, come again!")
    exit()

else:
    print("Sorry, authentication failure")
