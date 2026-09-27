# cook your dish here
a,b,c=map(int,input().split())
if(a>b):
    ans=((c-b)*b)+a
else:
    ans=((c-a)*b)+a
print(ans)