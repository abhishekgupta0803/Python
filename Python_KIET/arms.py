n=int (input())
temp=n
s=0
while n!=0:
    r=n%10
    s=s+(r**3)
    n=n//10
if s==temp:
        print("It is Armstrong Number")
else:
        print("It is not Armstrong Number")