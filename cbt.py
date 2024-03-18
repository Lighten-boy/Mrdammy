import time
import json
import pwinput as pw


# personnels_login = {}
# database = json.dumps(personnels_login)
# print(database)
# with open(r'C:\myclass\cbt.txt', 'w') as file:
#     file.write(database)

# user = int(input('How many student are taking this test: '))
students = []


class Cbt:
    def __init__(self):
        self.home()

    def home(self):
        print('Cbt page'.center(30,'_'))
        print('1. Sign up\n2. Login\n3. Exit')
        user = input('choose your option: ')
        if user == '1':
            self.sign_up()
        elif user == '2':
            self.login()
        elif user == '3':
            exit()
        else:
            print('Invalid Input!!!\n')
            time.sleep(2)
            self.home()


    def sign_up(self):
        print('Sign up')
        file = open(r'C:\myclass\cbt.txt', 'r')
        database = file.read()
        personnels_login = json.loads(database)
        # print(personnels_login)  

        print(f'Sign Up'.center(50,'_'))
        username = input('Username: ').strip().lower()
        # email = username = input('Email: ').strip().lower()
        password = input('pin (4 Digit): ').strip()

        personnels_login.update({username:password})
        print(personnels_login)

        # saving to a database
        database = json.dumps(personnels_login)
        # print(database),
        with open(r'C:\myclass\cbt.txt', 'w') as file:
            file.write(database)


        print('Sign up successful. Redirecting to login page')
        time.sleep(2)
        self.login()


    def login(self):
        file = open(r'C:\myclass\cbt.txt', 'r')
        database = file.read()
        personnels_login = json.loads(database)
        # print(personnels_login)
        print('Login'.center(50, '_'))

        username = input('Username: ').strip().lower()
        password = pw.pwinput()

        if password == personnels_login[username]:
            print('welcome....')
            # for each_studemt in personnels_login:
            #      name = input('Student name: ')
            #      ID = input('Input your student Id to get started')
            #      students.append(name)
            # scores = []
            # for student in students:
            #      print(f'{student} is about to take the test')
            #      questions = [
            #      "1. Who is the current president of Nigeria?   a.)Tinubu b.)Buhari",
            #      "2. When did Nigeria got her independence?   a.)1892 b.)1960",
            #      "3. who owns Twitter   a.)musk Elon b.)Elon musk",
            #      "4. Who is the richest person in the world   a.)israel b.)nobody",
            #      "5. Who is the fastest runner in the world   a.)usain bolt b.)Buhari",
            #      "6. Who is the first executive president in Nigeria   a.)Shagari b.)Azikiwe",
            #      "7. How many continent are there in the world   a.)9 b.)7",
            #      "8. How many States are in Nigeria   a.)35 b.)36",
            #      "9. 2+2   a.)5 b.)4",
            #      "10. 36/6   a.)6 b.)3",
            #      "11. who code this work   a.)Israel b.)John",
            #      "12. If i have two apples and you have one so i give you one apples from mine how many apples do i have left   a.)1 b.)0"
            #      ]

            #      answers = ['a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'a']

            #      score = 0

            #      for que, ans in zip(questions,answers):
            #          print(que)
            #          user= input('Answers: ')
            #          if user.strip().lower() == ans:
            #              print('corect')
            #              score+=5
            #          else:
            #              print('Why you know no book!')

            #      print(f'{student} your total score is {score}\n\n')
            #      scores.append(score)

            #      for stud, scr in zip(students, scores):
            #          print(f'{stud}, {scr}')

        
        else:
            print('Wrong username and password')



        self.home()       


cbt = Cbt()




# user = int(input('How many student are taking this test: '))
# students = []

# for each_studemt in range(user):
#         name = input('Student name: ')
#         ID = input('Input your student Id to get started: ')
#         students.append(name)
# scores = []
# print(students)
# for student in students:
#         print(f'{student} is about to take the test')
#         questions = [
#         "1. Who is the current president of Nigeria?   a.)Tinubu b.)Buhari",
#         "2. When did Nigeria got her independence?   a.)1892 b.)1960",
#         "3. who owns Twitter   a.)musk Elon b.)Elon musk",
#         "4. Who is the richest person in the world   a.)israel b.)nobody",
#         "5. Who is the fastest runner in the world   a.)usain bolt b.)Buhari",
#         "6. Who is the first executive president in Nigeria   a.)Shagari b.)Azikiwe",
#         "7. How many continent are there in the world   a.)9 b.)7",
#         "8. How many States are in Nigeria   a.)35 b.)36",
#         "9. 2+2   a.)5 b.)4",
#         "10. 36/6   a.)6 b.)3",
#         "11. who code this work   a.)Israel b.)John",
#         "12. If i have two apples and you have one so i give you one apples from mine how many apples do i have left   a.)1 b.)0"
#         ]

#         answers = ['a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'b', 'a', 'a', 'a']

#         score = 0

#         for que, ans in zip(questions,answers):
#             print(que)
#             user= input('Answers: ')
#             if user.strip().lower() == ans:
#                 print('')
#                 score+=5
#             else:
#                  print('')

#         print(f'{student} your total score is {score}\n\n')
#         scores.append(score)
#         print("This are the results of those who wrote the test\n")
#         time.sleep(2)

# for stud, scr in zip(students, scores):
#         print(f'{stud} score, {scr}')