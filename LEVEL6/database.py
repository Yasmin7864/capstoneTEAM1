import mysql.connector

class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        try:
            self.connection=mysql.connector.connect(host=self.host,
                                                    database=self.db,
                                                    user=self.user,
                                                    password=self.password)
        except:
            print("Error while connecting to the database")
    def inser_data(self,filename):
        self.filename=filename
        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);"
        val=(self.filename)

        self.cur.execute(sql,(val,))
        self.connection.commit()

    def search(self):
        self.cur= self.connection.cursor()
        sql="SELECT * FROM user limit 0,10"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
dbobj=Mysql_DBaccess('localhost','root','SALEEMasha@7','searchfiles')

dbobj.inser_data('C:/hcl1/file1.txt')

