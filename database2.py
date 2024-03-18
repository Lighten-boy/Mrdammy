import mysql.connector as sql
# mycon =  sql.connect(host = "127.0.0.1", user = "root", passwd = "")
mycon = sql.connect(host = "127.0.0.1", user = "root", database = "banks_database")

mycursor = mycon.cursor()

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)


# mycursor.execute("CREATE DATABASE banks_database")

mycursor.execute("CREATE TABLE if not exists lightenbank_account (acc_no int primary key auto_increment, fullname VARCHAR(50),email VARCHAR(50) UNIQUE, mobile_no char(10), balance int(6))")
mycursor.execute("CREATE TABLE if not exists transaction(acc_no int(6), amount int(6), ttype char(1), foreign key (acc_no) references lightenbank_account(acc_no))")
print('welcome to Lighten bank')
while True:
    print("1.Create account\n 2.Deposit money\n 3.Withdraw Money\n 4.View account details\n 5.Exit")

    ch = int(input("Enter your choice:"))
    if ch == 1:
        fullname = input("Enter your fullname:")
        email = input("Enter your email:")
        mn = input("Enter your mobile no:")
        balance = 0
        sql = "insert into lightenbank_account(fullname,email,mobile_no,balance) values (%s,%s,%s,%s)"
        val = (fullname, email, mn, balance)
        mycursor.execute(sql, val)
        mycon.commit()
        mycursor.execute("select * from  lightenbank_account where fullname='" + fullname + "'")
        print("Account is sucessfully created!")
        for i in mycursor:
            print(i)
    elif ch == 2:
        accno = input("Enter account no:")
        dp = int(input("Enter amount to be deposited:"))
        ttype = "d"
        mycursor.execute("insert into transaction values('" + accno + "','" + str(dp) + "','" + ttype + "')")
        mycursor.execute("update lightenbank_account set balance=balance+'" + str(dp) + "' where acc_no='" + accno + "'")
        print("#", dp, " has been deposited successfully in account no: ",accno)
    elif ch == 3:   
        accno = input("Enter account no:")
        wd = int(input("Enter amount to be withdraw:"))
        select_Query = "select balance from lightenbank_account where acc_no =cd '" + accno +"' "
        mycursor.execute(select_Query)
        bal = mycursor.fetchone()[0]
        if wd < bal:
            ttype = "w"
            mycursor.execute("insert into traction values('" + accno + "','" + str(wd) + "','" + ttype + "')")
            mycursor.execute("update lightenbank_account set balance=balance-'" + str(wd) + "' where acc_no='" + accno + "'")
            print("#", wd, " has been withdraw successfully in account no: ",accno)
        else:
            print("can't withdraw money. Insuffient balance!")
    elif ch == 4:
        accno = input("Enter account no:")
        mycursor.execute("select * from  lightenbank_account where accno='" + accno + "'")
        for i in mycursor:
            print(i)
    else:
        break