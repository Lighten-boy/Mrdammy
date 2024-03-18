import time

# Shopping = [
#     "1. Beans #100",
#     "2. Rice #100",
#     "3. Indomie #100",
#     "4. Yam #100",
#     "5. Coke #100",
#     "6. Fanta #100",
#     "7. 5Alive #100"
# ]

# Price = ['yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes']

# Total = 0

# for goods, label in zip(Shopping,Price):
#     print(goods)
#     user= input('Do you want to add this to cart: ')
#     if user.strip().lower() == label:
#         print('Added to cart')
#         Total+=100
#     else:
#         Total+=0

# print(f'your total price is {Total}')



Price = 0
Item1 =input("beans\n Do you want to add this to cart:  ").strip().capitalize()
if (Item1 == "Yes"):
    Price +=100
else:
    Price+=0
Item2 =input('\n\nrice\n Do you want to add this to cart:    ').strip().capitalize()
if (Item2 =='Yes'):
    Price+=700
else:
    Price +=0
Item3 =input('\nindomie\n Do you want to add this to cart:   ').strip().capitalize()
if (Item3 == 'Yes'):
    Price+=200
else:
    Price +=0 
Item4 =input('\nYam\n Do you want to add this to cart:   ').strip().capitalize()
if (Item4 == 'Yes'):
    Price+=200
else:
    Price +=0 
Item5 =input('\nCoke\n Do you want to add this to cart:   ').strip().capitalize()
if (Item5 == 'Yes'):
    Price+=200
else:
    Price +=0 
Item6 =input('\nFanta\n Do you want to add this to cart:   ').strip().capitalize()
if (Item6 == 'Yes'):
    Price+=200
else:
    Price +=0 
Item7 =input('\n5Alive\n Do you want to add this to cart:   ').strip().capitalize()
if (Item7 == 'Yes'):
    Price+=200
else:
    Price +=0 

print('Dear customer, this is your Total Price.',Price)
# print('Lighten shop'.center(50, '_'))
# products = [
#     'Beans',
#     'Rice',
#     'Indomie',
#     'Coke',
#     'Fanta',
#     '5Alive',
#     'Lighten drinks'
# ]

# prices = [
#     10_000,
#     200_000,
#     3_000_000,
#     20_000,
#     1_000,
#     10_000,
#     700_000_000
# ]
# x = 1
# time.sleep(2)
# print('\navailable items')
# for prod, price in zip(products,prices):
#     print(f'\n{x} {prod}: #{price:,}')
#     x+=1 

# user =int(input('choose item number: '))
# if user == '1':
#         print(input('how many: '))
# elif user == '2':
#      print(input('how many: '))
# elif user == '3':
#      print(input('how many: '))
# elif user == '4':
#      print(input('how many: '))
# elif user == '5':
#      print(input('how many: '))
# elif user == '6':
#      print(input('how many: '))
# elif user == '7':
#      print(input('how many: '))              

# print(f'you are about to purchase {products[user-1]} which cost #{prices[user-1]:,}')
