import pymysql

class Mydb():
    def __init__(self,host,user,password,dbname):
        try:
            self.conn = pymysql.connect(host, user, password, dbname, charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print('连接失败', e)

    def execute(self,sql,values):
        try:
            res = self.cursor.execute(sql,values)
            self.conn.commit()
            return res
        except Exception as e:
            self.conn.rollback()
            print('增删改失败' , e)

    def query(self,sql):
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except Exception as e:
            print('查询失败' ,e)

    def close(self):
        self.cursor.close()
        self.conn.close()