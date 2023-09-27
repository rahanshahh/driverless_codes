a=[]
n =int(input("the number of elements in the array"))
for i in range(0,n):
    l=int(input())
    a.append(l)
print("your array is ", a)
a.sort()
print("the largest number in array is: ")
print(a[n-1])