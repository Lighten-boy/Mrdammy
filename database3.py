import mysql.connector as sql
import time
import pwinput as pw
import random
num = random.randint(38569634,3697346996)
import colorama
from colorama import Fore,Back,init
import datetime as dt
# mycon =  sql.connect(host = "127.0.0.1", user = "root", passwd = "")
mycon = sql.connect(host = "127.0.0.1", user = "root", database = "bank_database3")

mycursor = mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE DATABASE bank_database3")

# mycursor.execute("CREATE TABLE if not exists lightenbank2_account (id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50),email VARCHAR(50) UNIQUE, password VARCHAR(20), account_no VARCHAR(15) UNIQUE, account_bal FLOAT(15))")
# mycursor.execute("CREATE TABLE if not exists transaction(id int(10), amount int(6), ttype char(1), foreign key (id) references lightenbank2_account(id))")
# print('welcome to Lighten bank')

class login():
    def __init__(self) :
         
         self.Sign_up()
    def Sign_up(self):
      self.fullname = input("Fullname:")
      self.email = input("Email:")
      self.password = input("Password:")
     #  myquery = "INSERT INTO lightenbank2_account (fullname,email,password,account_no) VALUES(%s,%s,%s,%s)"
     #  val = (self.fullname,self.email,self.password)
     #  mycursor.execute(myquery,val)
     #  mycon.commit()
      print(mycursor.rowcount,f"record inserted successfully. Your account number is {num} Redirecting to login page")
      time.sleep(2)


      self.account_no = input("Account_no:")
      myquery = "INSERT INTO lightenbank2_account (fullname,email,password,account_no) VALUES(%s,%s,%s,%s)"
      val = (self.fullname,self.email,self.password,self.account_no)
      mycursor.execute(myquery,val)
      mycon.commit()