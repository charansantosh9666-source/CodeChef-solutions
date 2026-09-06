n = int(input())
# Update the code below this line
a=0
b=1
sum=0
print(a,b,end=" ")
for i in range(2,n):
    sum=a+b
    print(sum,end=" ")
    a,b=b,sum