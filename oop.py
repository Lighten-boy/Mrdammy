class Parent:
    def __init__(self, first_name, age):
       self.age = age
       self.first_name = first_name
       self.last_name = 'Solademi'
       self.height = '5ft'
       self.complexion = 'Chocolate'
       self.hobby = 'Coding'

    def intro(self):
        print(f'My name is {self.first_name} {self.last_name}. I am {self.height} tall and {self.complexion} in complexion. I am {self.age} years old and i love {self.hobby}.')


        self.walking

    def walking(self, adj='Very fast'):
        print(f'{self.first_name} {self.last_name} is walking {adj}')



class Child(Parent):
    def __init__(self, first_name, age):
        super().__init__(first_name, age)

leumas = Child('Leumas', 7)
