import sqlite3

conn = sqlite3.connect('UserData.db')
cursor = conn.cursor()

def insertDb():
    sql ="""
         create table member(
            idx integer primary key autoinrement,
            Email text not null,
            Lastname text not null,
            Fristname text not null,
            Password text not null,
            regDate default(datetime('now', 'localtime')))
    """

def readDb():
    pass

def main():
    insertDb()
    readDb()
    conn.close()

if __name__ == '__main__':
    main()