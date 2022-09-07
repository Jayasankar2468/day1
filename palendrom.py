n=int(input("Enter the name:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The name is a palindrome!")
else:
    print("The name isn't a palindrome!")
