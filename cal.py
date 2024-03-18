val1= int(input("Value 1 = "))
val2 = int(input("Value 2 = "))
print("1. Addition\n 2.Subtraction\n 3.Division\n 4.Multiplecation")
user = input("enter choice : ")
if user == "1":
    print(val1+val2)
elif user == "2":
    print(val1-val2)
elif user == "3":
    print(val1/val2)
elif user == "4":
    print(val1*val2)
else:
    print("Syntax Error")