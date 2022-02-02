import dbinteractions as dbi

username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username == dbi.user[1] and password == dbi.user[2]:
    dbi.attempt_login(username, password)
