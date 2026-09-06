numbers = list(map(int, input().split()))
# Update your code below this line
n=len(numbers)
for i in range(0,n):
    if(8==numbers[i]):
        print(i)
        break