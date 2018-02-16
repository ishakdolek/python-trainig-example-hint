
import sqlite3


con = sqlite3.connect("libraries.db")
cursor = con.cursor()
def create_table():
cursor.execute("CREATE TABLE IF NOT EXISTS SELAM(first_name text ,last_name text)")
con.commit()

commandText=("Update SELAM SET first_name=? where Id=1","ishak")


# def insert_data():
# cursor.execute("insert into Test VALUES('ishak','dölek')")
# con.commit()


#     def verileri_al():
#     cursor.execute("select * from Contacts")
#     liste=cursor.fetchall()
#     print(liste)

#     con.close()



# operation=dbOperation()

# operation.create_table()

# operation.insert_data()
