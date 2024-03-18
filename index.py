numbers = range(1, 101, 2)

#print(list(numbers))
#print(tuple(numbers))

value = {1, 2, 3, 4, 4}
guess_word = {
    'Good',
    'Amapiano',
    'SQI',
    'Math',
    'Cobra'
}
#print(value)
#print(guess_word)

vehicle = {'model':'Toyota camry', 'YOP':'2014', 'color':'Gold'}
#print(len(vehicle))
#print(vehicle['YOP'])

basket = [
    'Garri',
    'Fruits',
    'Tomato'
]
#print(basket[0])

number =  bin(7)
#print(number)

number = bytes('Ayomide', encoding='utf8')
#print(number)

name = 'Ayomide' #['A', 'y', 'o', 'm', 'i', 'd', 'e']
#print(name[4])

#print(ord('A'))
#print(ord('y'))
#print(ord('o'))
#print(ord('m'))
#print(ord('i'))
#print(ord('d'))
#print(ord('e'))


value = 45
val = float(value)
#print(val)

# Python_student = ['Paul', 'Victor', 'Samuel', 'Helen', 'Leumas']
# print('Leumaas' in Python_student)

# x = 5
# y = 10
# if y == 10 and x <= 5:
#     print('Correct')

# else:
#     print('Wrong')

# degood_food = [
#     'rice',
#     'beans',
#     'bread'
# ]

# degood_comp = [
#     'meat',
#     'fish',
#     'egg'
# ]

# degood_drinks = [
#     'coke',
#     'fanta',
#     'water'
# ]
# user = input('Your name: ').strip().lower()
# User_food = input('Food: ').strip().lower()
# User_comp = input('Compliment: ').strip().lower()
# User_drink = input('Drink: ').strip().lower()

# if (User_food in degood_food) and (User_comp in degood_comp) and (User_drink in degood_drinks):
#     print(f"""
#             Degood resturant
#         Order from {user}
#         1. {User_food}
#         2. {User_comp}
#         3. {User_drink}

#         {user}, make payment
#         payment option:
#         1. Transfer
#         2. Debit card
#         3. Cash
#         """)
#     user_option = input('payment Option: ')
#     if user_option == '1':
#         print('send payment receipt')
#     elif user_option == '2':
#         print('payments received')
#     elif user_option == '3':
#         print('payments received')
#     else:
#         print('Invaild Transaction')

# elif (User_food in degood_food) or (User_comp in degood_comp) or (User_drink in degood_drinks):
#     print('we do not have all your requests')
#     print(f"""
#     Food menu: rice, beans, bread.
#     Complement menu: meat, fish, egg.
#     Drinks menu: coke, fanta, water.
#     """)
# else:
#     print('Order not available, Please come back later.')

My_list = ['mango', 'Apple', 'Pineapple','Banana','Watermelon', 'Plum']
# print(My_list[5])

# name = ('dam')
# print(name[::-1])

# name = input('name: ').strip().capitalize()
# print(name[::-1])

# My_list[0] = 'pawpaw'
# print(My_list)

# My_list.append('light')
# print(My_list)

# print(My_list.count('Pineapple'))

# My_list.insert(3, 'goat')
# print(My_list)

# My_list.pop(5)
# print(My_list)

num = [1, 4, 3, 5, 2, 7, 6]
# print(sum(num)/len(num))
# print(max(num))
# print(min(num))
# num.sort(reverse = False)
# num.sort(reverse = True)
# print(num)

# x = 1
# fruit = ['mango', 'Apple', 'Pineapple','Pineapple','Pineapple', 'Plum']
# for pop in fruit:
#     print(f'''
#     student {x}: {pop}
#     ''')
#     x+=1


# var = 'Welcome'
# for x in var:
#     print(x)

# questions = [
#     "1. Who is the richest person in the world a.) Me b.) You",
#     "2. Who is the fastest person in the world a.) Oyo b.) Abuja"
# ]

# answers = ['a', 'b']

# score = 0

