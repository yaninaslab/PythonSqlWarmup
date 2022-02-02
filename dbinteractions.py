import mariadb as db
import dbcreds
import traceback as t


def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except:
        print("Something went wrong!")
    return conn, cursor


def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except:
        print("The issue with cursor")
    try:
        conn.close()
    except:
        print("The issue with connection")


def attempt_login(username, password):
    user = None
    conn, cursor = connect_db()

    try:
        cursor.execute(
            f"select id from `user` u where username = '{username}' and password = '{password}'")
        user = cursor.fetchone()

    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
        # t.print_exc()
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
        # t.print_exc()
    except:
        print("Something went wrong!")
        # t.print_exc()

    disconnect_db(conn, cursor)

    if(user == None):
        return False
    else:
        return True


def show_items():
    items = None
    conn, cursor = connect_db()
    try:
        cursor.execute(f"select id, name, description, quantity from item")
        print("Here are the available items:")
        items = cursor.fetchall()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    for item in items:
        print("")
        print(f"{item[0]}: {item[1]} --- {item[3]}")
        print(item[2])
        print("")


def buy_item(name):
    conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                      host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute(
        f"update item set quantity = quantity - 1 where name = '{name}'")
    conn.commit()

    cursor.close()
    conn.close()
