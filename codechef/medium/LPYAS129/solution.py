numbers = list(map(int, input().split()))
# Update your code below this line
n=len(numbers)
for i in range(0,n):
    a=numbers[i]
    c=0
    for j in range(0,n):
        if(i!=j and a==numbers[j]):
            c+=1
    if(c==0):
        print(a)
        break