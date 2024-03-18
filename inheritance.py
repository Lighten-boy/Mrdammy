class Parent:
    def __init__(self):
       
       self.age = 22
       self.first_name = 'israel'
       self.last_name = 'Solademi'
       self.height = '5ft'
       self.complexion = 'Chocolate'
       self.hobby = 'Coding'

    #    self.intro()



    def intro(self):
        print(f'My name is {self.first_name} {self.last_name}. I am {self.height} tall and {self.complexion} in complexion. I am {self.age} years old and i love {self.hobby}.\n\n')


        # self.walking()

    def running(self, adj='Very fast'):
        print(f'{self.first_name} {self.last_name} is running {adj}\n\n')



class Child(Parent):
    def __init__(self):
        super().__init__()
        self.age = 7
        self.first_name = 'Leumas'
        self.height = '4.5ft'
        self.complexion = 'Light'
        self.hobby = 'singing'
    
        # self.intro()


# leumas = Child()
# leumas.intro()
# leumas.running()

class Grandchild(Child):
    def __init__(self):
        Child.__init__(self)
        self.age = 5
        self.first_name = 'Daniel'
        self.height = '3.5ft'
        self.complexion = 'Light'
        self.hobby = 'racing'

daniel = Grandchild()

daniel.intro()

# victor = Child()
# victor.first_name = 'Victor'
# victor.complexion = 'chocolate'
# victor.age = 17
# victor.hobby = 'swiming'
# victor.intro()




# class Child2(Parent):
#     def __init__(self):
#         super().__init__()
#         self.age = 5
#         self.first_name = 'Matthew'
#         self.height = '3.5ft'
#         self.complexion = 'Light'
#         self.hobby = 'Playing games'
    
#         self.intro()


# leumas = Child2()