# for que, ans in zip(questions,answers):
#     print(que)
#     user= input('Answers: ')
#     if user.strip().lower() == ans:
#         print('corect')
#         score+=5
#     else:
#         print('Why you know no book!')

# print(f'your total score is {score}')




# Shopping = [
#     "1. Beans #100",
#     "2. Rice #100"
# ]

# Price = ['yes', 'yes']

# Total = 0

# for goods, label in zip(Shopping,Price):
#     print(goods)
#     user= input('Do you want to add: ')
#     if user.strip().lower() == label:
#         print('Added to cart')
#         Total+=100
#     else:
#         Total+=0

# print(f'your total price is {Total}')



# Price = 0
# Item1 =input("beans\n\n Do you want to add this to cart:  ").strip().capitalize()
# if (Item1 == "Yes"):
#     Price +=100
# else:
#     Price+=0
# Item2 =input('rice\n\n Do you want to add this to cart:    ').strip().capitalize()
# if (Item2 =='Yes'):
#     Price+=700
# else:
#     Price +=0
# Item3 =input('indomie\n\n Do you want to add this to cart:   ').strip().capitalize()
# if (Item3 == 'Yes'):
#     Price+=200
# else:
#     Price +=0 

# print('Dear customer, this is your Total Price.',Price)


# val = list(range(1, 13))

# y = 1
# for x in val:
#     print(f'{x} x {y} = {x*y}')


# for x in range(1, 13):
#     print(f'\n{x} Times table')
#     for y in range(1, 13):
#         # print(y)

#         print(f'{x} x {y} = {x*y}')

# Using a title
# sentence = 'i studied at sQI'
# newsent = sentence.title()
# print(newsent)

# Using of find
# sent = "You're not a fool"
# print(sent.find('fool'))

# print(sent.replace(' ','%20'))

# sentence = 'I  would like to eat pizza'
# splitted = sentence.split()
# splitted.sort(key=str.lower)
# print(splitted)




user = int(input('Note only number\nHow many student are taking this test: '))
students = []

for each_student in range(user):
    name = input('Student name: ')
    ID = input('Input your student Id to get started: ')
    students.append(name)
scores = []
# print(students)
for student in students:
    print(f'{student} is about to take the test')
    questions = [
    "1. Who is the current president of Nigeria?   a.)Tinubu b.)Buhari",
    "2. When did Nigeria got her independence?   a.)1892 b.)1960",
    # "3. who owns Twitter   a.)musk Elon b.)Elon musk",
    # "4. Who is the richest person in the world   a.)israel b.)nobody",
    # "5. Who is the fastest runner in the world   a.)usain bolt b.)Buhari",
    # "6. Who is the first executive president in Nigeria   a.)Shagari b.)Azikiwe",
    # "7. How many continent are there in the world   a.)9 b.)7",
    # "8. How many States are in Nigeria   a.)35 b.)36",
    # "9. 2+2   a.)5 b.)4",
    # "10. 36/6   a.)6 b.)3",
    # "11. who code this work   a.)Israel b.)John",
    # "12. If i have two apples and you have one so i give you one apples from mine how many apples do i have left   a.)1 b.)0"
    ]

    answers = ['a', 'b']

    score = 0

    for que, ans in zip(questions,answers):
        print(que)
        user= input('Answers: ')
        if user.strip().lower() == ans:
            print('corect')
            score+=5
        else:
          print('Why you know no book!')

    print(f'{student} your total score is {score}\n\n')
    scores.append(score)

for stud, scr in zip(students, scores):
    print(f'{stud}, {scr}')



# user = input('Input your email: ').strip()
# if '@' and '.' in user:
#     print('valid email')
# else:
#     print('invalid')




# students = ['shola', 'ade']
# scores = [12, 14]
# avg = sum(scores)/len(scores)
# max_score = max(scores)

# # print(avg)
# # print(max_score)

# index_max = scores.index(max_score)
# student_max = students[index_max]
# print(f"{student_max} had the highiest score")




# import pwinput as pw

# personnels_login = []

# for user in range(3):

