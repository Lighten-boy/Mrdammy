# import time
# import json
# import pwinput as pw
# import random
# num = random.randint(38569634,3697346996)
# from colorama import Fore,Back,init


# # personnels_login = {}
# # database = json.dumps(personnels_login)
# # print(database)
# # with open(r'C:\myclass\bankingapp.txt', 'w') as file:
# #     file.write(database)


# class Create_Invoice:
#     def __init__(self):
#         self.home()
#         self.account = random.randint(38569634,3697346996)
#         self.name = 'Lighten boy PLC'

#     def home(self):
#         print('Lighten Bank'.center(30,'_'))
#         print('1. Register\n2. Login\n3. Exit')
#         user = input('choose your option: ')
#         if user == '1':
#             self.Register()
#         elif user == '2':
#             self.login()
#         elif user == '3':
#             exit()
            
#         else:
#             print('Invalid Input!!!\n')
#             time.sleep(2)
#             self.home()


#     def Register(self):
#         print('Sign up')
#         file = open(r'C:\myclass\bankingapp.txt', 'r')
#         database = file.read()
#         personnels_login = json.loads(database)
#         # print(personnels_login)  

#         print(f'Sign Up'.center(50,'_'))
#         username = input('Username: ').strip().lower()   
#         # email = username = input('Email: ').strip().lower()
#         password = input('pin (4 Digit): ').strip()

#         personnels_login.update({username:password})
#         print(personnels_login)

#         # saving to a database
#         database = json.dumps(personnels_login)
#         # print(database),
#         with open(r'C:\myclass\bankingapp.txt', 'w') as file:
#             file.write(database)


#         print(f'''Sign up successful. Redirecting to login page.
#               your account is {self.account}''')
#         time.sleep(2)
#         self.login()


#     def login(self):
#         file = open(r'C:\myclass\bankingapp.txt', 'r')
#         database = file.read()
#         personnels_login = json.loads(database)
#         # print(personnels_login)
#         print('Login'.center(50, '_'))

#         username = input('Username: ').strip().lower()
#         password = pw.pwinput()

#         if password == personnels_login[username]:
#             print('''
#                     1. Transfer to bank
#                     2. Withdraw
#                     3. Buy data
#                 ''')
#             user = input('choose option: ')
#             if user == '1':
#                 print(input('Enter account number: '))
#             elif user == '2':
#                 print(input('Amount to withdraw: '))
#             elif user == '3':
#                 print(f'''
#               1. Daily plan
#               2. Weekly plan
#               3. Monthly plan
#               4. Yealy plan
#               5. Night sub''')
#         user = input('choose option: ')
#         if user == '1':
#             print(f'''
#                   1. 50mb for 50
#                   2. 100mb for 100
#                   3. 1gb for 350''')
#             user = input('choose option: ')
#             if user == '1':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '2':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '3':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             else:
#                 print('invalid code')
#         elif user == '2':
#             print(f'''
#                   1. 1gb for 700
#                   2. 3gb for 1500
#                   3. 5gb for 3000''')
#             user = input('choose option: ')
#             if user == '1':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '2':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '3':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             else:
#                 print('invalid code')
#         elif user == '3':
#             print(f'''
#                   1. 10gb for 10000
#                   2. 20gb for 20000
#                   3. 30gb for 30000''')
#             user = input('choose option: ')
#             if user == '1':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '2':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '3':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             else:
#                 print('invalid code')
#         elif user == '4':
#             print(f'''
#                   1. 1tb for 1000000
#                   2. 2tb for 2000000
#                   3. 3tb for 3000000''')
#             user = input('choose option: ')
#             if user == '1':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '2':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '3':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             else:
#                 print('invalid code')
#         elif user == '5':
#             print(f'''
#                   1. 250mb for 25
#                   2. 500mb for 50
#                   3. 1gb for 100''')
#             user = input('choose option: ')
#             if user == '1':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '2':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             elif user == '3':
#                 print('You have sucessfully recieved 50mb from MTN and will expire 0n 07/07/2007 03:01:50.Kindly dial*312*4# to check data balance')
#             else:
#                 print('invalid code')
#         else:
#             print('Wrong username and password')



#         self.home()       


# invoice = Create_Invoice()









import time
import json
import pwinput as pw
import random
num = random.randint(38569634,3697346996)
from colorama import Fore,Back,init



# personnels_login = {}
# database = json.dumps(personnels_login)
# print(database)
# with open(r'C:\myclass\bankingapp.txt', 'w') as file:
#       file.write(database)

class bank:
    def __init__(self):
        self.home()
        # self.account_no = random.randint(38569634,3697346996)
        self.name = 'LIGHTEN BANK PLC'
        

    def home(self):
        print('Lighten Bank'.center(50,'-'))
        print('1. Register\n2. login\n3.Exit')
        user =input('option:  ')
        if user =='1':
            self.sign_up()
        elif user == '2':
            self.login()
        elif user == '3':
            exit()
        else :
            print('Invalid input!!!\n')
            time.sleep(2)
            self.home()           


    def sign_up(self):
        init(autoreset=True)
        print(f'{Fore.LIGHTBLUE_EX}Register'.center(50,'-') )
        file = open(r'C:\myclass\bankingapp.txt', 'r')
        database = file.read()
        personnels_login = json.loads(database)
        # print(personnels_login)

        username = input('Username:  ').strip().lower()
        password = input('Password:   ').strip().lower()
        # email = input('Email:  ').strip().lower()
     
        personnels_login.update({username:password})
        # print(personnels_login)
        # sacving to a temporary database 
        database = json.dumps(personnels_login)
        # print(database)
        with open(r'C:\myclass\bankingapp.txt', 'w') as file:
          file.write(database)


        print(f'''{Fore.LIGHTBLUE_EX} Sign up successful .
              Your account number is {num}
              Redirecting to login page''')
        time.sleep(2)
        self.login()


    def login(self):
        file =open(r'C:\myclass\bankingapp.txt', 'r')
        database = file.read()
        personnels_login = json.loads(database)
        # print(personnels_login)
        print('Login'.center(50, '-'))

    
           


        username = input('Username: ').strip().lower()
        password = pw.pwinput()
    

        if password == personnels_login[username]:
          print(f'''{Fore.LIGHTBLUE_EX}Welcome.....{num}''')
          answer = input(f''' {Fore.LIGHTYELLOW_EX}
                1. withdraw
                2. transfer
                3. check balance
                4.exit \n  
                Option:  ''')
          if answer == '1':
              self.withdraw()
                
          elif answer == '2':
               self.transfer()
              
                      
          elif answer == '3':
               username = input('Username: ').strip().lower()
               password = pw.pwinput()
                        
        
        
        

        else: 
          print(f'{Fore.LIGHTBLUE_EX}Wrong username and password')




          self.home()




    def withdraw(self):
        reply = input( f''' 
        1. 1_000
        2. 5_000
        3. 10_000
        4. 20_000
        5.others\n\n 
        Option:  ''')
        if reply == '1':
                    # username = input('Username: ').strip().lower()
                    password = pw.pwinput()
        elif reply == '2':
                    # username = input('Username: ').strip().lower()
                    password = pw.pwinput()
        elif reply == '3':
                    # username = input('Username: ').strip().lower()
                    password = pw.pwinput()
        elif reply == '4':
                    # username = input('Username: ').strip().lower()
                    password = pw.pwinput()
        elif reply == '5':
                    # username = input('Username: ').strip().lower()
                    password = pw.pwinput()

    def transfer(self):
        reciever = input("Input reciever's account number:  ")

  
invoice = bank()