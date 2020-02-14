import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host='mysql-test',
    port='3306',
    user='mysql',
    password='mysql',
    database='mydb'
)

# カーソルの生成
cursor = conn.cursor()

# 実行するたびに同じ結果になるようにテーブルを削除しておく
cursor.execute("DROP TABLE IF EXISTS pc_specs")

# テーブルを作成する
cursor.execute("CREATE TABLE pc_specs ()")
cursor.commit()