import sqlite3

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()


def insertDb():
    sql = """
        insert into member(Email, Lastname, Firstname, Password)
        values('hong1','1323','hong1@')
    """
    cursor.execute(sql)
    conn.commit()


def readDb():
    cursor.execute("select*from member")
    rows = cursor.fechall()
    for row in rows:
        print(row)


def main():
    insertDb()
    readDb()
    conn.close()


if __name__ == '__main__':
    main