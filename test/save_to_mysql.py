import pymysql


if __name__ == '__main__':
    # 打开数据库连接
    db = pymysql.connect(host="localhost",user= "root",password= "12345678",database= "TEST")

    # 获取游标
    cursor = db.cursor()
    
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")
    
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    
    print ("Database version : %s " % data)
    

    # # 进行判断，如果表存在就删除表
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    # # 创建数据库表SQL语句
    # sql = """CREATE TABLE EMPLOYEE(
    #     FIRST_NAME  CHAR(20) NOT NULL,
    #      LAST_NAME  CHAR(20),
    #      AGE INT,  
    #      SEX CHAR(1),
    #      INCOME FLOAT 
    #     )"""
    
    # cursor.execute(sql)
    
    # 关闭数据库
    db.close()  