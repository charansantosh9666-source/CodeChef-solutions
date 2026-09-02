# cook your dish here
a,b,c=map(int,input().split())
if(a<b and a<c):
    print("Increasing")
elif(a>b and a>c):
    print("Decreasing")
else:
    print("Neither")