#     print(f'sign up personnel {user+1}'.center(50,'_'))
#     username = input('username: ')
#     password = input('password: ')
#     personnel_login = (username, password)
#     personnels_login.append(personnel_login)


# # print(personnels_login)
# print('Login'.center(50,'_'))
# id = int( input('id: '))
# username = input('username: ')
# password = pw.pwinput()

# if username in personnels_login[id-1] and password in personnels_login[id-1]:
#     print('welcome....')
# else:
#     print('Wrong user name and password')


# info = ('Hen Hen', 'Helen', '1234', 'hen@gmail.com',5000)
# info = list(info)
# info[2] = input('change password: ')
# info = tuple(info)
# print(info)
    
# w, x, y, z = info
# print(w)
# *x, = info
# print(x)
# x[2] = input('change password: ')
# info = tuple(x)
# print(info)


# values = [
#     ('a','1. Who is the current president of Nigeria?   (a) Tinubu (b) Buhari'),
#     ('b','2. Who is the current president of Nigeria?   (a) Tinubu (b) Buhari'),
# ]
# for ans, ques in values:
#     print(ques)
#     user = input('ans: ')
#     if user == ans:
#         print('correct')
#     else:
#         print('wrong')




# name = {"apple", "water", "cocoa","fruit"}
# newName = ("hot", "cold")

# vehicle = {
#     'name':'Toyota',
#     'model':'highlander',
#     'color':['green','black'],
#     'year':2022,
#     'status':{
#         'brand_new':True,
#         'Fairly_used':False,
#         'hand to hand':False
#     }
# }

# print(vehicle['status']['brand_new'])
# vehicle
# print(vehicle.keys())
# print(vehicle['status'].keys())
# print(vehicle.items())

# for each in vehicle.values():
#     print(each)



# for x , y in vehicle.items():
#     print(f'{x}: {y}')    

# print('1. Data plan\n2. Check balance')
# value = {'1':'Data plan', '2':'Check balance'}
# for key, val in value.items():
#     user = input('Your option: ')
#     if user == key:
#         print(value[user])



# val = ['tom', 'pep']
# dic = {}
# dic = dic.fromkeys(val, '20')
# print(dic)


# personnel_login = []
# # ID = []
# for user in range(2):
#     print(f'Id {user+1}'.center(50,'_'))
#     students_detail = {
#     'ID':{
#         'name':input('name: '),
#         'matric no':input('M no: '),
#         'gender':input('Gen: ')
#     }
# }

# print(personnel_login)
# print('Login'.center(50,'_'))
# ID = int( input('id: '))

# print(students_detail)


# students_details = {
#     'ID':{
#         'name':'',
#         'matric no':''
#     }
# }

# students_details = {}
    
# for x in range(3):
#     student = {}
#     name = input(f'Name{x+1}: ')
#     matric_no = input(f'Matric no {x+1}: ')
#     student['Name'] = name
#     student['Matric no'] = matric_no
#     # print(student)
#     students_details[f'Id{x+1}'] = student

# print(students_details)

# import json


# dic_file = {"Name":"Arise Dammy", "Year":"2023"}
# # print(type(dic_file))
# json_file = json.dumps(dic_file)
# # print(type(json_file))
# with open("c:\\myclass\\cbt.txt", 'w') as myfile:
#     myfile.write(json_file)


# x = 1
# while x <= 10:
#     print(f'you are welcome{x}')
#     x +=1

# x = 10
# while x > 0:
#     print('i will no do it again', x)

#     x -=1

# ussd = input('Enter ussd code: ')

# while ussd != "*131#":
#     ussd = input('invalid input !! try again: ')

# print ('''
#         1. daily plan
#         2. weekly plan
#     ''')


# std_name = []
# x = 1
# admin_slot = 10
# while x <= admin_slot:
#     name = input (f'Enter student name {x}, press "done" to quit: ')
#     if name == "done":
#         break
#     x+=1
#     std_name.append(name)
# print(std_name)


# user = input("Input website:")
# while user != "index.com":
#     user = input("No connection, Try again: ")
# print("Welcome to Index")



# def speed(name_of_object: str, rate:int = 1):
#     print(f'About to increase the speed of your {name_of_object} at {rate}km/hr')

