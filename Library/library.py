
import sqlite3

class Kitap():
    def __init__(self,isim,yazar):
        self.isim=isim
        self.yazar=yazar
    def __str__():
        return "Kitap: {}\n Yazar:{}\n".format(self.isim,self.yazar)



class Library(self):
 def __init__(self):
     self.connection()

 def connection(self):
     self.con=sqlite3.connect("library.db")
     self.cursor=self.con.cursor()
     sorgu="create table If not exists kitaplar(isim TEXT,yazar TEXT)"
     self.cursor.execute(sorgu)
     self.con.commit()
 
 def close_connection(self):
     self.close()
    
 def show_book(self):
     sorgu = "select * from kitaplar"
     self.cursor.execute(sorgu)
     liste=self.cursor.fetchall()

