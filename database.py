# import mysql.connector as sql
# # mycon = sql.connect(host = '127.0.0.1', user = 'root', passwd = '')

# mycon = sql.connect(host = '127.0.0.1', user = 'root', passwd = '' , database = 'bank_database')

# mycursor = mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor.execute("CREATE DATABASE bank_database")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
# mycursor.execute("CREATE DATABASE bank_database")
# def login():
#     username_inp = input('username: ')
#     password_inp = input('password: ')
#     query = 'SELECT * from customer_table WHERE username =%s and password = %s'
#     val = (username_inp,password_inp)
#     mycursor.excute(query, val)
#     output = mycursor.fetchall()
#     print(output)

#     if output:
#         print('Login successful')
#     else:
#         print('invalid username or password')


import mysql.connector as sql
# mycon =  sql.connect(host = "127.0.0.1", user = "root", passwd = "")
mycon = sql.connect(host = "127.0.0.1", user = "root", database = "bank_database")

mycursor = mycon.cursor()
 
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE DATABASE bank_database")

# mycursor.execute("CREATE TABLE customer_table (id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50),email VARCHAR(50) UNIQUE, password VARCHAR(20))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)

# mycursor.execute("ALTER TABLE customer_table ADD (account_no VARCHAR(15) UNIQUE, account_bal FLOAT(15))")


# mycursor.execute("INSERT INTO customer_table (fullname, email, password, account_no, account_bal) VALUES('Solademi Israel','Israelsolademi@gmail.com','1234567', '217658356','700000000000')")
# mycon.commit()




import random

class login():
    def __init__(self) :
         
         self.Sign_up()
    def Sign_up(self):
      self.fullname = input("Fullname:")
      self.email = input("Email:")
      self.password = input("Password:")
      myquery = "INSERT INTO customer_table (fullname,email,password) VALUES(%s,%s,%s)"
      val = (self.fullname,self.email,self.password)
      mycursor.execute(myquery,val)
      mycon.commit()
      print(mycursor.rowcount,"record inserted successfully")
log  = login()      



# def login():
#     username_inp  = input("Username:")
#     password_inp = input("Password:")
#     query = "SELECT * FROM customer_table WHERE username = %s and password = %s "
#     val = (username_inp, password_inp)
#     mycursor.execute(query,val)
#     output = mycursor.fetchall()
#     print(output)

#     if output :
#         print("Login successful")
#     else:
#         print("Invalid username or password")

# login()    


# searching by while card "%"
# query =  "SELECT *FROM customer_table WHERE username LIKE '%ajayi'"
# query =  "SELECT *FROM customer_table WHERE username LIKE 'a%'"  #startwith
# mycursor.execute(query)
# myreg = mycursor.fetchall()
# print(myreg)