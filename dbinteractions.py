import mariadb as db
import dbcreds


def attempt_login(self, username, password):
    conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                      host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute(f"select username, password from `user` u")
    users = cursor.fetchall()

    cursor.close()
    conn.close()