# speed('G-wagon')

# import time


# def Addition():

#     value1 = int(input('First value: '))
#     value2 = int(input('Second value: '))
#     result = value1 + value2
#     print(f'Ans:{result}')
#     print(f'\nreturn to home page....')
#     Landing_page()





# def Division():

#     value1 = int(input('First value: '))
#     value2 = int(input('Secondt value: '))
#     result = value1 / value2
#     print(f'Ans:{result}')
#     print(f'\nreturn to home page....')
#     Landing_page()





# def Subtraction():

#     value1 = int(input('First value: '))
#     value2 = int(input('Second value: '))
#     result = value1 - value2
#     print(f'Ans:{result}')
#     print(f'\nreturn to home page....')
#     Landing_page()




# def multiplication():

#     value1 = int(input('First value: '))
#     value2 = int(input('Second value: '))
#     result = value1 * value2
#     print(f'Ans:{result}')
#     print(f'\nreturn to home page....')
#     Landing_page()



# def Landing_page():
#     print('''
#           My super calculator

#         choose operation;
#           1. Subtraction
#           2. Multiplication 
#           3. addition
#           4. division
#           5. exit
#           ''')
#     user = input('option: ')
#     if user == '1':
#         Subtraction()
#     elif user == '2':
#         multiplication()
#     elif user == '3':
#         Addition()
#     elif user == '4':
#         Division()
#     elif user == '5':
#         exit()
#     else:
#         print('Syntax Error')
#         Landing_page()


# Landing_page()





# class Parent:
#     def __init__(self, first_name, age):
#        self.age = age
#        self.first_name = first_name
#        self.last_name = 'Solademi'
#        self.height = '5ft'
#        self.complexion = 'Chocolate'
#        self.hobby = 'Coding'

#     def intro(self):
#         print(f'My name is {self.first_name} {self.last_name}. I am {self.height} tall and {self.complexion} in complexion. I am {self.age} years old and i love {self.hobby}.')


#         self.walking

#     def walking(self, adj='Very fast'):
#         print(f'{self.first_name} {self.last_name} is walking {adj}')


# class Child(Parent):
#     def __init__(self, first_name, age):
#         super().__init__(first_name, age)

# leumas = Child('Leumas', 7)

# # israel = Human()
# # israel = Human('Israel', 20)

# # israel.walking()
# # israel.intro()
# # print(israel.last_name)
# # print(type(israel))


# import time
# import json
# import pwinput as pw


# # personnels_login = {}
# # database = json.dumps(personnels_login)
# # print(database)
# # with open(r'C:\myclass\oop.txt', 'w') as file:
# #     file.write(database)


# class Create_Invoice:
#     def __init__(self):
#         self.home()

#     def home(self):
#         print('Invoice Creator'.center(30,'_'))
#         print('1. Sign up\n2. Login\n3. Exit')
#         user = input('choose your option: ')
#         if user == '1':
#             self.sign_up()
#         elif user == '2':
#             self.login()
#         elif user == '3':
#             exit()
#         else:
#             print('Invalid Input!!!\n')
#             time.sleep(2)
#             self.home()


#     def sign_up(self):
#         print('Sign up')
#         file = open(r'C:\myclass\cat.py', 'r')
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
#         with open(r'C:\myclass\cat.py', 'w') as file:
#             file.write(database)


#         print('Sign up successful. Redirecting to login page')
#         time.sleep(2)
#         self.login()


#     def login(self):
#         file = open(r'C:\myclass\cat.py', 'r')
#         database = file.read()
#         personnels_login = json.loads(database)
#         # print(personnels_login)
#         print('Login'.center(50, '_'))

#         username = input('Username: ').strip().lower()
#         password = pw.pwinput()

#         if password == personnels_login[username]:
#             print('welcome....')
#         else:
#             print('Wrong username and password')



#         self.home()       


# invoice = Create_Invoice()






# import random
# num = random.randint(38569634,3697346996)

# self.account_no = random.randint(38569634,3697346996)
# print(num)