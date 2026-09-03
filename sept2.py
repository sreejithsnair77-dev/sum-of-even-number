n=int(input("enter a number : "))
a=0
b=0
for i in range(n,1,-1):
    if i%2==0:
        a+=i
        b+=1
print("sum of even number : ",a)
print("count of even number : ",b)
