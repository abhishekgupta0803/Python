#Create Calculate in python
first=input("Enter first Number : ")
operator=input("+,-,/,% :")
second=input("Enter second Number : ")
first=int(first)
second=int(second)
if(operator=='+'):
    print(first+second)
elif(operator=='-'):
    print(first-second)
elif(operator=='/'):
    print(first/second)
elif(operator=='%'):
    print(first%second)
else:
    print("Invalid")