a=int(input("enter any number of your choice"))
b=int(input("enter another number of your choice"))
c=int(input("enter yet another number of your choice"))
if(a>=b and a>c):
    print(a," is maximum")
elif(b>=a and b>c):
    print(b," is maximum")
else:
    print(c," is maximum")
