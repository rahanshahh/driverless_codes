a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("enter any multiplication operation of your choice")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(abs(a-b))
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
else:
    print("invalid choice")