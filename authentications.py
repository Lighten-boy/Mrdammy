import pwinput as pw
import json

# Creating a  note: comment after creation

# personnels_login = {}
# database = json.dumps(personnels_login)
# print(database)
# with open(r'C:\myclass\cbt.py', 'w') as file:
#     file.write(database)

print('''
        Welcome
    
    1. Sign Up
    2. Login
''')
user = input('Choice: ').strip()

if user == '1':
    # Signin up

    file = open(r'C:\myclass\cat.py', 'r')
    database = file.read()
    personnels_login = json.loads(database)
    print(personnels_login)

    print(f'Sign Up'.center(50,'_'))
    username = input('Username: ').strip().lower()
    password = input('Password: ')
    
    personnels_login.update({username:password})
    print(personnels_login)

    # saving to a database
    database = json.dumps(personnels_login)
    print(database)
    with open(r'C:\myclass\cat.py', 'w') as file:
        file.write(database)

elif user == '2':
    # To login, Fetch you data from the database

    file = open(r'C:\myclass\cat.py', 'r')
    database = file.read()
    personnels_login = json.loads(database)
    print(personnels_login)

    print('Login'.center(50, '_'))

    username = input('Username: ').strip().lower()
    password = pw.pwinput()

    if password == personnels_login[username]:
        print('welcome....')
    else:
        print('Wrong username and password')

else:
    print('Invalid input')