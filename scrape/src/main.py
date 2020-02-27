from sql import Sql
from parser import Parser

if __name__ == "__main__":
    sql = Sql()
    sql.deleteTable()
    sql.createTable()

    dics = Parser.main()
    for dic in dics:
        # print("inserted :",format(dic))
        sql.insertItem(**dic)
    
    # print(sql.getAllItem())
    sql.finish()