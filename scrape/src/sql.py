import mysql.connector as mydb


class Sql:
    def __init__(self):
        # コネクションの作成
        self.conn = mydb.connect(
            host='mysql',
            port='3306',
            user='mysql',
            password='mysql',
            database='mydb'
        )
        self.conn.ping(reconnect=True)
        # カーソルの生成
        self.cursor = self.conn.cursor(buffered=True, dictionary=True)

    def deleteTable(self):
        # 実行するたびに同じ結果になるようにテーブルを削除しておく
        self.cursor.execute("DROP TABLE IF EXISTS pc_specs")
        self.conn.commit()

    def createTable(self):
        # テーブルを作成する
        self.cursor.execute(
            "CREATE TABLE pc_specs (id INT(11) AUTO_INCREMENT NOT NULL, name VARCHAR(50) NOT NULL, price VARCHAR(10) NOT NULL, processor VARCHAR(50) NOT NULL, memory VARCHAR(50) NOT NULL, PRIMARY KEY (id));")
        self.conn.commit()

    def insertItem(self, name, price, processor, memory):
        self.cursor.execute(
            "INSERT INTO pc_specs (name, price, processor, memory) VALUES (%s, %s, %s, %s);", (name, price, processor, memory))
        # self.cursor.execute("INSERT INTO pc_specs (name, price, processor, memory) VALUES ('name1', 'price1', 'processor1', 'memory1');")
        self.conn.commit()

    def getAllItem(self):
        self.cursor.execute("SELECT * from pc_specs")
        self.conn.commit()
        data = self.cursor.fetchall()
        return data

    def finish(self):
        self.cursor.close
        self.conn.close
