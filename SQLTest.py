import sqlite3


# 数据库操作老保存数据。

def create_sql():
    conn = sqlite3.connect("sqlite.db")  # 创建sqlite.db数据库
    query = """create table IF NOT EXISTS score(
        id INTEGER primary KEY AUTOINCREMENT ,
        customer VARCHAR(20)
    );"""
    conn.execute(query)



def insert(score):
    with sqlite3.connect("sqlite.db") as conn:
        cursor = conn.cursor()
        cursor.execute('insert into score ( customer) values ( "{}") '.format(score))
        print(cursor.rowcount)
        cursor.close()
        conn.commit()

def query():
    with sqlite3.connect("sqlite.db") as conn:
        cursor = conn.cursor()
        cursor.execute('select * from score ')
        values = cursor.fetchall()
        print(values)
        cursor.close()


create_sql()
insert(250)
query()
