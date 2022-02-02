import mariadb as db
import dbcreds


def attempt_login(username, password):
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
        cursor.execute(
            f"select id from `user` u where username = '{username}' and password = '{password}'")
        user = cursor.fetchone()

        cursor.close()
        conn.close()
    except:
        print("Something went wrong!")

    if(user == None):
        return False
    else:
        return True


def show_items():
    conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                      host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute(f"select id, name, description, quantity from item")
    print("Here are the available items:")
    items = cursor.fetchall()
    for item in items:
        print("")
        print(f"{item[0]}: {item[1]} --- {item[3]}")
        print(item[2])
        print("")
    cursor.close()
    conn.close()


def buy_item(name):
    conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                      host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute(
        f"update item set quantity = quantity - 1 where name = '{name}'")
    conn.commit()

    cursor.close()
    conn.close()
