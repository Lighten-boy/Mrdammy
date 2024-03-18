import pwinput as pw
import json

# personnels_login = {
# }
# Database = json.dumps(personnels_login)
# print(Database)
# with open("c:\\myclass\\cbt.txt", 'a') as file:
#         file.write(Database)



personnels_login = {}
print('''
        welcome
      
    1. sign up
    2. login
''')
user = input('choice: ').strip()

if user == '1':
    #   Sign up

    file = open("c:\\myclass\\cbt.txt", 'r')
    Database = file.read()
    personnels_login = json.loads(Database)
    # print(personnels_login)

    print(f'sign up'.center(50,'_'))
    username = input('username: ')
    password = input('password: ')

    if personnels_login[-1][-1]:
        id = personnels_login[-1][-1] + 1
    else:
        id = 1 

    personnel_login = (username, password)
    personnels_login.append(personnel_login)
    print(personnels_login)

    # Saving to a temporary database
    Database = json.dumps(personnels_login)
    print(Database)
    with open("c:\\myclass\\cat.txt", 'w') as file:
        file.write(Database)











personnels_login = []

for user in range(3):

    print(f'sign up personnel {user+1}'.center(50,'_'))
    username = input('username: ')
    password = input('password: ')
    personnel_login = (username, password)
    personnels_login.append(personnel_login)


# print(personnels_login)
print('Login'.center(50,'_'))
id = int( input('id: '))
username = input('username: ')
password = pw.pwinput()

if username in personnels_login[id-1] and password in personnels_login[id-1]:
    print('welcome....')
else:
    print('Wrong user name and password')