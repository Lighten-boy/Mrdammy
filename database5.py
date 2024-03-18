import mysql.connector as sql
import time
import pwinput as pw
import random
num = random.randint(38569634,3697346996)
import colorama
from colorama import Fore,Back,init
import datetime as dt

# mycon =  sql.connect(host = "127.0.0.1", user = "root", passwd = "")
mycon = sql.connect(host = "127.0.0.1", user = "root", database = "bank_database5")

mycursor = mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE DATABASE bank_database5")

mycursor.execute("CREATE TABLE if not exists lightenbank5_account (id INT(4) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50),email VARCHAR(50) UNIQUE,username VARCHAR(50) ,password VARCHAR(20),address VARCHAR(50) , phone INT(12), account_no VARCHAR(15) UNIQUE, account_bal FLOAT(15))")
mycursor.execute("CREATE TABLE if not exists transaction5(id int(10), amount int(6), ttype char(1), foreign key (id) references lightenbank5_account(id))")
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
             self.sign_up()
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
         print("pls wait some sec to verify your details and also checking if your gmail address is valid thank you for waiting")
         time.sleep(3)
         if email.endswith(".com") and "@" in email :
             print("Thank you for your patience your account has been verified😊.")
         else:
             print("Invalid email address")

         myquery = "INSERT INTO lightenbank5_account (fullname,email,username,password,address,phone,account_no) VALUES(%s,%s,%s,%s,%s,%s,%s)"
         val = (fullname,email,username,password,address,phone,self.account_no,account_type)
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
         query= "SELECT * FROM lightenbank5_account WHERE username=%s and passwords=%s"
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

     def deposit(self):
         print(colorama.Fore.BLUE+"WELCOME TO THE TRANSACTION PAGE".center(50,"-"))
         print(colorama.Fore.RESET)
         account_no = input("Enter account no:")
         dp = int(input("Enter amount to be deposited:"))
         ttype = "d"
         mycursor.execute("insert into transaction values('" + account_no + "','" + str(dp) + "','" + ttype + "')")
         mycursor.execute("update lightenbank_account set balance=balance+'" + str(dp) + "' where id='" + account_no + "'")
         print("#", dp, " has been deposited successfully in account no: ",account_no)

     def withdraw(self):
         print(colorama.Fore.BLUE+"WELCOME TO THE TRANSACTION PAGE".center(50,"-"))
         print(colorama.Fore.RESET)
         account_no = input("Enter account no:")
         wd = int(input("Enter amount to be withdraw:"))
         select_Query = "select balance from lightenbank_account where acc_no =cd '" + account_no +"' "
         mycursor.execute(select_Query)
         bal = mycursor.fetchone()[0]
         if wd < bal:
            ttype = "w"
            mycursor.execute("insert into traction values('" + account_no + "','" + str(wd) + "','" + ttype + "')")
            mycursor.execute("update lightenbank_account set balance=balance-'" + str(wd) + "' where id='" + account_no + "'")
            print("#", wd, " has been withdraw successfully in account no: ",account_no)
         else:
            print("can't withdraw money. Insuffient balance!")
         
              

lighten = bank()