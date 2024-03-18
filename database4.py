import mysql.connector as sql
import time
import pwinput as pw
import random
num = random.randint(38569634,3697346996)
import colorama
from colorama import Fore,Back,init
import datetime as dt

# mycon =  sql.connect(host = "127.0.0.1", user = "root", passwd = "")
mycon = sql.connect(host = "127.0.0.1", user = "root", database = "bank_database4")

mycursor = mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE DATABASE bank_database4")

mycursor.execute("CREATE TABLE if not exists lightenbank2_account (id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50),email VARCHAR(50) UNIQUE,username VARCHAR(50) ,password VARCHAR(20),address VARCHAR(50) , phone INT(12), account_no VARCHAR(15) UNIQUE, account_bal FLOAT(15))")
mycursor.execute("CREATE TABLE if not exists transaction(id int(10), amount int(6), ttype char(1), foreign key (id) references lightenbank2_account(id))")
print('welcome to Lighten bank')


class bank():
     def __init__(self) :
        colorama.init()
        self.balance=0
        self.landing_page()
        self.account_no= random.randint(1000000000,99999999999)
     def landing_page(self):
        print(colorama.Fore.BLUE+"WELCOME TO LIGHTEN BANK".center(50,"-"))
        print(colorama.Fore.RESET)
        print("1.Sign Up\n2.Login\n3.Exit")
        user = input("Input Choice:").strip()
        if user == "1":
             self.account_no = random.randint(1000000000,99999999999)
             self.Sign_up()
        elif user == "2":
            self.login()
        elif user == "3":
            exit()
        else:
            print("Invalid input\nInput number from 1-3 only")
            time.sleep(2)
            self.landing_page()
     def sign_up(self):
         print(colorama.Fore.BLUE+"Sign up if you have an account".center(50,"-"))
         print(colorama.Fore.RESET)
         fullname = input("Fullname:").strip().lower()
         email = input("Email:").strip().lower()
         username = input("Username:").strip().lower()
         password = input("Password:").strip().lower()
         address = input("City\Town:").strip().lower()
         phone = int(input(("Phone Number:").strip()))
         account_type = input("Account type(savings/current):").strip().lower()
         tim=dt.datetime.now()
         date=tim
         print(f"Your account number is --{self.account_no}--")
         if email.endswith(".com") and "@" in email :
             print("You have an account with us \n Thank you for your banking with us")
         else:
             print("Invalid email address")

         myquery = "INSERT INTO lightenbank2_account (fullname,email,username,password,address,phone,date,account_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
         val = (fullname,email,username,password,address,phone,date,self.account_no,account_type)
         mycursor.execute(myquery,val)
         mycon.commit()
         print(mycursor.rowcount,"record inserted sucessfully")

         time.sleep(2)
         self.login()

     def login(self):
         print(colorama.Fore.BLUE+"WELCOME BACK".center(50,"-"))
         print(colorama.Fore.RESET)
         username = input("username: ").strip().lower()
         password = input("Password:").strip().lower()
         query= "SELECT * FROM customer WHERE username=%s and passwords=%s"
         val = (username,password)
         mycursor.execute(query,val)
         output = mycursor.fetchall()
         if output:
             print(colorama.Fore.LIGHTYELLOW_EX+"1.Deposit\n2.Withdraw\n3.Transfer\n4.check balance\n5.view transaction history\n6.account_no\n7.exit")
             print(colorama.Fore.RESET)
             option=input("Input your option:")
             if option== "1":
                 self.deposit()
             elif option== "2":
                 self.withdraw()
             elif option== "4":
                 self.balance()
             elif option== "5":
                 self.history()
             elif option== "6":
                 self.account_no()
             elif option== "7":
                 exit()
             else:
                 print("Wrong input")

 